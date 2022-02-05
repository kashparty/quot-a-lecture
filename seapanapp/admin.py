from operator import mod
from django.contrib import admin

# Register your models here.

from .models import QuestionAnswer, Recording

admin.site.register(QuestionAnswer)
admin.site.register(Recording)
