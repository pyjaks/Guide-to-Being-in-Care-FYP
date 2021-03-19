from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='main'),
    path('age-check', views.AgeCheckView.as_view(), name='age-check'),
]
