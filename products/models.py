from django.db import models

# Models for cars app

class Product(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE, 'Live'), (DELETE, 'Delete'))

    # Define category choices directly
    CATEGORY_CHOICES = (
        ('cloth', 'Cloth'),
        ('watch', 'Watch'),
        ('footwear', 'Footwear'),
        ('electronics', 'Electronics'),
        ('bags', 'Bags'),
    )

    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='media/')
    rating = models.IntegerField(default=1)
    priority = models.IntegerField(default=0)
    
    # Add categories field
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES,default='', blank=True)

    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title






