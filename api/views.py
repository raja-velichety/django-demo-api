from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer
from rest_framework import viewsets

# Create your views here.
# first method to create a view but this has only post and put and no other crud 
class InvoiceView(APIView):
    def post(self, request, *args, **kwargs):
        # Use the InvoiceSerializer to validate and save the data
        serializer = InvoiceSerializer(data=request.data)
        
        if serializer.is_valid():
            # Save the invoice and its related InvoiceDetails (handled automatically by the serializer)
            serializer.save()
            
            # Return a successful response with the serialized data of the created invoice
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        invoice_number = request.data.get('invoice_number', None)

        # Check for invoice number
        if not invoice_number:
            return Response({"detail": "Invoice number is required for updating."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Fetch to check whether there is any valid data with invoice number else return not found
            invoice = Invoice.objects.get(invoice_number=invoice_number)
        except Invoice.DoesNotExist:
            return Response({"detail": "Invoice not found."}, status=status.HTTP_404_NOT_FOUND)

        # Use the InvoiceSerializer to update the invoice and its InvoiceDetails
        serializer = InvoiceSerializer(invoice, data=request.data, partial=False)  # partial=False for required fields

        if serializer.is_valid():
            # updation is done by the serializer (handled automatically by the serializer)
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)