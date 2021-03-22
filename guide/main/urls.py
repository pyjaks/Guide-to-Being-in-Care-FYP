from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='main'),
    path('age-check', views.HomePageView.as_view(template_name="age-check.html")),
    path('your-rights', views.HomePageView.as_view(template_name="your-rights.html")),
    path("5-8", views.YoungerChildPageView.as_view(), name='5-8'),
    path("16+", views.HomePageView.as_view(template_name="16+.html"))
]
