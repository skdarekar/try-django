from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, RowProductForm

# Create your views here.
# def product_create_view(req):
#     # print(req.GET)
#     my_form = RowProductForm();
#     if(req.method == "POST"):
#         my_form = RowProductForm(req.POST);
#         if(my_form.is_valid()):
#             print(my_form.cleaned_data);
#             Product.objects.create(**my_form.cleaned_data);
#             my_form = RowProductForm()
#         else:
#             print(my_form.errors);
#     context = {
#         'form': my_form
#     }
#     return render(req, 'products/product_create.html', context);

# def product_create_view(req):
#     # print(req.GET)
#     if(req.method == "POST"):
#         my_title = req.POST.get('title')
#         print(my_title)
#     context = {}
#     return render(req, 'products/product_create.html', context);

def product_create_view(req):
    form = ProductForm(req.POST or None);
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }
    return render(req, 'products/product_create.html', context);

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

def render_initial_view(req):
    initial_data = {
        'title': "My initial title"
    }
    obj = Product.objects.get(id=1)
    form = ProductForm(req.POST or None, instance=obj);
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }
    return render(req, 'products/product_create.html', context);

def dynamic_lookup_view(req, my_id):
    # obj = Product.objects.get(id=id);
    # obj = get_object_or_404(Product, id=id)
    try:
        obj = Product.objects.get(id=my_id);
    except Product.DoesNotExist:
        raise Http404

    context = {
        'object': obj
    }
    return render(req, 'products/product_detail.html', context);

def delete_product_view(req, my_id):
    obj = get_object_or_404(Product, id=my_id)
    if(req.method == "POST"):
        obj.delete();
        return redirect('../../')
    context = {
        'obj': obj
    }
    return render(req, 'products/product_delete.html', context)

def preview_products_list(req):
    query_set = Product.objects.all();
    context = {
        'object_list': query_set
    }
    return render(req, 'products/product_list.html', context)
