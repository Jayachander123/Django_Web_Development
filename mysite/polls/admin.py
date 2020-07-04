from django.contrib import admin
from .models import Choice, Question, Review

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Review)


# Register your models here.
