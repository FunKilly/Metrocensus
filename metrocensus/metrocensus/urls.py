from django.urls import path
from rest_framework import routers

from admin.views import CitizenViewSet, CreateTokenView, UserViewSet
from bank_accounts.views import BankAccountViewSet, SavingProgramViewSet


router = routers.SimpleRouter()
router.register(r"admin-panel/users", UserViewSet)
router.register(r"admin-panel/citizens", CitizenViewSet)
router.register(r"bank/accounts", BankAccountViewSet)
router.register(r"bank/saving-programs", SavingProgramViewSet)

urlpatterns = [
    path("admin-panel/login", CreateTokenView.as_view(), name="login"),
]

urlpatterns += router.urls
