from django.shortcuts import redirect, render
from core.models import Blog,ContactUs,Setting
from core.forms import ContactForm

# Create your views here.
def index(request):
    context = {
        'blog':Blog.objects.filter(is_active='True').order_by('created_at',)
    }
    return render(request,'index.html',context=context)

def blog(request):
    blogs = Blog.objects.filter(is_active='True').order_by('created_at',)
    context = {
             'title':Setting.objects.get(id=3).blog_title,
             'blogs':blogs,
             'blog_count':blogs.count()
               }
    return render(request,'blog.html',context=context)

def singleblog(request,blog_slug):
    blog = Blog.objects.get(slug=blog_slug)
    context = {
             'title':blog.title,
             'blog':blog
             }
    return render(request,'single-blog.html',context=context)



# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, 'contact.html', context={'contact_form': ContactForm()})
#     contacts = Contact.objects.filter(is_active=True).order_by('-created_at')
#     context = {
#         'contact_form': ContactForm(),
#         'title': 'Contact page',
#         'contact': contacts.first()
#     }
#     return render(request, 'contact.html',context=context)

def contact_us(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_us')


    context = {
        'contact_form':ContactForm(),
        'title':Setting.objects.get(id=3).contact_title,
        'contact_us': ContactUs.objects.all()
               }
    return render(request,'contact_us.html',context=context)

def cart(request):
    
    return render(request,'cart.html')

def checkout(request):
    return render(request,'checkout.html')

def singleproduct(request):
    return render(request,'single-product.html')

def category(request):
    return render(request,'category.html')



def tracking(request):
    return render(request,'tracking.html')

def elements(request):
    return render(request,'elements.html')


# def login(request):
#     return render(request,'login.html')


# def register(request):
#     return render(request,'register.html')