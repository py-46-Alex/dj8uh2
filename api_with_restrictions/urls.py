"""api_with_RL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#
from rest_framework.routers import DefaultRouter
from advertisements.views import ZadVievSet

#
r = DefaultRouter()
r.register('advertisements', ZadVievSet)
#
urlpatterns = [
    path('api/', include(r.urls)),
    path('admin/', admin.site.urls),]
