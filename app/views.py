from urllib import request
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView,DetailView
from .models import Blog,Analytics
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views import generic
from django.core.paginator import Paginator
from django.http import Http404
from gallery.models import FileUpload,FileDetail,Photo,PhotoDetails
 
def index(request):
    all_blog = Blog.objects.all().order_by('-created')
    paginator = Paginator(all_blog,5)
    x_forw_for = request.META.get('HTTP_X_FORWARDED_F0R')
    if x_forw_for is not None:
        ip = x_forw_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
        analytics = Analytics(ip=ip)
        analytics.save()
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj':page_obj
    }
    return render(request,'index.html',context)

class BlogDetailView(DetailView):
    model=Blog
    template_name='single-post.html'

class GalleryView(ListView):
    model = Photo
    template_name="gallery.html"
    ordering = ['-created']
    paginate_by = 20
    paginate_orphans=1
    def paginate_queryset(self,queryset,page_size):
        try:
            return super(GalleryView,self).paginate_queryset(queryset,page_size)
        except Http404:
            self.kwargs['page']=1
            return super(GalleryView,self).paginate_queryset(queryset,page_size)
