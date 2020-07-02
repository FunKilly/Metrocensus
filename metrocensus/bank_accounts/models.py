import uuid
from datetime import datetime

from django.db import models

from citizens.models import Citizen


class CitizenAccount(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(Citizen, on_delete=models.PROTECT)
    account_balance = models.DecimalField(default=0, decimal_places=2, max_digits=9)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "citizen_account"

    def add_entry_to_operation_history(self, amount_of_change):
        description = self.generate_description(amount_of_change)

        entry = AccountHistory(account=self, description=description)
        entry.save()

    def generate_description(self, amount_of_change):
        return f"{datetime.now()}: The amount of change is equal : {amount_of_change}, current account balance is equal: {self.account_balance}"


class AccountHistory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account = models.ForeignKey(CitizenAccount, on_delete=models.PROTECT)
    description = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "account_history"


class SavingProgramParticipant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account = models.ForeignKey(CitizenAccount, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=4, default=0.055)

    class Meta:
        db_table = "saving_program_participant"
