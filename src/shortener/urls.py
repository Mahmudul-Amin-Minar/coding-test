from django.urls import path

from .views import HomePage, ShortenURLView, UrlListView

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
    path('list-url/', UrlListView.as_view(), name='list'),
    path('<shortcode>/', ShortenURLView.as_view(), name='scode'),
]
