from rest_framework import serializers

from bank_accounts.models import AccountHistory, CitizenAccount, SavingProgramParticipant


class CitizenAccountCreateSerializer(serializers.Serializer):
    citizen_id = serializers.UUIDField()

    class Meta:
        model = CitizenAccount
        fields = []

    def create(self, validated_data):
        account = CitizenAccount(owner=self.validated_data["owner"],)
        account.save()
        return account


class CitizenAccountDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CitizenAccount
        fields = ["owner", "account_balance", "created_at", "modified_at"]


class CitizenAccountListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CitizenAccount
        fields = ["id", "owner", "created_at"]

class CitizenAccountUpdateSerializer(serializers.Serializer):
    amount_of_change = serializers.DecimalField(max_digits=9, decimal_places=2)


class CitizenAccountHistoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountHistory
        fields = "__all__"

class SavingProgramCreateSerializer(serializers.ModelSerializer):
    account_id = serializers.UUIDField(allow_null=False)

    class Meta:
        model = SavingProgramParticipant
        fields = ["deposit_balance", "account_id"]


class SavingProgramDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProgramParticipant
        fields = "__all__"


class SavingProgramListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProgramParticipant
        fields = ["id", "created_at", "interest_rate", "deposit_balance"]
