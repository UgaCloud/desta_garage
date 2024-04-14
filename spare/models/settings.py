from django.db import models

from AbstractModels.singleton import SingletonModel


# Create your models here.


class Currency(models.Model):
    code = models.CharField(max_length=10, unique=True, default="UGX")
    desc = models.CharField(max_length=20, default="Ugandan Shillings")
    cost = models.CharField(max_length=20, default="1")

    def __str__(self):
        return self.code


class SiteSetting(SingletonModel):
    COUNTRIES = (
        ("UG", "Uganda"),
        ("KE", "Kenya"),
        ("TZ", "Tanzania"),
        ("RD", "Rwanda"),
        ("BD", "Burundi"),
        ("SD", "South Sudan")
    )
    country = models.CharField(max_length=40, choices=COUNTRIES, default="Uganda")
    city = models.CharField(max_length=40, default="Kampala")
    address = models.CharField(max_length=50, default="Kansanga Plot 10, Gaba Road")
    postal = models.CharField(max_length=50, default="P. O. Box 104747 Kampala,Uganda")
    website = models.CharField(max_length=50, default="www.uga-cloud.com")
    company_official_name = models.CharField(max_length=50, default="UGACLOUD SERVICES (U) LTD")
    mobile = models.CharField(max_length=20, blank=True, null=True)
    office_phone_number1 = models.CharField(max_length=20, blank=True, null=True)
    office_phone_number2 = models.CharField(max_length=40, blank=True, null=True)
    logo = models.ImageField(upload_to="logo", height_field=None, width_field=None, max_length=None)
    app_name = models.CharField(max_length=20, default="UGACloud Bakozi")

