import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from urlshortener.settings import VALIDITY

from .forms import UrlForm, UrlFormLoggedUsers
from .models import ShortenUrl

# Create your views here.

class HomePage(View):
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            form = UrlFormLoggedUsers()
        else:
            form = UrlForm()
        context = {
            "title": "Submit Url",
            "form": form
        }
        return render(request, "shortener/home.html", context)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            form = UrlFormLoggedUsers(request.POST)
        else:
            form = UrlForm(request.POST)
        context = {
            'title': 'Submit Url',
            'form': form
        }
        template = 'shortener/home.html'

        if form.is_valid():
            new_url = form.cleaned_data.get('url')
            custom_shortcode = form.cleaned_data.get('shortcode') or ""
            validity = form.cleaned_data.get('valid_for') or VALIDITY

            s = new_url
            s = s.replace('www.', '')
            if 'http://' in s or 'https://' in s:
                s = s
            else:
                s = 'http://' + s
            obj, created = ShortenUrl.objects.get_or_create(url=s, shortcode=custom_shortcode, validity=validity)
            try:
                obj.user = self.request.user
                obj.save()
            except:
                pass
            context = {
                'object': obj,
                'created': created
            }
            if created:
                template = 'shortener/success.html'
            else:
                template = 'shortener/exist.html'
        return render(request, template, context)


class ShortenURLView(View):

    def get(self, request, shortcode=None, *args, **kwargs):
        qs = ShortenUrl.objects.filter(shortcode__iexact=shortcode)
        if qs.count() == 1 and qs.exists():
            obj = qs.first()
            return HttpResponseRedirect(obj.url)
        else:
            raise Http404

class UrlListView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        qs = ShortenUrl.objects.filter(user=request.user)
        for q in qs:
            td = datetime.datetime.now(datetime.timezone.utc) - q.timestamp
            if td.days > q.validity:
                q.active = False
        context = {
            "title": "Shortened URL List",
            "objects": qs
        }
        return render(request, "shortener/list.html", context)
