from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='main'),
    path('age-check', views.HomePageView.as_view(template_name="age-check.html")),
    path("5-8", views.YoungerChildPageView.as_view(), name='5-8'),
    path('your-rights', views.HomePageView.as_view(template_name="your-rights.html")),
    path("your-education", views.HomePageView.as_view(), name='your-education'),
    path("your-wellbeing", views.HomePageView.as_view(), name='your-wellbeing'),
    path("your-voice", views.HomePageView.as_view(), name='your-voice'),
    path("your-skills", views.HomePageView.as_view(), name='your-skills'),
    path("what-does-that-mean", views.HomePageView.as_view(template_name="what-does-that-mean.html"), name='what-does-that-mean'),
    path("16+", views.SixteenPlusPageView.as_view(template_name="16+.html"), name='16+'),
]
