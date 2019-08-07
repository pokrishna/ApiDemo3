from django.contrib import admin
from myapp.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','rollno','marks','gf','bf']
