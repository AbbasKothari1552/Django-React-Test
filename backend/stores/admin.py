from django.contrib import admin
from stores.models import *

# Store view in admin panel
class StoreAdmin(admin.ModelAdmin):
    list_display = ['id','store_name', 'contact_no', 'store_email', 'is_contact_verified', 'created_at', 'updated_at']
    search_fields = ['store_name', 'store_email', 'contact_no']
    list_filter = ['is_contact_verified', 'created_at']

# address view in admin panel
class addressAdmin(admin.ModelAdmin):
    list_display = ['id','store_id','store', 'city', 'state', 'country', 'pin_code']
    search_fields = ['store', 'city', 'state']
    list_filter = ['created_at']

# Geo-coordinates view in admin panel
class GeoCoordinateAdmin(admin.ModelAdmin):
    list_display = ('id','address_id','store_name', 'latitude', 'longitude')
    search_fields = ('address__store__store_name',)


# Registering all the models.
admin.site.register(Store, StoreAdmin)
admin.site.register(Address, addressAdmin)
admin.site.register(GeoCoordinate, GeoCoordinateAdmin)

