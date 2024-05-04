# vendors/urls.py`:
# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('api/vendors/', views.VendorListCreateView.as_view(), name='vendor-list'),
    path('api/vendors/<int:pk>/', views.VendorRetrieveUpdateDestroyView.as_view(), name='vendor-detail'),
    path('api/purchase_orders/', views.PurchaseOrderListCreateView.as_view(), name='purchase-order-list'),
    path('api/purchase_orders/<int:pk>/', views.PurchaseOrderRetrieveUpdateDestroyView.as_view(), name='purchase-order-detail'),
    path('api/vendors/<int:vendor_id>/performance/', views.VendorPerformanceView.as_view(), name='vendor-performance'),
    path('api/purchase_orders/<int:po_id>/acknowledge/', views.PurchaseOrderAcknowledgeView.as_view(), name='purchase-order-acknowledge'),
]
