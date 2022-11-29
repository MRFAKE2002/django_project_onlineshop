from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('contact_us/', views.ContactUsPageView.as_view(), name='contact_us'),
]
