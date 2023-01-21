from django.shortcuts import render, get_object_or_404
from .models import Blog, Analytics, Comment, Contact
from django.core.paginator import Paginator
from gallery.models import Photo, VideoUpload
from django.contrib import messages


def index(request):
    if request.method == "GET":
        all_blog = Blog.objects.all().order_by('-created')
        paginated_number = 5
        paginator = Paginator(all_blog, paginated_number)
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
            'page_obj': page_obj,
        }
        return render(request, 'index.html', context)
    else:
        messages.error(request, "Something went wrong please try again")


def blogdetail(request, slug):
    if request.method == "GET":
        blog = get_object_or_404(Blog, slug=slug)
        x_forw_for = request.META.get('HTTP_X_FORWARDED_F0R')
        if x_forw_for is not None:
            ip = x_forw_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
            analytics = Analytics(ip=ip)
            analytics.save()
        context = {
            "blog": blog,
        }
        return render(request, 'single-post.html', context)
    elif request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        comment = request.POST["message"]
        if len(name) < 5 and len(email) < 3 and len(comment) < 10:
            messages.error(request, "Please enter atleast 5 character name, full valid email and atleast 10 character comment ")
        else:
            comment = Comment(name=name, email=email, comment=comment)
            comment.save()
            messages.success(request, "data saved successfully")
        return render(request, "single-post.html")
    else:
        messages.error(request, "Something went wrong please try again")


def galleryview(request):
    if request.method == "GET":
        all_images = Photo.objects.all().order_by('-created')
        paginated_gallery_number = 10
        gallery_paginator = Paginator(all_images, paginated_gallery_number)
        x_forw_for = request.META.get('HTTP_X_FORWARDED_F0R')
        if x_forw_for is not None:
            ip = x_forw_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
            analytics = Analytics(ip=ip)
            analytics.save()
        page_number = request.GET.get('page')
        page_obj = gallery_paginator.get_page(page_number)
        context = {
            'page_obj': page_obj
        }
        return render(request, 'gallery.html', context)
    else:
        messages.error(request, "Something went wrong please try again")


def contactview(request):
    if request.method == "GET":
        x_forw_for = request.META.get('HTTP_X_FORWARDED_F0R')
        if x_forw_for is not None:
            ip = x_forw_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
            analytics = Analytics(ip=ip)
            analytics.save()
        return render(request, 'contact.html')
    elif request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        if len(name) < 5 or len(email) < 5 and len(subject) < 5 or len(message) < 5:
            messages.error(
                request,
                "Your form contains error please give a name , email , subject , message at least 5 character and try again")
        else:
            contact = Contact(name=name, email=email, subject=subject, message=message)
            contact.save()
            messages.success(request, "The data you have provided has been saved successfully")
        return render(request, "contact.html")
    else:
        messages.error(request, "Something went wrong please try again")


def aboutview(request):
    if request.method == "GET":
        return render(request, "about.html")
    else:
        messages.error(request, "Something went wrong please try again")


def watch_all(request):
    if request.method == "GET":
        all_videos = VideoUpload.objects.all().order_by('-created')
        x_forw_for = request.META.get('HTTP_X_FORWARDED_F0R')
        if x_forw_for is not None:
            ip = x_forw_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
            analytics = Analytics(ip=ip)
            analytics.save()
        context = {
            "videos": all_videos
        }
        return render(request, "allvideos.html", context)


def watchview(request, slug):
    if request.method == "GET":
        video = get_object_or_404(VideoUpload, slug=slug)
        x_forw_for = request.META.get('HTTP_X_FORWARDED_F0R')
        if x_forw_for is not None:
            ip = x_forw_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
            analytics = Analytics(ip=ip)
            analytics.save()
        context = {
            "video": video
        }
    return render(request, 'watch.html')
