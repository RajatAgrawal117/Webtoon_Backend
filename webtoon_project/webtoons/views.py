from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Webtoon
from .serializers import WebtoonSerializer
from rest_framework.throttling import UserRateThrottle

# Custom throttle class
class WebtoonThrottle(UserRateThrottle):
    rate = '100/day'  # Example rate limit for authenticated users

@api_view(['GET'])
@throttle_classes([WebtoonThrottle])  # Apply throttling for this endpoint
def get_all_webtoons(request):
    webtoons = Webtoon.objects.all()
    serializer = WebtoonSerializer(webtoons, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@throttle_classes([WebtoonThrottle])
def add_webtoon(request):
    serializer = WebtoonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_webtoon_by_id(request, webtoon_id):
    try:
        webtoon = Webtoon.objects.get(pk=webtoon_id)
    except Webtoon.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = WebtoonSerializer(webtoon)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_webtoon(request, webtoon_id):
    try:
        webtoon = Webtoon.objects.get(pk=webtoon_id)
    except Webtoon.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    webtoon.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
