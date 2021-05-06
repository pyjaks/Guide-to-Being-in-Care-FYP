from datetime import datetime

from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, DetailView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404

from .forms import *
from .models import Category, Author


class DiscussionBoardHomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['discussion_boards'] = Category.objects.all()
        return context


class DiscussionBoardDetailView(DetailView):
    model = Post

    def get(self, request, *args, **kwargs):
        response = super().get(self, request, *args, **kwargs)
        if self.object.approved:
            return response
        else:
            raise Http404

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class DiscussionBoardPostsView(ListView):
    model = Post

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Post.objects.filter(categories=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        return context


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'categories']

    def form_valid(self, form):
        model_instance = form.save(commit=False)
        model_instance.user = Author.objects.get(user=self.request.user)
        model_instance.datePosted = datetime.now()
        model_instance.save()
        return super().form_valid(form)


