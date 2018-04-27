from .models import Comment
from .models import TemporaryUser

from .forms import CommentForm
from .forms import TemporaryUserForm

from django.http.response import HttpResponse 
from django.urls.base import resolve
from django.shortcuts import render 

from _sha256 import sha256
import uuid 


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
    context = {'page_name' : current_url, 'current_path' : current_path}
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


def registration (request): 
    current_url = resolve(request.path_info).url_name;
    current_path = request.get_full_path();
    if request.method == 'POST':  
        print('Storing user ', request.POST['atrb_username'], '.')
        hashed_password = hash_password(request.POST['atrb_password'])
        temp_user = TemporaryUser(username=request.POST['atrb_username'], email=request.POST['atrb_email'], password=hashed_password, activation_code=uuid.uuid4())
        temp_user.save()
        send_email(temp_user.username, temp_user.email, str(temp_user.activation_code))
        return HttpResponse('')
    else:
        form = TemporaryUserForm()

    print('The URL name: ' + current_url);
    context = {'form' : form, 'page_name' : current_url, 'current_path' : current_path}
    return render(request, 'webcontext/registration.html', context)   


def activate (request): 
    current_url = resolve(request.path_info).url_name;
    current_path = request.get_full_path();
    username = 'Null' 
    if request.method == 'GET':  
        parameter_code = request.GET.get('code','')
        print('the code parameter',parameter_code)
        
        user_object = TemporaryUser.objects.get(activation_code=parameter_code)
        username = user_object.username
        # get user name from parameter and load username from database
    
    context = {'username' : username, 'page_name' : current_url, 'current_path' : current_path}
    return render(request, 'webcontext/activate.html', context)   


def hash_password(password):
    hex_dig = sha256(password.encode('ascii')).hexdigest()
    return hex_dig
 
        
def send_email(username, recipient, activation_code):
    import smtplib
    
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    
    # sender == my email address 
    sender = 'wtl4ever@gmail.com' 
    pwd = '!Ww33423554'
    
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Activate your account"
    msg['From'] = sender
    msg['To'] = recipient
    
    # Create the body of the message (a plain-text and an HTML version).
    text = "Dear" + username + "\nYou are almost done!\nPlease click in the link to activate your account: http://localhost:8000/activate?code=" + activation_code
    html = """\
    <html>
      <head></head>
      <body>
        <p>You are almost done!<br>
           Click <a href="http://localhost:8000/activate?code=""" + activation_code + """\">here</a> or in the link below to activate your account.<br>
           http://localhost:8000/activate?code=""" + activation_code + """\
        </p>
      </body>
    </html>
    """
    
    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    
    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)
    # Send the message via local SMTP server.
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    
    mail.ehlo()
    
    mail.starttls()
    
    mail.login(sender, pwd)
    mail.sendmail(sender, recipient, msg.as_string())
    mail.quit()
