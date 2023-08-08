from django.db import models
from django.db.models.expressions import OrderBy
from django.urls import reverse


class Category(models.Model):

    category_name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    # image = models.ImageField(upload_to=None, max_length=None)


    class Meta:
        verbose_name = ("category")
        verbose_name_plural = ("categories")
        ordering = ("category_name",)

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"pk": self.pk})


class Item(models.Model):

    item_name = models.CharField(max_length=100)
    brand = models.CharField(max_length=25)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    units_in_stock = models.IntegerField()
    reorder_level = models.IntegerField(("Minimum Units to maintain in stock"))
    discontinued = models.BooleanField(("Yes means item is no longer available"), default=False)

    class Meta:
        verbose_name = ("Item")
        verbose_name_plural = ("Items")
        ordering = ("item_name",)
    
    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse("Items_detail", kwargs={"pk": self.pk})


class Measurement(models.Model):

    unit_name = models.CharField(("Measurement"), max_length=50)

    class Meta:
        verbose_name = ("Measurement")
        verbose_name_plural = ("Measurements")
        ordering = ("unit_name",)

    def __str__(self):
        return self.unit_name

    def get_absolute_url(self):
        return reverse("Measurement_detail", kwargs={"pk": self.pk})


class ItemMeasurement(models.Model):

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    measurement = models.ForeignKey(Measurement, on_delete=models.CASCADE)
    units_contained = models.IntegerField()
    unit_price = models.IntegerField()

    class Meta:
        verbose_name = ("ItemMeasurement")
        verbose_name_plural = ("ItemMeasurements")
        unique_together = ("item", "measurement")

    def __str__(self):
        # return f"{self.item} - {self.measurement} - {self.unit_price}"
        return f"{self.item} - {self.measurement}"

    def get_absolute_url(self):
        return reverse("ItemMeasurement_detail", kwargs={"pk": self.pk})

