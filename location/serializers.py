from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers


class LocationSerializer(serializers.Serializer):
    days = serializers.IntegerField(default=10)

    class Meta:
        fields = ("days",)

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    def validate(self, attrs):
        """
        :param attrs:
        :return: attrs
        """
        days = attrs.get("days", None)
        if days > 10:
            raise serializers.ValidationError(
                {"days": _("Days shouldn't be greater than 10 days.")}
            )
        return attrs
