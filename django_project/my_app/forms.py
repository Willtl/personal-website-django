# A class that represents the form in a HTML file
from django import forms


class CommentForm(forms.Form):
    atrb_name = forms.CharField(max_length=30,
                                widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Name' }))
    atrb_email = forms.EmailField(max_length=30,
                                widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Email' }))
    atrb_comment = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control', 'placeholder' : 'Comment', 'style' : 'resize: none;' }))

    
class TemporaryUserForm(forms.Form):
    atrb_username = forms.CharField(max_length=30,
                                widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Username' }))
    atrb_email = forms.EmailField(max_length=30,
                                widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Email' }))
    atrb_password = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control', 'placeholder' : 'Password' }))
    
