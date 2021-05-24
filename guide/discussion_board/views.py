from datetime import datetime

from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import TemplateView, DetailView, ListView, CreateView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseForbidden
from django.urls import reverse

from .forms import *
from .models import Category, Author


class DiscussionBoardHomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['discussion_boards'] = Category.objects.all()
        context["posts"] = Post.objects.all()
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'

    def get(self, request, *args, **kwargs):
        response = super().get(self, request, *args, **kwargs)
        if self.object.approved:
            return response
        else:
            raise Http404

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new_comment_form'] = NewCommentForm()
        context['new_reply_formset'] = NewReplyFormSet(queryset=Reply.objects.none())
        return context


class DiscussionBoardDetailView(View):

    def get(self, request, *args, **kwargs):
        view = PostDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        view = NewCommentFormView.as_view()
        if "reply_to" in request.POST:
            view = NewReplyFormView.as_view()
        return view(request, *args, **kwargs)


class NewCommentFormView(SingleObjectMixin, FormView):
    template_name = 'detail.html'
    form_class = NewCommentForm
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["new_comment_form"] = self.get_form()
        context['new_reply_formset'] = NewReplyFormSet(queryset=Reply.objects.none())
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = Author.objects.get(user=self.request.user)
        form.instance.datePosted = datetime.now()
        form.instance.original_post = self.get_object()
        form.instance.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('detail', kwargs={'slug': self.object.slug})


class NewReplyFormView(SingleObjectMixin, FormView):
    template_name = 'detail.html'
    form_class = NewReplyFormSet
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new_reply_formset'] = self.get_form()
        context["new_comment_form"] = NewCommentForm
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        instances = form.save(commit=False)
        for instance in instances:
            instance.user = Author.objects.get(user=self.request.user)
            instance.datePosted = datetime.now()
            instance.reply_to = Comment.objects.get(id=form.data["reply_to"])
            instance.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse('detail', kwargs={'slug': self.object.slug})


class DiscussionBoardPostsView(ListView):
    model = Post
    paginate_by = 8

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Post.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        return context


class NewPostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = NewPostForm

    def form_valid(self, form):
        model_instance = form.save(commit=False)
        model_instance.user = Author.objects.get(user=self.request.user)
        model_instance.datePosted = datetime.now()
        model_instance.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('new-post-success')


class NewPostSuccessView(TemplateView):
    template_name = "new-post-success.html"

