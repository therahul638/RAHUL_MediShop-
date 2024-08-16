from django.contrib import admin
from .models import *

# Register your models here.
class contactusAdmin(admin.ModelAdmin):
    list_display =('Name','Email','Mobile','Message')
admin.site.register(contactus,contactusAdmin)

class categoryAdmin(admin.ModelAdmin):
    list_display = ('id','cname','cpic','cdate')

admin.site.register(category,categoryAdmin)

class sliderAdmin(admin.ModelAdmin):
    list_display =('id','spic','sdate')

admin.site.register(slider,sliderAdmin)

class cityAdmin(admin.ModelAdmin):
    list_display = ('id','city_name','city_picture')

admin.site.register(city,cityAdmin)

class placenameAdmin(admin.ModelAdmin):
    list_display = ('id','place','address','ppic','pdate')

admin.site.register(placename,placenameAdmin)

class medicineAdmin(admin.ModelAdmin):
    list_display = ('id','medicine_category','medicine_name','shop','city','medicine_picture','medicine_picture','price','dprice','medicine_date')

admin.site.register(medicine,medicineAdmin)

class imagegalleryAdmin(admin.ModelAdmin):
    list_display = ('id','category','picture','medicinedate','medicine_des')

admin.site.register(imagegallery,imagegalleryAdmin)

class videogalleryAdmin(admin.ModelAdmin):
    list_display = ('id','category','vlink','vdate','medicine_des')

admin.site.register(videogallery,videogalleryAdmin)

class registerAdmin(admin.ModelAdmin):
    list_display=('email','uname','passwd','upic','address')

admin.site.register(register,registerAdmin)
