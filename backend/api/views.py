from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Project

class ProjectViewSet(viewsets.Viewset):
    permission_classes = [permissions.Allowany]
    queryset = Project.objects.all()

    def list(self, request):
        pass
    
    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass


    def update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass