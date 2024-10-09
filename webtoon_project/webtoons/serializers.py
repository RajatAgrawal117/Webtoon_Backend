from rest_framework import serializers
from .models import Webtoon
class WebtoonSerializer(serializers.ModelSerializer):
    characters = serializers.JSONField()

    class Meta:
        model = Webtoon
        fields = '__all__'

    def create(self, validated_data):
        characters = validated_data.pop('characters')
        webtoon = Webtoon.objects.create(**validated_data)
        webtoon.set_characters(characters)
        webtoon.save()
        return webtoon

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['characters'] = instance.get_characters()
        return representation