from django.shortcuts import render
from .models import Comment
from .forms import CommentForm
from django.http.response import HttpResponse 
from django.urls.base import resolve


def index (request):
    return render(request, 'webcontext/index.html')


def comment (request):
    # Get the url name used to call this view
    current_url = resolve(request.path_info).url_name;
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

    #comments = Comment.objects.order_by('-date_added') 
    comments = Comment.objects.filter(url_name = current_url).order_by('-date_added')
    print('The URL name: ' + current_url);
    context = {'comments' : comments, 'form' : form}
    return render(request, 'webcontext/comment.html', context)   

def code (request):
    # Get the url name used to call this view
    current_url = resolve(request.path_info).url_name;
    if request.method == 'POST':  
        new_comment = Comment(name=request.POST['atrb_name'], email=request.POST['atrb_email'], comment=request.POST['atrb_comment'], url_name=current_url)
        new_comment.save()
        return HttpResponse('')
    else:
        form = CommentForm()

    #comments = Comment.objects.order_by('-date_added') 
    comments = Comment.objects.filter(url_name = current_url).order_by('-date_added')
    print('The URL name: ' + current_url);
    context = {'comments' : comments, 'form' : form}
    return render(request, 'webcontext/code.html', context)   
