from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserDetail
from .serializers import UserDetailSerializer

@api_view(['GET'])
def retrieveDetails(request, username):
    try:
        user = UserDetail.objects.get(username=username)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)
    except UserDetail.DoesNotExist:
        return JsonResponse({'message': 'Username does not exist'}, status=404)

@api_view(['POST'])
def createUsername(request):
    serializer = UserDetailSerializer(data=request.data)
    if serializer.is_valid():
        if UserDetail.objects.filter(username=request.data.get('username')).exists():
            return JsonResponse({'message': 'Username already exists'}, status=400)
        serializer.save()
        return JsonResponse({'message': 'Created'})
    else:
        return Response(serializer.errors, status=400)

@api_view(['POST'])
def fillDetail(request):
    username = request.data.get('username')
    if not username:
        return Response({'error': 'Username is required'}, status=400)
    
    try:
        user = UserDetail.objects.get(username=username)
        serializer = UserDetailSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Saved successfully'})
        else:
            return Response(serializer.errors, status=400)
    except UserDetail.DoesNotExist:
        return JsonResponse({'error': 'Username does not exist'}, status=404)



@api_view(['POST'])
def createUserDetail(request):
    serializer = UserDetailSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def userDetail(request, pk):
    try:
        user_detail = UserDetail.objects.get(pk=pk)
    except UserDetail.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserDetailSerializer(user_detail)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserDetailSerializer(user_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
