from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# Create your views here.
from ecommerceapp.models import Category, Product


def allProdCat(request,c_slug=None):
    c_page=None
    product_list=None
    if c_slug != None:
        c_page=get_object_or_404(Category,slug=c_slug)
        product_list=Product.objects.all().filter(category=c_page,availability=True)
    else:
        product_list=Product.objects.all().filter(availability=True)
    p=Paginator(product_list,6)
    try:
        pg=int(request.GET.get('page','1'))
    except:
        pg=1
    try:
        product=p.page(pg)
    except (EmptyPage,InvalidPage):
        product=p.page(p.num_pages)
    return render(request,"category.html",{'category':c_page,'product':product})

def proDetails(request,c_slug,product_slug):
    try:
        product=Product.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,"product.html",{'product':product})
