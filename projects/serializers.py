from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id','Título', 'Contenido', 'Autor', 'Creado')
        read_only_fields = ('Creado',)