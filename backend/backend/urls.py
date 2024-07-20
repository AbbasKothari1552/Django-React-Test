from django.contrib import admin
from django.urls import path, include
# from api.views import CustomTokenCreateView   # *do not remove

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('auth/jwt/create/', CustomTokenCreateView.as_view(), name='jwt-create'), # *do not remove
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.social.urls')),
    
    # path for apps
    path('', include('api.urls')),
    path('store/', include('stores.urls')),
]
