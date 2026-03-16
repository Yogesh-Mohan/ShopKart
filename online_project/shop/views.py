from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from .models import Category, Product
import json

# Create your views here.
def home(request):
    # Get trending products and categories for home page
    trending_products = Product.objects.filter(trending=True, status=False)[:8]
    categories = Category.objects.filter(status=False)[:6]
    
    context = {
        'trending_products': trending_products,
        'categories': categories,
    }
    return render(request, "shop/index.html", context)

def collections(request):
    # Show all categories
    categories = Category.objects.filter(status=False)
    context = {'categories': categories}
    return render(request, "shop/collections.html", context)

def collectionsview(request, name):
    # Show products in a specific category
    if Category.objects.filter(name=name, status=False):
        products = Product.objects.filter(category__name=name, status=False)
        context = {
            'products': products,
            'category_name': name
        }
        return render(request, "shop/products/index.html", context)
    else:
        messages.warning(request, "No such category found")
        return redirect('collections')

def product_detail(request, cname, pname):
    # Show individual product details
    if Category.objects.filter(name=cname, status=False):
        if Product.objects.filter(name=pname, status=False):
            product = Product.objects.filter(name=pname, status=False).first()
            context = {'product': product}
            return render(request, "shop/products/product_detail.html", context)
        else:
            messages.error(request, "No such product found")
            return redirect('collections')
    else:
        messages.error(request, "No such category found")
        return redirect('collections')

def search_products(request):
    # Search functionality
    query = request.GET.get('q', '')
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | 
            Q(description__icontains=query) | 
            Q(vendor__icontains=query),
            status=False
        )
    else:
        products = Product.objects.filter(status=False)
    
    context = {
        'products': products,
        'query': query
    }
    return render(request, "shop/search.html", context)

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already registered")
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password
                )
                messages.success(request, "Registration successful! Please login.")
                return redirect('login')
        else:
            messages.error(request, "Passwords do not match")
            return redirect('register')
    
    return render(request, "shop/register.html")

def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.first_name}!")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')
    
    return render(request, "shop/login.html")

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logged out successfully")
    return redirect('home')

# Shopping Cart Functions
def add_to_cart(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        if request.user.is_authenticated:
            data = json.load(request)
            product_id = data['product_id']
            product_qty = data['product_qty']
            
            if Product.objects.filter(id=product_id):
                # Here you would typically save to a Cart model
                # For now, we'll use session-based cart
                cart = request.session.get('cart', {})
                
                if str(product_id) in cart:
                    cart[str(product_id)] += int(product_qty)
                else:
                    cart[str(product_id)] = int(product_qty)
                
                request.session['cart'] = cart
                return JsonResponse({'status': 'Added to cart'}, status=200)
            else:
                return JsonResponse({'status': 'Product not found'}, status=404)
        else:
            return JsonResponse({'status': 'Login to add to cart'}, status=200)
    else:
        return JsonResponse({'status': 'Invalid request'}, status=200)

def cart_page(request):
    if request.user.is_authenticated:
        cart = request.session.get('cart', {})
        cart_products = []
        total_price = 0
        
        for product_id, qty in cart.items():
            product = Product.objects.get(id=product_id)
            subtotal = product.selling_price * qty
            total_price += subtotal
            
            cart_products.append({
                'product': product,
                'qty': qty,
                'subtotal': subtotal
            })
        
        context = {
            'cart_products': cart_products,
            'total_price': total_price
        }
        return render(request, "shop/cart.html", context)
    else:
        return redirect('login')
