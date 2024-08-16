from django.urls import path
from . import views
urlpatterns=[
    path('index/',views.index),
    path('',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('signin/',views.signin),
    path('signup/',views.signup),
    path('medicine/',views.mymedicine),
    path('imagegallery/',views.igallery),
    path('videogallery/',views.vgallery),
    path('viewdetails/',views.viewdetails),
    path('logout/',views.logout),
    path('payment/',views.payment),

]

