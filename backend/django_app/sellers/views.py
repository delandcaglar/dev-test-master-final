from django.core.exceptions import ObjectDoesNotExist
from django.http.response import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views import View
from rest_framework import permissions
from .models import Seller, OldHandles
from .serializers import sellerSerializer, oldHandlesSerializer
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response


class SellerById(viewsets.ViewSet):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'post', 'put', 'delete']

    def get(self, request, seller_id=None):
        slides = Seller.objects.filter(id=seller_id)
        serializer = sellerSerializer(slides, many=True)
        print(serializer)
        print("burasi data")
        print(serializer.data)
        if serializer.data == []:
            return Response({'error': 'seller not found'},status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.data[0])
        pass

    def put(self, request, seller_id=None):
        print("burasi mi", seller_id)
        print("burasi mi", request)
        print("burasi mi", request.data)
        print("burasi mi", request.data.get("name"))
        serializer1 = oldHandlesSerializer(data={"old_handle": request.data.get("handle"),
                                                 "seller": seller_id,
                                                 "name": request.data.get("name")
                                                 })
        slides = Seller.objects.get(id=seller_id)
        serializer = sellerSerializer(instance=slides, data=request.data)
        if serializer1.is_valid() and serializer.is_valid(): # means in the future we will be able to update this
            serializer.save()
            # serializer1.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        else:
            return Response({'cannot_be_done': 'cannot_be_done'}, status.HTTP_202_ACCEPTED)


class SellerByHandle(viewsets.ViewSet):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'post', 'put', 'delete']

    def get(self, request, seller_handle=None):
        try:
            slides = Seller.objects.filter(handle=seller_handle)
            serializer = sellerSerializer(slides, many=True)
            if slides.count() == 0:
                slides = OldHandles.objects.filter(old_handle=seller_handle)
                serializer = oldHandlesSerializer(slides, many=True)

            return Response(serializer.data[0])
            # return Response({'success': 'Record Added'})
            pass
        except:
            return Response({'error': 'seller not found'}, status.HTTP_404_NOT_FOUND)
            # return JsonResponse(status=404, data={'error': 'seller not found'})

    def create(self, request):
        serializer = oldHandlesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True) # it means link it is already taken
        serializer.save()
        # return Response(serializer.data, status.HTTP_202_ACCEPTED)
        return Response({'success': 'success'}, status.HTTP_202_ACCEPTED)
