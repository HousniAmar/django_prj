from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def get_image_url(self):
        """Return the image URL or a default URL if no image is uploaded"""
        if self.image:
            return self.image.url
        else:
            # Default product image URL
            return "https://images.squarespace-cdn.com/content/v1/5d14e8bfa505890001205e37/1695585825282-APKBZGPET2G61FCSRHH3/avis-yves-saint-laurent-mon-paris-intensement-eau-de-parfum-femme-revue-pauuulette-IMG_7573.jpg"

  
