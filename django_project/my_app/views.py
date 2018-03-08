from django.shortcuts import render, redirect
from .models import Comment
from .forms import CommentForm
from django.http.response import HttpResponse


def index (request):
    return render(request, 'webcontext/index.html')


def simple (request):
    if request.method == 'POST':  
        # form = CommentForm(request.POST)
        # if form.is_valid():
        #    new_comment = Comment(name=request.POST['atrb_name'],  email=request.POST['atrb_email'], comment=request.POST['atrb_comment'])
        #    new_comment.save()
        #    return redirect('simple')
        new_comment = Comment(name=request.POST['atrb_name'], email=request.POST['atrb_email'], comment=request.POST['atrb_comment'])
        new_comment.save()
        return HttpResponse('')
    else:
        form = CommentForm()

    comments = Comment.objects.order_by('-date_added')    
    context = {'comments' : comments, 'form' : form}
    return render(request, 'webcontext/simple.html', context)  
