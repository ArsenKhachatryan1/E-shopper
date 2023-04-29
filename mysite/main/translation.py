from .models import HeaderInfo, HomeSlider, Category, SubCategory, Items
from modeltranslation.translator import register, TranslationOptions

@register(HeaderInfo)
class HeaderInfoTranslationOptions(TranslationOptions):
    fields = ('name', 'country1', 'country2', 'country1', 'account', 'wishlist', 'checkout', 'cart', 'login',
              'logout', 'signup')


@register(HomeSlider) 
class HomeSliderTranslationOptions(TranslationOptions):
    fields = ('name1', 'name2', 'text', 'button_name')


@register(Category) 
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(SubCategory) 
class SubCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Items) 
class ItemsTranslationOptions(TranslationOptions):
    fields = ('name',)