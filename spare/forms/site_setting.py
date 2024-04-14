from spare.models.settings import SiteSetting
from django.forms import ModelForm


class SiteSettingForm(ModelForm):
    class Meta:
        model = SiteSetting
        fields = ("country","city", "address", "postal","website", "company_official_name", "mobile",
                  "office_phone_number1", "office_phone_number2", "logo", "app_name")
