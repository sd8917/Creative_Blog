from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect,HttpResponse

from .models import Blog

# Create your views here.
def BlogView(request):
    posts = Blog.objects.all()

    return render(request, 'blog/index.html',{'post': posts})


def BlogDetail(request, slug):
    posts = get_object_or_404(Blog, Slug=slug)

    return render(request, 'blog/blogdetail.html',{'blog':posts})