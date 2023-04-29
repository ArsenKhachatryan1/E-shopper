from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('404/',views.pagenotfound, name = '404'),
    path('blog-single/',views.blog_single, name = 'blog_single'),
    path('blog/',views.blog, name = 'blog'),
    path('cart/',views.cart, name = 'cart'),
    path('checkout/',views.checkout, name = 'checkout'),
    path('contact-us/',views.contact_us,name = 'contact-us'),
    path('product-details/',views.product_details, name = 'product-details'),
    path('shop',views.shop, name = 'shop'),
    path('login/', views.login_request, name='login'),
    path('register/', views.register_request, name='register'),
    path('logout/', views.logout_request, name='logout'),
]