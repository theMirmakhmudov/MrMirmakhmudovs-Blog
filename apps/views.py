from django.views.generic import ListView
from .models import LatestBlogPost, Tags


class HomeView(ListView):
    template_name = 'index.html'
    model = LatestBlogPost

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Post"] = LatestBlogPost.objects.all()
        context["Tags"] = Tags.objects.all()
        return context
