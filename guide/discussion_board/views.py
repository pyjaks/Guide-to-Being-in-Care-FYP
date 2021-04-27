from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, ListView
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


class DiscussionBoardPostsView(ListView):
    model = Post

    def get_queryset(self):
        self.category = get_object_or_404(Category, title=self.kwargs['slug'])
        return Post.objects.filter(categories=self.category)


