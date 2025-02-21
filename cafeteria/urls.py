from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('',views.home) ,
   path('login/',views.user_login),
   path('register/',views.registration),
   path('detail/<cid>',views.viewdetail),
    path('logout/',views.user_logout),
    path('dessert/',views.dessert),
    path('place/',views.pinfo),
    path('new/',views.pinfo),
    path('club/',views.club),
    path('catfilter/<cid>',views.catfilter),
    path('catfilterd/<cid>',views.catfilterd),
    path('catfilterp/<cid>',views.catfilterp),
    path('catfilterb/<cid>',views.catfilterb),
    path('addtowish/<cid>',views.addTowish),
    path('viewwish/',views.viewwish),
    path('jain/<cid>',views.jinfo),
   path('reservation/',views.reservation),
   path('remove/',views.remove_res),
   path("senduseremail",views.sendusermail)
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

