from django.shortcuts import render
from .models import Product
from .forms import ProductForm, RowProductForm

# Create your views here.
def product_create_view(req):
    # print(req.GET)
    my_form = RowProductForm();
    if(req.method == "POST"):
        my_form = RowProductForm(req.POST);
        if(my_form.is_valid()):
            print(my_form.cleaned_data);
            Product.objects.create(**my_form.cleaned_data);
            my_form = RowProductForm()
        else:
            print(my_form.errors);
    context = {
        'form': my_form
    }
    return render(req, 'products/product_create.html', context);

# def product_create_view(req):
#     # print(req.GET)
#     if(req.method == "POST"):
#         my_title = req.POST.get('title')
#         print(my_title)
#     context = {}
#     return render(req, 'products/product_create.html', context);

# def product_create_view(req):
#     form = ProductForm(req.POST or None);
#     if form.is_valid():
#         form.save()
#         form = ProductForm()

#     context = {
#         'form': form
#     }
#     return render(req, 'products/product_create.html', context);

def product_detail_view(req):
    obj = Product.objects.get(id=1);
    # context = {
    #     'title': obj.title,
    #     'description': obj.description
    # }
    context = {
        'object': obj
    }
    return render(req, 'products/product_detail.html', context);