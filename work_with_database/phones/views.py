from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort')
    template = 'catalog.html'
    phones = Phone.objects.all()
    if sort == 'name':
        phones = sorted(phones, key=lambda x: x.name)
    elif sort == 'min_price':
        phones = sorted(phones, key=lambda x: x.price)
    elif sort == 'max_price':
        phones = sorted(phones, key=lambda x: x.price, reverse=True)
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug)
    context = {'phone': phone[0]}
    return render(request, template, context)
