from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SixteenPlusPageView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class YoungerChildPageView(TemplateView):
    template_name = "5-8.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

