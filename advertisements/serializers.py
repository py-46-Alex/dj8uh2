from itertools import count

from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from advertisements.models import Advertisement
from rest_framework.exceptions import ValidationError

#
class ZadSerializ(serializers.ModelSerializer):
    """Serializer для объявления."""
    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'user', 'status', 'created_at', )
        read_only_fields = ['user', ]
    #
    def create(self, validated_data):
        # print(validated_data)
        validated_data["user"] = self.context["request"].user
        # print(self.context)
        return super().create(validated_data)
    #     """Метод для создания"""
    #
    def validate(self, data):
        request = self.context['request']
        qty_advs = count(Advertisement.objects.filter(user=request.user, status='OPEN'))
        #
        if request.method == 'POST':
            if qty_advs >= 10:
                raise ValidationError('Вы достигли максимального количества открытых объявлений (10шт)')
        #
        if request.method == 'PATCH':
            if data.get('status') == 'OPEN':
                if qty_advs >= 10:
                    raise ValidationError('Вы достигли максимального количества открытых объявлений (10шт)')
        #
        return data