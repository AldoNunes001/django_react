from rest_framework import serializers
from AliquotaApp.models import Produtos


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        fields = ('id', 'aliquota', 'produto', 'ncm', 'fecoep')

