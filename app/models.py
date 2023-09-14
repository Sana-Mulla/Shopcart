from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
STATE_CHOICES = (
                ('Maharashtra', 'Maharashtra'),
                ('Tripura', 'Tripura'),
                ('Tamilnadu', 'Tamilnadu'),
                ('J&K', 'J&K'),
                ('UttarPradesh', 'UttarPradesh'),
                ('West Bengal', 'West Bengal'),

)

class Customer(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.IntegerField()
    state  = models.CharField(choices=STATE_CHOICES, max_length=50)

    def __str__(self):
        return str(self.id)
    
CATEGORY_CHOICES =(
                ('M','Mobile'),
                ('L','Laptop'),
                ('TW','Topware'),
                ('BW','Bottomware'),
                )

SIZE_CHOICES =(
                ('S','Small'),
                ('M','Medium'),
                ('L','Large'),
                ('XL','ExtraLarge'),
                ('XXL','ExtraLarge'),
                 

)



class Product(models.Model):
    title = models.CharField(max_length=200)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    size= models.CharField(choices=SIZE_CHOICES, max_length=3,default='M')
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)
    
    @property
    def reduced_prices(self):
        return self.discounted_price - ((self.discounted_price*5)/100)
    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity= models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    

STATUS_CHOICES = (
                ('Accepted', 'Accepted'),
                ('Packed', 'Packed'),
                ('On The Way','On The Way'),
                ('Delivered', 'Delivered'),
                ('Cancel', 'Cancel')
                )

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES,default='Pending')

    def __str__(self):
        return str(self.id)
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price




