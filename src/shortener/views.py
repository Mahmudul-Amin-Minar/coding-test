from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UrlForm
from .models import ShortenUrl

# Create your views here.

class HomePage(View):
    
    def get(self, request, *args, **kwargs):
        form = UrlForm()
        context = {
            "title": "Submit Url",
            "form": form
        }
        return render(request, "shortener/home.html", context)

    def post(self, request, *args, **kwargs):
        form = UrlForm(request.POST)
        context = {
            'title': 'Submit Url',
            'form': form
        }
        template = 'shortener/home.html'

        if form.is_valid():
            new_url = form.cleaned_data.get('url')
            s = new_url
            s = s.replace('www.', '')
            if 'http://' in s or 'https://' in s:
                s = s
            else:
                s = 'http://' + s
            obj, created = ShortenUrl.objects.get_or_create(url=s)
            # obj.user = self.request.user or None
            # obj.save()
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
        print(request.user.id)
        qs = ShortenUrl.objects.filter(user=request.user)
        context = {
            "title": "Shortened URL List",
            "objects": qs
        }
        return render(request, "shortener/list.html", context)
