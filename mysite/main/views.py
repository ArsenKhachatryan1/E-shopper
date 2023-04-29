from django.shortcuts import render, redirect
from .models import HeaderInfo, HomeSlider, Category, SubCategory, Items, ContactUs, Curency

from .forms import NewUserForm, ContactForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.



def index(request):
    
    if request.method == 'POST':
        cur = Curency.objects.all()[0]
        amd = Curency.objects.all()[0].kurs_amd
        x = Items.objects.all()
        
        if cur.name == 'usd':
            for i in range(0, len(x)):
                x[i].price = x[i].price * amd
                x[i].save()
            cur.name = 'amd'
            cur.save()
        elif cur.name == 'amd':
            for i in range(0, len(x)):
                x[i].price = x[i].price / amd
                x[i].save()
            cur.name = 'usd'
            cur.save()
    cur = Curency.objects.all()[0]       
    headerinfo = HeaderInfo.objects.all()[0]
    homeslideractive = HomeSlider.objects.all()[0]
    homeslider = HomeSlider.objects.all()[1:]
    category_list = Category.objects.all()
    sub_categry_list = SubCategory.objects.all()
    items = Items.objects.all()
    return render(request, 'main/index.html', context={
	   'headerinfo':headerinfo,
	   'act':'index',
	   'homeslideractive':homeslideractive,
	   'homeslider':homeslider,
	   'category_list':category_list,
	   'sub_categry_list':sub_categry_list,
	   'items':items,
        'cur':cur
    })



def index_detail(request):
    
    headerinfo = HeaderInfo.objects.all()[0]
    homeslideractive = HomeSlider.objects.all()[0]
    homeslider = HomeSlider.objects.all()[1:]
    category_list = Category.objects.all()
    sub_categry_list = SubCategory.objects.all()
    category_filter = Category.objects.filter(pk=id)
    return render(request, 'main/index.html', context={
	   'headerinfo':headerinfo,
	   'act':'index',
	   'homeslideractive':homeslideractive,
	   'homeslider':homeslider,
	   'category_list':category_list,
	   'sub_categry_list':sub_categry_list,
    	'category_filter':category_filter,
    })

def pagenotfound(request):

    return render(request,'main/404.html')


def blog_single(request):
    headerinfo = HeaderInfo.objects.all()[0]

    return render(request,'main/blog-single.html', context={
	   'headerinfo':headerinfo,
	   'act':'blog_single'
	   
    })


def blog(request):
    headerinfo = HeaderInfo.objects.all()[0]

    return render(request,'main/blog.html', context={
	   'headerinfo':headerinfo,
	   'act':'blog'
	   
    })


def cart(request):
    headerinfo = HeaderInfo.objects.all()[0]

    return render(request,'main/cart.html', context={
	   'headerinfo':headerinfo,
	   'act':'cart'
    })


def checkout(request):
    headerinfo = HeaderInfo.objects.all()[0]

    return render(request,'main/checkout.html', context={
	   'headerinfo':headerinfo,
	   'act':'checkout'
    })


def contact_us(request):
    headerinfo = HeaderInfo.objects.all()[0]
    contactus = ContactUs.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactUs.objects.create(**form.cleaned_data)
            return redirect('contact-us')
    else:
        form = ContactForm()
    return render(request,'main/contact-us.html', context={
	   'headerinfo':headerinfo,
	   'act':'contact_us',
        'contactus':contactus
    })



def product_details(request):
    headerinfo = HeaderInfo.objects.all()[0]

    return render(request,'main/product-details.html', context={
	   'headerinfo':headerinfo,
	   'act':'product_details'
    })


def shop(request):
    headerinfo = HeaderInfo.objects.all()[0]

    return render(request,'main/shop.html', context={
	   'headerinfo':headerinfo,
	   'act':'shop'
    })




def register_request(request):
	headerinfo = HeaderInfo.objects.all()[0]
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request=request, template_name="main/register.html", context={
		"register_form":form,
		'headerinfo':headerinfo,
		'act':'register_request'
	})

def login_request(request):
	headerinfo = HeaderInfo.objects.all()[0]
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={
		"login_form":form,
	    'headerinfo':headerinfo,
	    'act':'login_request'
        })

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index")