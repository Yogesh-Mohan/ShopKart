from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('collections/', views.collections, name='collections'),
    path('collections/<str:name>/', views.collectionsview, name='collectionsview'),
    path('collections/<str:cname>/<str:pname>/', views.product_detail, name='product_detail'),
    path('search/', views.search_products, name='search'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_page, name='cart'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
