from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Movement
from .serializers import MovementSerializer
import requests


class MovementViewSet(viewsets.ModelViewSet):
    queryset = Movement.objects.all()
    serializer_class = MovementSerializer

    def perform_create(self, serializer):
        movement = serializer.save()

        # Llamar al inventory
        inventory_url = f'http://localhost:8002/api/products/{movement.producto_id}/'

        # Consultar
        producto = requests.get(inventory_url).json()
        stock_actual = producto['stock']

        if movement.tipo == 'entrada':
            nuevo_stock = stock_actual + movement.cantidad
        else:
            if movement.cantidad > stock_actual:
                raise ValueError('No puede salir más stock del disponible.')
            nuevo_stock = stock_actual - movement.cantidad

        # Actualizar
        requests.put(
            inventory_url,
            json={
                'nombre': producto['nombre'],
                'descripcion': producto['descripcion'],
                'stock': nuevo_stock
            }
        )
