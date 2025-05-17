from rest_framework import viewsets, permissions
from .models import Patient
from .serializers import PatientSerializer

class IsOwnerOrChiropractor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.user == request.user

class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrChiropractor]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Patient.objects.all()
        return Patient.objects.filter(user=user)
