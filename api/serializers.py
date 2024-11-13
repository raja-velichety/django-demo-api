from rest_framework import serializers
from .models import Invoice, InvoiceDetail

class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = ['description', 'quantity', 'price', 'line_total']  

    # Custom validation for line_total
    def validate(self, data):
        if data['line_total'] != data['quantity'] * data['price']:
            raise serializers.ValidationError(
                "Line total should be the product of quantity and price."
            )
        return data

class InvoiceSerializer(serializers.ModelSerializer):
    details = InvoiceDetailSerializer(many=True)

    class Meta:
        model = Invoice
        fields = ['invoice_number', 'customer_name', 'date', 'details']

    def create(self, validated_data):
        details_data = validated_data.pop('details')
        
        # Create the invoice first
        invoice = Invoice.objects.create(**validated_data)
        
        # Create InvoiceDetail instances and associate them with the invoice
        for detail_data in details_data:
            InvoiceDetail.objects.create(invoice=invoice, **detail_data)
        
        return invoice

    def update(self, instance, validated_data):
        details_data = validated_data.pop('details', [])
        
        # Update the invoice fields
        instance.invoice_number = validated_data.get('invoice_number', instance.invoice_number)
        instance.customer_name = validated_data.get('customer_name', instance.customer_name)
        instance.date = validated_data.get('date', instance.date)
        instance.save()

        # for replacing the details with the new ones deleting it first
        instance.details.all().delete()
        # Create new InvoiceDetails if any
        for detail_data in details_data:
            InvoiceDetail.objects.create(invoice=instance, **detail_data)

        return instance

