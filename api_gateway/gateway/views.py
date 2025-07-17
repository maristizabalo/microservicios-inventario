import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.http import JsonResponse


class ProxyView(APIView):
    def get_permissions(self):
        service = self.kwargs.get('service')
        path = self.kwargs.get('path')

        if service == 'auth' and (
            'token' in path or 'register' in path
        ):
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def get(self, request, service, path):
        return self.forward_request(request, service, path)

    def post(self, request, service, path):
        return self.forward_request(request, service, path)

    def put(self, request, service, path):
        return self.forward_request(request, service, path)

    def delete(self, request, service, path):
        return self.forward_request(request, service, path)

    def forward_request(self, request, service, path):
        services_map = {
            'auth': 'http://localhost:8001/api/',
            'inventory': 'http://localhost:8002/api/',
            'stock': 'http://localhost:8003/api/',
        }

        base_url = services_map.get(service)
        if not base_url:
            return JsonResponse({'error': 'Servicio no encontrado'}, status=404)

        url = base_url.rstrip('/') + '/' + path

        headers = {
            "Authorization": request.headers.get("Authorization")
        }

        method = request.method.lower()

        if method in ['post', 'put', 'patch']:
            response = requests.request(
                method=method,
                url=url,
                headers=headers,
                json=request.data
            )
        else:
            response = requests.request(
                method=method,
                url=url,
                headers=headers,
                params=request.query_params
            )

        try:
            return Response(response.json(), status=response.status_code)
        except Exception:
            return Response({}, status=response.status_code)
