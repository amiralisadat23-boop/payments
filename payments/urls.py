from django.urls import path
from . import views

urlpatterns = [
    path("pay/", views.send_request, name="send_request"),
    path("verify/", views.verify_payment, name="payment_verify"),
]
