from rest_framework.response import Response
from rest_framework.decorators import api_view
from samata_base.models import Item
from .serializers import ItemSerializer
from django.db.models import Sum


@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getDataSum(request):
    itemsPrice = Item.objects.aggregate(Sum('price'))
    return Response('Bendra sa'
                    'mata: ' + str(round(itemsPrice['price__sum'], 2)))


@api_view(['POST'])
def postData(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteData(request, item_id):
    item = Item.objects.get(pk=item_id)
    item.delete()
    return Response('Pašalintas įrašas su id: ' + item_id)

@api_view(['POST'])
def updateData(request, item_id):
    item = Item.objects.get(id=item_id)
    serializer = ItemSerializer(instance=item, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



