from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from django.db.models import F, Sum
from rest_framework.views import APIView
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from .serializers import VendorSerializer, PurchaseOrderSerializer, HistoricalPerformanceSerializer
from datetime import datetime, timedelta

class VendorListCreateView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def perform_create(self, serializer):
        vendor = serializer.save()
        self.update_vendor_performance(vendor)

    def update_vendor_performance(self, vendor):
        completed_pos = vendor.purchase_orders.filter(status='completed')
        on_time_deliveries = completed_pos.filter(delivery_date__lte=F('delivery_date')).count()
        on_time_delivery_rate = on_time_deliveries / completed_pos.count() if completed_pos.count() else 0
        quality_ratings = [po.quality_rating for po in completed_pos if po.quality_rating is not None]
        quality_rating_avg = sum(quality_ratings) / len(quality_ratings) if quality_ratings else 0
        response_times = [po.acknowledgment_date - po.issue_date for po in completed_pos if po.acknowledgment_date is not None]
        average_response_time = sum(response_times, timedelta()).total_seconds() / len(response_times) / 3600 if response_times else 0
        fulfilled_pos = completed_pos.filter(quality_rating__isnull=False)
        fulfillment_rate = fulfilled_pos.count() / completed_pos.count() if completed_pos.count() else 0

        vendor.on_time_delivery_rate = on_time_delivery_rate
        vendor.quality_rating_avg = quality_rating_avg
        vendor.average_response_time = average_response_time
        vendor.fulfillment_rate = fulfillment_rate
        vendor.save()

        HistoricalPerformance.objects.create(
            vendor=vendor,
            on_time_delivery_rate=on_time_delivery_rate,
            quality_rating_avg=quality_rating_avg,
            average_response_time=average_response_time,
            fulfillment_rate=fulfillment_rate
        )

class VendorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def perform_update(self, serializer):
        vendor = serializer.save()
        self.update_vendor_performance(vendor)

    def update_vendor_performance(self, vendor):
        completed_pos = vendor.purchase_orders.filter(status='completed')
        on_time_deliveries = completed_pos.filter(delivery_date__lte=F('delivery_date')).count()
        on_time_delivery_rate = on_time_deliveries / completed_pos.count() if completed_pos.count() else 0
        quality_ratings = [po.quality_rating for po in completed_pos if po.quality_rating is not None]
        quality_rating_avg = sum(quality_ratings) / len(quality_ratings) if quality_ratings else 0
        response_times = [po.acknowledgment_date - po.issue_date for po in completed_pos if po.acknowledgment_date is not None]
        average_response_time = sum(response_times, timedelta()).total_seconds() / len(response_times) / 3600 if response_times else 0
        fulfilled_pos = completed_pos.filter(quality_rating__isnull=False)
        fulfillment_rate = fulfilled_pos.count() / completed_pos.count() if completed_pos.count() else 0

        vendor.on_time_delivery_rate = on_time_delivery_rate
        vendor.quality_rating_avg = quality_rating_avg
        vendor.average_response_time = average_response_time
        vendor.fulfillment_rate = fulfillment_rate
        vendor.save()

        HistoricalPerformance.objects.create(
            vendor=vendor,
            on_time_delivery_rate=on_time_delivery_rate,
            quality_rating_avg=quality_rating_avg,
            average_response_time=average_response_time,
            fulfillment_rate=fulfillment_rate
        )

class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def perform_create(self, serializer):
        po = serializer.save()
        self.update_vendor_performance(po.vendor)

    def update_vendor_performance(self, vendor):
        completed_pos = vendor.purchase_orders.filter(status='completed')
        on_time_deliveries = completed_pos.filter(delivery_date__lte=F('delivery_date')).count()
        on_time_delivery_rate = on_time_deliveries / completed_pos.count() if completed_pos.count() else 0
        quality_ratings = [po.quality_rating for po in completed_pos if po.quality_rating is not None]
        quality_rating_avg = sum(quality_ratings) / len(quality_ratings) if quality_ratings else 0
        response_times = [po.acknowledgment_date - po.issue_date for po in completed_pos if po.acknowledgment_date is not None]
        average_response_time = sum(response_times, timedelta()).total_seconds() / len(response_times) / 3600 if response_times else 0
        fulfilled_pos = completed_pos.filter(quality_rating__isnull=False)
        fulfillment_rate = fulfilled_pos.count() / completed_pos.count() if completed_pos.count() else 0

        vendor.on_time_delivery_rate = on_time_delivery_rate
        vendor.quality_rating_avg = quality_rating_avg
        vendor.average_response_time = average_response_time
        vendor.fulfillment_rate = fulfillment_rate
        vendor.save()

        HistoricalPerformance.objects.create(
            vendor=vendor,
            on_time_delivery_rate=on_time_delivery_rate,
            quality_rating_avg=quality_rating_avg,
            average_response_time=average_response_time,
            fulfillment_rate=fulfillment_rate
        )

class PurchaseOrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def perform_update(self, serializer):
        po = serializer.save()
        self.update_vendor_performance(po.vendor)

    def update_vendor_performance(self, vendor):
        completed_pos = vendor.purchase_orders.filter(status='completed')
        on_time_deliveries = completed_pos.filter(delivery_date__lte=F('delivery_date')).count()
        on_time_delivery_rate = on_time_deliveries / completed_pos.count() if completed_pos.count() else 0
        quality_ratings = [po.quality_rating for po in completed_pos if po.quality_rating is not None]
        quality_rating_avg = sum(quality_ratings) / len(quality_ratings) if quality_ratings else 0
        response_times = [po.acknowledgment_date - po.issue_date for po in completed_pos if po.acknowledgment_date is not None]
        average_response_time = sum(response_times, timedelta()).total_seconds() / len(response_times) / 3600 if response_times else 0
        fulfilled_pos = completed_pos.filter(quality_rating__isnull=False)
        fulfillment_rate = fulfilled_pos.count() / completed_pos.count() if completed_pos.count() else 0

        vendor.on_time_delivery_rate = on_time_delivery_rate
        vendor.quality_rating_avg = quality_rating_avg
        vendor.average_response_time = average_response_time
        vendor.fulfillment_rate = fulfillment_rate
        vendor.save()

        HistoricalPerformance.objects.create(
            vendor=vendor,
            on_time_delivery_rate=on_time_delivery_rate,
            quality_rating_avg=quality_rating_avg,
            average_response_time=average_response_time,
            fulfillment_rate=fulfillment_rate
        )

class VendorPerformanceView(APIView):
    def get(self, request, vendor_id):
        vendor = get_object_or_404(Vendor, id=vendor_id)
        vendor.update_performance_metrics()
        serializer = VendorSerializer(vendor)
        return Response(serializer.data)

class PurchaseOrderAcknowledgeView(APIView):
    def post(self, request, po_id):
        po = get_object_or_404(PurchaseOrder, id=po_id)
        po.acknowledgment_date = datetime.now()
        po.save()
        vendor = po.vendor
        self.update_vendor_performance(vendor)
        return Response({'message': 'Purchase order acknowledged'}, status=status.HTTP_200_OK)

    def update_vendor_performance(self, vendor):
        completed_pos = vendor.purchase_orders.filter(status='completed')
        on_time_deliveries = completed_pos.filter(delivery_date__lte=F('delivery_date')).count()
        on_time_delivery_rate = on_time_deliveries / completed_pos.count() if completed_pos.count() else 0
        quality_ratings = [po.quality_rating for po in completed_pos if po.quality_rating is not None]
        quality_rating_avg = sum(quality_ratings) / len(quality_ratings) if quality_ratings else 0
        response_times = [po.acknowledgment_date - po.issue_date for po in completed_pos if po.acknowledgment_date is not None]
        average_response_time = sum(response_times, timedelta()).total_seconds() / len(response_times) / 3600 if response_times else 0
        fulfilled_pos = completed_pos.filter(quality_rating__isnull=False)
        fulfillment_rate = fulfilled_pos.count() / completed_pos.count() if completed_pos.count() else 0

        vendor.on_time_delivery_rate = on_time_delivery_rate
        vendor.quality_rating_avg = quality_rating_avg
        vendor.average_response_time = average_response_time
        vendor.fulfillment_rate = fulfillment_rate
        vendor.save()

        HistoricalPerformance.objects.create(
            vendor=vendor,
            on_time_delivery_rate=on_time_delivery_rate,
            quality_rating_avg=quality_rating_avg,
            average_response_time=average_response_time,
            fulfillment_rate=fulfillment_rate
        )

# HTML Template Views
def index(request):
    return render(request, 'base.html', {})

def vendor_list(request):
    vendors = Vendor.objects.all()
    context = {'vendors': vendors}
    return render(request, 'vendor_list.html', context)

def vendor_detail(request, vendor_id):
    vendor = get_object_or_404(Vendor, id=vendor_id)
    context = {'vendor': vendor}
    return render(request, 'vendor_detail.html', context)

def vendor_performance(request, vendor_id):
    vendor = get_object_or_404(Vendor, id=vendor_id)
    vendor.update_performance_metrics()
    context = {'vendor': vendor}
    return render(request, 'vendor_performance.html', context)


def purchase_order_list(request):
    purchase_orders = PurchaseOrder.objects.all()
    context = {'purchase_orders': purchase_orders}
    return render(request, 'purchase_order_list.html', context)

def purchase_order_detail(request, po_id):
    purchase_order = get_object_or_404(PurchaseOrder, id=po_id)
    context = {'purchase_order': purchase_order}
    return render(request, 'purchase_order_detail.html', context)
