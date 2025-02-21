from django.contrib import admin
from .models import cafes,jain,sweet,bar,place,Wishlist,list,visitor

# Register your models here.
class CafesAdmin(admin.ModelAdmin):
    list_display=['id','name','detail','place','category','address','rating', 'contact','cusine']

class JainAdmin(admin.ModelAdmin):
    list_display=['id','name','detail','place','category','address','rating', 'contact','cusine']    

class sweetAdmin(admin.ModelAdmin):
    list_display=['id','name','detail','address','place','category','rating' ,'contact'] 

class barAdmin(admin.ModelAdmin):
    list_display=['id','name','detail','place','category','address','rating', 'contact']  

class placeAdmin(admin.ModelAdmin):
    list_display=['id','name','detail','place','category','address','rating', 'contact']  

# class wishAdmin(admin.ModelAdmin):
#     list_display=['uid','cid']                 
class vAdmin(admin.ModelAdmin):
    list_display=['name','contact','email','visitors']

admin.site.register(cafes,CafesAdmin)
admin.site.register(jain,JainAdmin)
admin.site.register(sweet,sweetAdmin)
admin.site.register(bar,barAdmin)
admin.site.register(place,placeAdmin)
admin.site.register(Wishlist)
admin.site.register(list)
admin.site.register(visitor,vAdmin)