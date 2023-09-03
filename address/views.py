from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import AddressSerializer
from .models import Address


@api_view(['GET'])
def search_address_by_name(request):
    nome = request.data.get('nome', None)
    if nome is not None:
        addresses = Address.objects.filter(data__nome=nome)
        if addresses.exists():
            serializer = AddressSerializer(addresses, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse({'error': 'Nome não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return JsonResponse({'error': 'Nome não especificado'}, status=status.HTTP_400_BAD_REQUEST)
