from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from AliquotaApp.models import Produtos
from AliquotaApp.serializers import ProdutoSerializer

# Create your views here.

@csrf_exempt
def produtoApi(request, id=0):
    if request.method == 'GET':
        produtos = Produtos.objects.all()
        produtos_serializer = ProdutoSerializer(produtos, many=True)
        return JsonResponse(produtos_serializer.data, safe=False)

    elif request.method == 'POST':
        produto_data = JSONParser().parse(request)
        produto_serializer = ProdutoSerializer(data=produto_data)

        if produto_serializer.is_valid():
            produto_serializer.save()
            return JsonResponse('Adicionado com sucesso', safe=False)

        return JsonResponse('Falha ao adicionar', safe=False)

    elif request.method == 'PUT':
        produto_data = JSONParser().parse(request)
        produto = Produtos.objects.get(id=produto_data['id'])
        produto_serializer = ProdutoSerializer(produto, data=produto_data)

        if produto_serializer.is_valid():
            produto_serializer.save()
            return JsonResponse('Atualizado com sucesso', safe=False)

        return JsonResponse('Falha ao atualizar', safe=False)

    elif request.method == 'DELETE':
        produto = Produtos.objects.get(id=id)
        produto.delete()
        return JsonResponse('Deletado com sucesso', safe=False)
