from django.contrib import admin
from .models import Task, Department, Importance
# Register your models here.

admin.site.register(Task)
admin.site.register(Department)
admin.site.register(Importance)