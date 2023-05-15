from django.urls import path

from .views import CartView, CardAddView

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('add/<int:product_id>/', CardAddView.as_view(), name='cart-add'),
]
