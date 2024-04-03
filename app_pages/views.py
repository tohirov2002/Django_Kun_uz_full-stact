from django.views.generic import TemplateView

# Create your views here.
from app_news.models import Category


class HomePageView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        return {'categories': Category.objects.all()}
