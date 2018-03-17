from .models import Comment
from .forms import CommentForm
from django.http.response import HttpResponse 
from django.urls.base import resolve
from django.shortcuts import render


def index (request):
    current_url = 'home';
    current_path = 'home'; 
    context = {'page_name' : current_url, 'current_path' : current_path}
    return render(request, 'webcontext/index.html', context)


def publications (request): 
    current_url = resolve(request.path_info).url_name;
    current_path = request.get_full_path();
    if request.method == 'POST':  
        new_comment = Comment(name=request.POST['atrb_name'], email=request.POST['atrb_email'], comment=request.POST['atrb_comment'], url_name=current_url)
        new_comment.save()
        return HttpResponse('')
    else:
        form = CommentForm()
 
    comments = Comment.objects.filter(url_name=current_url).order_by('-date_added')
    print('The URL name: ' + current_url);
    context = {'comments' : comments, 'form' : form, 'page_name' : current_url, 'current_path' : current_path}
    return render(request, 'webcontext/publications.html', context)   


def research (request): 
    current_url = resolve(request.path_info).url_name;
    current_path = request.get_full_path();
    if request.method == 'POST':  
        new_comment = Comment(name=request.POST['atrb_name'], email=request.POST['atrb_email'], comment=request.POST['atrb_comment'], url_name=current_url)
        new_comment.save()
        return HttpResponse('')
    else:
        form = CommentForm()

    # comments = Comment.objects.order_by('-date_added') 
    comments = Comment.objects.filter(url_name=current_url).order_by('-date_added')
    print('The URL name: ' + current_url);
    context = {'comments' : comments, 'form' : form, 'page_name' : current_url, 'current_path' : current_path}
    return render(request, 'webcontext/research.html', context)   


def contact (request): 
    current_url = resolve(request.path_info).url_name;
    current_path = request.get_full_path();
    if request.method == 'POST':  
        # form = CommentForm(request.POST)
        # if form.is_valid():
        #    new_comment = Comment(name=request.POST['atrb_name'],  email=request.POST['atrb_email'], comment=request.POST['atrb_comment'])
        #    new_comment.save()
        #    return redirect('comment') 
        new_comment = Comment(name=request.POST['atrb_name'], email=request.POST['atrb_email'], comment=request.POST['atrb_comment'], url_name=current_url)
        new_comment.save()
        return HttpResponse('')
    else:
        form = CommentForm()

    # comments = Comment.objects.order_by('-date_added') 
    comments = Comment.objects.filter(url_name=current_url).order_by('-date_added')
    print('The URL name: ' + current_url);
    context = {'comments' : comments, 'form' : form, 'page_name' : current_url, 'current_path' : current_path}
    return render(request, 'webcontext/contact.html', context)   


def code (request): 
    current_url = resolve(request.path_info).url_name;
    current_path = request.get_full_path();
    if request.method == 'POST':  
        new_comment = Comment(name=request.POST['atrb_name'], email=request.POST['atrb_email'], comment=request.POST['atrb_comment'], url_name=current_url)
        new_comment.save()
        return HttpResponse('')
    else:
        form = CommentForm()
 
    comments = Comment.objects.filter(url_name=current_url).order_by('-date_added')
    print('The URL name: ' + current_url);
    context = {'comments' : comments, 'form' : form, 'page_name' : current_url, 'current_path' : current_path}
    return render(request, 'webcontext/code.html', context)   
