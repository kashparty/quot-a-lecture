from operator import mod
from django.contrib import admin

# Register your models here.

from .models import Category, Lecturer, QuestionAnswer, Recording

admin.site.register(QuestionAnswer)
admin.site.register(Recording)
admin.site.register(Lecturer)
admin.site.register(Category)
