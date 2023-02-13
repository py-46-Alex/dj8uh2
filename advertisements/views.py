from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsAuthenticatedOrReadOnly, IsOwner
from advertisements.serializers import ZadSerializ

# 84cba275708ced3b3549b5fb1e03ca2d2c573b06
class ZadVievSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = ZadSerializ
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['user', 'created_at', ]
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = AdvertisementFilter
     # #
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    #
    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "destroy"]:
            return [IsAuthenticatedOrReadOnly(), IsOwner()]
    #
    #