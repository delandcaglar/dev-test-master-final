from django.urls import path

from . import views
from .views import SellerById, SellerByHandle

urlpatterns = [
    path('handle/<str:seller_handle>/', SellerByHandle.as_view({
        'get': 'get'
    }),name="handle_get"),
    path('handle/', SellerByHandle.as_view({
        'post': 'create',
    }),name="handle_post"),
    path('<int:seller_id>/', SellerById.as_view({
        'get': 'get',
        'put': 'put',
    }),name="seller_id"),
]
