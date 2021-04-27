from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import *
from .forms import *
from main.views import HomePageView


# Create your views here.
# class HomePageView(TemplateView):
#     template_name = "home.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context
#
class DiscussionBoardDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

