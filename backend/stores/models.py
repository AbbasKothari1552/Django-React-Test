from django.conf import settings
from django.db import models
from django.core.validators import RegexValidator


class Store(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=100)
    store_description = models.TextField()
    store_logo = models.ImageField(upload_to='store_logos/')
    contact_no = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message='Contact number must be a 10-digit number.'
            )
        ]
    )
    is_contact_verified = models.BooleanField(default=False)
    store_email = models.EmailField()
    instagram_id = models.CharField(max_length=100, blank=True, null=True)
    facebook_id = models.CharField(max_length=100, blank=True, null=True)
    youtube_id = models.CharField(max_length=100, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.store_name

class Address(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    pin_code = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}"
    
    def store_id(self):
        return self.store.id



class GeoCoordinate(models.Model):
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def store_name(self):
        return self.address.store.store_name
    store_name.short_description = 'Store Name'

    def address_id(self):
        return self.address.id



