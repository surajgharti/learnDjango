from django.shortcuts import render
from .models import Product
from .forms import ProductForm

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