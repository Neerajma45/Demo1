from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.demo,name='demo'),
    path('add/',views.addition,name='add')

    # path('contact/', views.contact, name='contact'),
    # path('detail/', views.detail, name='detail'),
    # path('thanks/', views.thanks, name='thanks'),

]