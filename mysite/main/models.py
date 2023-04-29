from django.db import models

# Create your models here.




class HeaderInfo(models.Model):

    name = models.CharField('Site name', max_length=50)
    phone = models.CharField('Phone number', max_length=50)
    email = models.URLField('Email adress', null=True)
    img = models.ImageField('Logo', upload_to='images')
    facebook = models.URLField('Facebook link', blank=True)
    twitter = models.URLField('Twitter link', blank=True)
    linkedin = models.URLField('Linkedin link', blank=True)
    dribbble = models.URLField('Dribbble link', blank=True)
    google_plus = models.URLField('Google-plus link', blank=True)
    country1 = models.CharField('Country 1', max_length=50, blank=True)
    country2 = models.CharField('Country 2', max_length=50, blank=True)
    country3 = models.CharField('Country 3', max_length=50, blank=True)
    curency1 = models.CharField('CUrency 1', max_length=50, blank=True)
    curency2 = models.CharField('CUrency 2', max_length=50, blank=True)
    curency3 = models.CharField('CUrency 3', max_length=50, blank=True)
    account = models.CharField('accaunt', max_length=50)
    wishlist = models.CharField('wishlist', max_length=50)
    checkout = models.CharField('checkout', max_length=50)
    cart = models.CharField('cart', max_length=50)
    login = models.CharField('login', max_length=50)
    logout = models.CharField('logout', max_length=50)
    signup = models.CharField('signup', max_length=50)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'HeaderInfo'
        verbose_name_plural = 'HeaderInfo'




class HomeSlider(models.Model):

    name1 = models.CharField('Slider name1', max_length=30)
    name2 = models.CharField('Slider name2', max_length=30)
    text = models.TextField('Slider text')
    button_name = models.CharField('Slider button name', max_length=20)
    img = models.ImageField('Slider image1', upload_to='media')
    img_logo = models.ImageField('Slider image2', upload_to='media')

    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'HomeSlider'
        verbose_name_plural = 'HomeSlider'



class Category(models.Model):
    
    name = models.CharField('Category name', max_length=60)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class SubCategory(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    name = models.CharField('SubCategory name', max_length=60)
    price = models.PositiveIntegerField('SubCategory price', default=0)
    img = models.ImageField('SubCategory image', upload_to='images', blank=True)

    def __str__(self):
        return f'{self.name} - {self.category.name}'
    
    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'


class Items(models.Model):

    name = models.CharField('Item name', max_length=60)
    price = models.PositiveIntegerField('Item price', default=0)
    img = models.ImageField('Item image', upload_to='images', blank=True)
    img_logo = models.ImageField('Item sale image', upload_to='images', blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Items'
        verbose_name_plural = 'Items'


class ContactUs(models.Model):

    name = models.CharField('User name', max_length=50)
    email = models.EmailField('User email')
    subject = models.CharField('User name', max_length=50)
    message = models.TextField('User message')

    class Meta:
        verbose_name = 'ContactUs'
        verbose_name_plural = 'ContactUs'

    def __str__(self) -> str:
        return self.name
    

class Curency(models.Model):
    name = models.CharField('Curency name', default='usd', max_length=20)
    kurs_amd = models.PositiveIntegerField('AMD kurs')

    class Meta:
        verbose_name = 'Curency'
        verbose_name_plural = 'Curency'

    def __str__(self) -> str:
        return self.name
