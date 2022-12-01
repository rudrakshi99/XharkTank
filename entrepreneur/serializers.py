from rest_framework import serializers

from entrepreneur.models import Entrepreneur
from investor.serializers import InvestorSerializer


class EntrepreneurSerializer(serializers.ModelSerializer):
    offers = InvestorSerializer(read_only=True, many=True)

    class Meta:
        model = Entrepreneur
        fields = (
            "id",
            "entrepreneur",
            "pitchTitle",
            "pitchIdea",
            "askAmount",
            "equity",
            "offers",
        )

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret["id"] = str(ret["id"])
        return ret

    def update(self, instance, validated_data):
        instance.offers.add(validated_data)
        instance.save()
        return instance
