from rest_framework import serializers
from investor.models import Investor


class InvestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investor
        fields = (
            "id",
            "investor",
            "amount",
            "equity",
            "comment",
        )

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret["id"] = str(ret["id"])
        return ret
