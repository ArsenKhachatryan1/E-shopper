from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from . models import HeaderInfo, HomeSlider, Category, SubCategory, Items, ContactUs, Curency, Cart


class HeaderInfoAdmin(TranslationAdmin):
    pass

class HomeSliderAdmin(TranslationAdmin):
    pass

class CategoryAdmin(TranslationAdmin):
    pass

class SubCategoryAdmin(TranslationAdmin):
    pass




admin.site.register(HeaderInfo)
admin.site.register(HomeSlider)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Items)
admin.site.register(ContactUs)
admin.site.register(Curency)
admin.site.register(Cart)
