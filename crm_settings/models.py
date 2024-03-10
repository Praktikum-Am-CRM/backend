from django.db import models

from ambassador.models import AmbassadorStatus, Goal
from crm_messages.models import MessageStatus, MessageType
from merches.models import DeliveryStatus
from reports.models import ReportStatus, ReportType


class CrmSettings(models.Model):
    default_ambassador_status = models.OneToOneField(
        AmbassadorStatus,
        on_delete=models.PROTECT,
        null=False, blank=False
    )
    default_message_type = models.OneToOneField(
        MessageType,
        on_delete=models.PROTECT,
        null=True, blank=True
    )
    default_message_status = models.OneToOneField(
        MessageStatus,
        on_delete=models.PROTECT,
        null=True, blank=True,
        related_name='default_message_status'
    )
    delayed_sending_message_type = models.OneToOneField(
        MessageStatus,
        on_delete=models.PROTECT,
        null=False, blank=False,
        related_name='delayed_sending_message_type'
    )
    default_delivery_status = models.OneToOneField(
        DeliveryStatus,
        on_delete=models.PROTECT,
        null=False, blank=False
    )
    default_report_status = models.OneToOneField(
        ReportStatus,
        on_delete=models.PROTECT,
        null=True, blank=True
    )
    default_report_type = models.OneToOneField(
        ReportType,
        on_delete=models.PROTECT,
        null=True, blank=True
    )
    goal_own_version = models.OneToOneField(
        Goal,
        on_delete=models.PROTECT,
        null=True, blank=True,
    )
    date = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ('-date',)
