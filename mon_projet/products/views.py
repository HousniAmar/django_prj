from django.shortcuts import render,get_object_or_404, redirect
from .models import Product
from .forms import ProductForm
# # Create your views here.
def index(request):
    return render(request,'products/products.html')


def product_dashboard(request):
    products = Product.objects.all()
    editing_product = None
    form = ProductForm()

    if request.method == 'POST':
        if 'add' in request.POST:
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('product_dashboard')

        elif 'edit_id' in request.POST:
            product = get_object_or_404(Product, pk=request.POST.get('edit_id'))
            form = ProductForm(instance=product)
            editing_product = product

        elif 'save_edit' in request.POST:
            product = get_object_or_404(Product, pk=request.POST.get('save_edit'))
            form = ProductForm(request.POST, instance=product)
            if form.is_valid():
                form.save()
                return redirect('product_dashboard')

        elif 'delete' in request.POST:
            product_id = request.POST.get('delete')
            product = get_object_or_404(Product, pk=product_id)
            product.delete()
            return redirect('product_dashboard')

    context = {
        'products': products,
        'form': form,
        'editing_product': editing_product,
    }
    return render(request, 'products/dashboard.html', context)
