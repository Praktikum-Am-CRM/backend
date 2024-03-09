from .models import CrmSettings


class CRMDefaultSettings:
    def __init__(self):
        try:
            self._crm_settings = CrmSettings.objects.first()
        except Exception:
            self._crm_settings = None

    @property
    def default_ambassador_status(self):
        if self._crm_settings:
            return self._crm_settings.default_ambassador_status
        return None

    @property
    def default_message_type(self):
        if self._crm_settings:
            return self._crm_settings.default_message_type
        return None

    @property
    def default_message_status(self):
        if self._crm_settings:
            return self._crm_settings.default_message_status
        return None

    @property
    def delayed_sending_message_type(self):
        if self._crm_settings:
            return self._crm_settings.delayed_sending_message_type
        return None

    @property
    def default_delivery_status(self):
        if self._crm_settings:
            return self._crm_settings.default_delivery_status
        return None

    @property
    def default_report_status(self):
        if self._crm_settings:
            return self._crm_settings.default_report_status
        return None

    @property
    def default_report_type(self):
        if self._crm_settings:
            return self._crm_settings.default_report_type
        return None


crm_settings = CRMDefaultSettings()
