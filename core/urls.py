from django.urls import path
from core.views import index, blog, contact_us,cart,checkout,singleproduct,category,singleblog,tracking,elements

urlpatterns = [
    
    path('',index,name='index'),
    path('blog/',blog,name='blog'),
    # path('singleblog/<int:blog_id>/',singleblog,name='single-blog'),
    path('singleblog/<str:blog_slug>/',singleblog,name='single-blog'),
    path('contact-us/',contact_us,name='contact_us'),
    path('cart/',cart,name='cart'),
    path('checkout/',checkout,name='checkout'),
    path('singleproduct/',singleproduct,name='singleproduct'),
    path('category/',category,name='category'),
    path('tracking/',tracking,name='tracking'),
    path('elements/',elements,name='elements'),
   
    
    



]