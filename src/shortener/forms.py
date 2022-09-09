from cProfile import label
from wsgiref.validate import validator
from django import forms
from .validators import validate_url

class UrlForm(forms.Form):
    url = forms.CharField(label='Submit Url', validators=[validate_url])

class UrlFormLoggedUsers(forms.Form):
    url = forms.CharField(label='Submit Url', validators=[validate_url])
    shortcode = forms.CharField(label="custom shortcode", required=False)
    valid_for = forms.IntegerField(label="Valid for", required=False)