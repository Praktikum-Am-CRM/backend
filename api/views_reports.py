from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from reports.models import Report
from reports.serializers import ReportSerializer


class ReportListCreateAPIView(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]


class ReportRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]
