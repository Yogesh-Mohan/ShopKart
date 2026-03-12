from django.db import models
import datetime
import os


# Create your models here.
def getfilename(request, filename):
    now_time = datetime.datetime.now().strftime("%Y%m%d%H_%M_%S")#year month day hour minute second
    new_filename="%s%s"%(now_time,filename) 
    return os.path.join('uploads/',new_filename) 

class Category (models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    images=models.ImageField(upload_to=getfilename,null=False,blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0=show,1=Hidden") # status la 0 na status vanthu show agum,1 hidden agum
   
    created_at=models.DateTimeField(auto_now_add=True) # created_at la date time automatic agum

    def __str__(self):
        return self.name
    

class Product (models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE) # on_delete=models.CASCADE na category delete agum pothu athoda products um delete agum
    name=models.CharField(max_length=100,null=False,blank=False)
    vendor=models.CharField(max_length=100,null=False,blank=False)
    quantity=models.IntegerField(null=False,blank=False)
    original_price=models.FloatField(null=False,blank=False)
    selling_price=models.FloatField(null=False,blank=False)

    product_images=models.ImageField(upload_to=getfilename,null=False,blank=False)  
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0=show,1=Hidden") # status la 0 na status vanthu show agum,1 hidden agum
    trending=models.BooleanField(default=False,help_text="0=show,1=Hidden") # trending la 0 na status vanthu show agum,1 hidden agum
    created_at=models.DateTimeField(auto_now_add=True) # created_at la date time automatic agum


