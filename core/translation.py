from modeltranslation.translator import translator, TranslationOptions


from core.models import (
    Contact,
    ContactUs,
    Setting,
    Product,
    Category,
    Blog,
)



class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

class ProductTranslationOptions(TranslationOptions):
    fields = ('name',)


class ContactUsTranslationOptions(TranslationOptions):
    fields = ('name','email','address',)

class ContactTranslationOptions(TranslationOptions):
    fields = ('name','email','message','subject')

class SettingTranslationOptions(TranslationOptions):
    fields = ('name','address','email',)
class BlogTranslationOptions(TranslationOptions):
    fields = ('title','description',)



translator.register(Category,CategoryTranslationOptions)
translator.register(ContactUs,ContactUsTranslationOptions)
translator.register(Product,ProductTranslationOptions)
translator.register(Contact,ContactTranslationOptions)
translator.register(Setting,SettingTranslationOptions)
translator.register(Blog,BlogTranslationOptions)