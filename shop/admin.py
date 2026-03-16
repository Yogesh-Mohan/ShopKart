from django.contrib import admin
from .models import * #(* na models la irukura ella models um import pannum)
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)

