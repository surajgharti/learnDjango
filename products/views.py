from django.shortcuts import render, Http404
from .models import Product
from .forms import ProductForm, RawProductForm


def dynamic_product_view(request, my_id):
    try:
        obj = Product.objects.get(id=my_id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        "object": obj
    }
    return render(request, "product/dynamic_product_detail.html", context)

def product_create_view(request):
    form = ProductForm(request.POST)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "product/product_create.html", context)

# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'title': obj.title,
        'description': obj.description
    }
    return render(request, "product/detail.html", context)