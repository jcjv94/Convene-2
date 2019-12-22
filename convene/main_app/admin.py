from django.contrib import admin
from .models import Event, Photo, Comment

# Register your models here.
admin.site.register(Event)
admin.site.register(Photo)
admin.site.register(Comment)