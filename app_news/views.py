from django.shortcuts import render
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# Create your views here.

from .models import Category,News


class NewsCreateView(LoginRequiredMixin,CreateView):
    model = News
    template_name = 'news/add_news.html'
    success_url = '/'
    fields = ['news_title', 'news_description', 'news_image', 'news_content', 'news_category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class ListNewView(ListView):
    model = News
    template_name = 'news/list_news.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        return {'categories': Category.objects.all(), 'news_list': self.get_queryset()}

    def get_queryset(self):
        if 'keyword' in self.request.GET:
            return (
                News.objects.filter(news_title__icontains=self.request.GET['keyword']) |
                News.objects.filter(news_description__icontains=self.request.GET['keyword']) |
                News.objects.filter(news_content__icontains=self.request.GET['keyword'])
            )
        return News.objects.all()


class DetailNewView(DetailView):
    model = News
    template_name = 'news/show_news.html'


class EditNewView(UpdateView):
    model = News
    template_name = 'news/edit_news.html'
    fields = ['news_title', 'news_description', 'news_image', 'news_content', 'news_category']
    success_url = reverse_lazy('list-news')


class DeleteNewView(DeleteView):
    model = News
    template_name = 'news/delete_news.html'

    def get_success_url(self):
        return reverse_lazy('list-news')



