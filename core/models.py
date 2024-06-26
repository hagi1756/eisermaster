from django.db import models
from django.utils.translation import gettext as _
# Create your models here.


SIZE = (

('XS','Extra Small'),
('S','Small'),
('M','Medium'),
('L','Large'),
('EL','Extra large'),
('XXL','Extra Extra large'),
('XXXL','Extra Extra Extra large'),

)


class Basemodel(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    is_active = models.BooleanField(default = True)

    class Meta:
        abstract = True


class Category(Basemodel):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name=_('Catagory')
        verbose_name_plural=_('Catagories')
    

    def __str__(self) -> str:
        return f"{self.name}, {self.created_at}"



class Product(Basemodel):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=50,choices=SIZE,default='M')
    like = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/products/')
    description = models.TextField()

    class Meta:
        verbose_name=_('Product')
        verbose_name_plural=_('Products')

    def __str__(self) -> str:
         return f"{self.name}, {self.created_at}"


class Blog(Basemodel):
    slug = models.SlugField(max_length=100,null=True,blank=True,unique = True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='media/blog/')

    

    class Meta:
        verbose_name=_('Blog')
        verbose_name_plural=_('Blogs')
        ordering = ('created_at',)

    def __str__(self):
         return self.title
    
    def save(self, *args, **kwargs):
        from core.utils.replace_letter import replace_letter

        if not self.slug:
            self.slug = replace_letter(self.title.lower())

        return super().save(*args, **kwargs)

    


    
    

class ContactUs(Basemodel):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    phone_note = models.CharField(max_length=100)
    email = models.EmailField()
    email_note = models.CharField(max_length=100)


    class Meta:
        verbose_name=_('Contact Us')
        verbose_name_plural=_('Contact Us')
       

    def __str__(self):
         return self.name
    


class Setting(Basemodel):
    name = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    dribbble = models.URLField(null=True, blank=True)
    behance = models.URLField(null=True, blank=True) 
    logo = models.ImageField(upload_to='media/blog/')
    blog_bg_image = models.ImageField(upload_to='media/blog/')
    blog_title = models.CharField(max_length=100, null=True, blank=True)
    contact_title = models.CharField(max_length=100, null=True, blank=True)

    
    class Meta:
        verbose_name=_('Setting')
        verbose_name_plural=_('Setting')
       

    
    

class Contact(Basemodel):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=100)
    
    
    class Meta:
        verbose_name=_('Contact')
        verbose_name_plural=_('Contacts')
       

    def __str__(self):
         return self.name


class Subscriber(Basemodel):
    email = models.EmailField()
    def __str__(self):
        return self.email
    
    