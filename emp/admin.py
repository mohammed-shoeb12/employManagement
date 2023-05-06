from django.contrib import admin
from .models import model_employee
# Register your models here.
class AdminModel(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','dept','salary','bonus','role','hire_date','location','phone']

admin.site.register(model_employee,AdminModel)
