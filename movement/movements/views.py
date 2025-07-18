from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Movement
from .serializers import MovementSerializer
import requests


class MovementViewSet(viewsets.ModelViewSet):
    queryset = Movement.objects.all()
    serializer_class = MovementSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        producto_id = serializer.validated_data['producto_id']
        cantidad = serializer.validated_data['cantidad']
        tipo = serializer.validated_data['tipo']

        inventory_url = f'http://localhost:8002/api/products/{producto_id}/'
        response = requests.get(inventory_url)
        if response.status_code != 200:
            return Response({"error": "Producto no encontrado en el inventario."}, status=status.HTTP_400_BAD_REQUEST)

        producto = response.json()
        stock_actual = producto['stock']

        if tipo == 'entrada':
            nuevo_stock = stock_actual + cantidad
        else:
            if cantidad > stock_actual:
                return Response(
                    {"error": "No puede salir más stock del disponible."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            nuevo_stock = stock_actual - cantidad

        requests.put(
            inventory_url,
            json={
                'nombre': producto['nombre'],
                'descripcion': producto['descripcion'],
                'stock': nuevo_stock
            }
        )

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
