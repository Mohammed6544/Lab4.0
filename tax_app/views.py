from django.http import HttpResponse
from django.shortcuts import render


tax_rate = 0.15

def home(request):

    return HttpResponse("This is a site to calculate tax.")

def calculate_tax(request, price):

    total_price = price + (price * tax_rate)
    return HttpResponse(f"Total price with tax: {total_price}")

def show_tax_rate(request):

    return render(request, 'tax_rate.html', {'tax_rate': tax_rate * 100})