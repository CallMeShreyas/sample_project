from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Course)
admin.site.register(Test)
admin.site.register(Question)
# admin.site.register(Option)
# admin.site.register(CorrectOption)
admin.site.register(Answer)

