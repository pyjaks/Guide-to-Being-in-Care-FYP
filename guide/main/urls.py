from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='main'),
    path('age-check', views.HomePageView.as_view(template_name="age-check.html")),
    path('your-rights', views.HomePageView.as_view(template_name="your-rights.html")),
]
