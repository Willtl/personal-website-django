from django.contrib import admin
from .models import Comment
from .models import TemporaryUser
from .models import User

admin.site.register(Comment)
admin.site.register(TemporaryUser)
admin.site.register(User)
