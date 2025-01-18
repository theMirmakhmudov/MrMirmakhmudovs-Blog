from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from .models import Posts, Tags


class HomeView(ListView):
    template_name = 'index.html'
    model = Posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Post"] = Posts.published.all()
        context["Tags"] = Tags.objects.all()
        return context
