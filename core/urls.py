from django.urls import path
from core.views import index, blog, contact_us,cart,checkout,singleproduct,category,singleblog,tracking,elements,export_excel,all_search
from django.urls import include
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
    path('', include('social_django.urls', namespace='social')),
    path('export_excel/',export_excel,name='export_excel'),
    path('all-search/',all_search,name='all-search'),

    #  path('login/',login,name='login'),
    #  path('register/',register,name='register'),
   
    
    



]




