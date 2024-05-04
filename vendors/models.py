# vendor_management\vendors\models.py
from django.db import models
from django.db.models import Count, Avg, F
from django.utils import timezone

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=20, unique=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

    def update_performance_metrics(self):
        # Calculate On-Time Delivery Rate
        completed_orders_count = self.purchase_orders.filter(status='completed').count()
        on_time_delivery_count = self.purchase_orders.filter(status='completed', delivery_date__lte=timezone.now()).count()
        if completed_orders_count > 0:
            self.on_time_delivery_rate = (on_time_delivery_count / completed_orders_count) * 100
        else:
            self.on_time_delivery_rate = 0

        # Calculate Quality Rating Average
        self.quality_rating_avg = self.purchase_orders.filter(status='completed').aggregate(avg_quality=Avg('quality_rating'))['avg_quality'] or 0

        # Calculate Average Response Time
        response_times = self.purchase_orders.filter(status='completed', acknowledgment_date__isnull=False, issue_date__isnull=False).annotate(
            response_time=F('acknowledgment_date') - F('issue_date')).aggregate(avg_response=Avg('response_time'))['avg_response'] or 0
        self.average_response_time = response_times

        # Calculate Fulfillment Rate
        successful_orders_count = self.purchase_orders.filter(status='completed', issue_date__isnull=False).count()
        if completed_orders_count > 0:
            self.fulfillment_rate = (successful_orders_count / completed_orders_count) * 100
        else:
            self.fulfillment_rate = 0

        self.save()

    def __str__(self):
        return self.name

class PurchaseOrder(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]
    
    po_number = models.CharField(max_length=20, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='purchase_orders')
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Update vendor performance metrics upon saving a purchase order
        self.vendor.update_performance_metrics()

    def __str__(self):
        return self.po_number


class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='historical_performance')
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"{self.vendor.name} - {self.date}"
