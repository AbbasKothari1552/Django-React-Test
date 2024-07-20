from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Address, GeoCoordinate
from .utils import get_lat_lng

@api_view(['POST'])
def create_geo_coordinate(request):
    if request.method == 'POST':
        address_data = request.data.get('address')
        if not address_data:
            return Response({"error": "Address data not provided"}, status=400)
        
        # Create or get the Address object
        address_obj, created = Address.objects.get_or_create(
            address_1=address_data['address_1'],
            city=address_data['city'],
            state=address_data['state'],
            country=address_data['country'],
            pin_code=address_data['pin_code']
        )
        
        # Check if GeoCoordinate already exists for this Address
        geo_coord = GeoCoordinate.objects.filter(address=address_obj).first()
        if geo_coord:
            return Response({"message": "GeoCoordinate already exists", "data": {
                "latitude": geo_coord.latitude,
                "longitude": geo_coord.longitude,
                "altitude": geo_coord.altitude
            }})
        
        api_key = '6699404a9936f776959004tsd87c57c'
        # If GeoCoordinate doesn't exist, fetch coordinates from geocoding API
        lat, lng = get_lat_lng(f"{address_obj.address_1}, {address_obj.city}, {address_obj.state}, {address_obj.country}, {address_obj.pin_code}, {api_key}")
        
        if lat is not None and lng is not None:
            # Create GeoCoordinate object
            geo_coord = GeoCoordinate.objects.create(
                address=address_obj,
                latitude=lat,
                longitude=lng
            )
            return Response({"message": "GeoCoordinate created", "data": {
                "latitude": geo_coord.latitude,
                "longitude": geo_coord.longitude,
                "altitude": geo_coord.altitude
            }})
        else:
            return Response({"error": "Failed to get coordinates from geocoding API"}, status=500)
