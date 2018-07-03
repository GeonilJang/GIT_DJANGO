from django.shortcuts import render, get_object_or_404
from .models import Product
# from .forms import ProductsForm
# Create your views here.
qs = Product.objects.all()
def products_list(request):
    return render(request, "products/product_list.html",{
        "products":qs
    })


def products_detail(request, id):
    post= get_object_or_404(Product, id=id)
    return render(request, "products/product_detail.html",{
        "post": post
    })

#
# def products_new(request):
#     if request.method =="POST":
#         form = ProductsForm(request.POST, request.FIELS)
#
