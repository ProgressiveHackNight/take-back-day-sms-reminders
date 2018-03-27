from rest_framework import serializers
from tbdsms.models import Location, AlertRecipient, LANGUAGE_CHOICES, STYLE_CHOICES

class LocationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=True, max_length=300)
    type = serializers.CharField(required=False, allow_blank=True, max_length=100)
    address = serializers.CharField(required=False, allow_blank=True, max_length=200)
    latitude = serializers.FloatField(required=False)
    longitude = serializers.FloatField(required=False)

    def create(self, validated_data):
        """
        Create and return a new `Location` instance, given the validated data.
        """
        return Location.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.type = validated_data.get('type', instance.type)
        instance.address = validated_data.get('address', instance.address)
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.longitude = validated_data.get('longitude', instance.longitude)
        instance.save()
        return instance

class AlertRecipientSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    class Meta:
        model = AlertRecipient
        fields = ('phone_number', 'zip_code', 'language', 'location')
