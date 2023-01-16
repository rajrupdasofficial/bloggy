from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView,DetailView,TemplateView,UpdateView,CreateView,DeleteView,RedirectView
from .models import Blog
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views import generic
from django.core.paginator import Paginator
from django.http import Http404

class IndexView(ListView):
    model = Blog
    template_name="index.html"
    slug_field = 'slug'
    ordering = ['-created']
    paginate_by=5
    paginate_orphans=1
    def paginate_queryset(self,queryset,page_size):
        try:
            return super(IndexView,self).paginate_queryset(queryset,page_size)
        except Http404:
            self.kwargs['page']=1
            return super(IndexView,self).paginate_queryset(queryset,page_size)

class BlogDetailView(DetailView):
    model=Blog
    template_name='single-post.html'
