from django.shortcuts import redirect, render
from core.models import Blog,ContactUs,Setting,Category,Product
from core.forms import ContactForm
from django.views.generic import ListView
from excel_response import ExcelResponse


# Create your views here.
def index(request):
    context = {
        'blog':Blog.objects.filter(is_active='True').order_by('created_at',)
    }
    return render(request,'index.html',context=context)


def shop (request):
    context = {
        'products':Product.objects.filter(is_active='True'),
        'title':'Shop',
    }
    return render(request,'shop.html',context=context)

# class shopView(ListView):
#     model = Product
#     template_name ='shop.html'
#     context_object_name = 'products'
#     queryset = Product.objects.filter(is_active='True')
#     paginate_by = 10
#     ordering = ['-created_at']
#     page_kwarg = 'p'
#     extra_context = {
#         'title':'Shop',
#     }

def blog(request):
    from django.db.models import Q
    blogs = Blog.objects.filter(is_active='True').order_by('created_at',)
    start_date = None
    end_date = None
    if request .method == 'POST':
        print('request.POST:',request.POST)
        user_input = request.POST.get('blog_search')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        category = request.POST.get('category')

        # if category:
        #     blogs = blogs.filter(category__id=category)
        if user_input:
            blogs = blogs.filter(title__icontains=user_input)
        if start_date and end_date:
            blogs = blogs.filter(
                 Q(created_at__gte=start_date)&
                 Q(created_at__lte=end_date))
                                 
        
        
        
    context = {
             'title':Setting.objects.get(id=3).blog_title,
             'blogs':blogs,
             'blog_count':blogs.count(),
             'categories':Category.objects.filter(is_active=True),
            #  'no_results':'Blog tapilmadi' if blogs.count()==0 else None,
            'start_date':start_date,
            'end_date':end_date,
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


def export_excel(request):
    blogs = Blog.objects.values('title','description','created_at',)
    response = ExcelResponse(blogs, output_filename= 'blogs.xls')
    response['Content-Disposition'] = 'attachment; filename="blogs.xls"'
    return response



def all_search(request):
    # blogs = Blog()
    # products = Product()
    
    if request.method == 'POST':
        user_input = request.POST.get('all_search')
        print('user_input:',user_input)
        blogs = Blog.objects.filter(title__icontains=user_input)
        products = Product.objects.filter(name__icontains=user_input)

        context = {
            'title':' Search',
            'blogs':blogs,
            'products':products,
        }
        return render(request,'search.html',context=context)
    return render(request,'search.html') 