from rest_framework import serializers
from . import models


class ProviderSerializer(serializers.ModelSerializer):
    language_name = serializers.CharField(source='language.short_name', read_only=True)
    currency_name = serializers.CharField(source='currency.symbol', read_only=True)

    class Meta:
        model = models.Provider
        fields = ('id', 'name', 'email', 'phoneNumber', 'language', 'language_name', 'currency', 'currency_name')


class ServiceAreaSerializer(serializers.ModelSerializer):
    provider_name = serializers.CharField(source='provider.name', read_only=True)

    class Meta:
        model = models.ServiceArea
        fields = ('id', 'provider', 'provider_name', 'price', 'poly')
