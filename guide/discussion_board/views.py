from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, DetailView, ListView
from .forms import *


class DiscussionBoardHomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['discussion_boards'] = Category.objects.all()
        return context


class DiscussionBoardDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class DiscussionBoardPostsView(ListView):
    model = Post

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Post.objects.filter(categories=self.category)


