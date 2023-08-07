from django.contrib import admin
from django.db import models
from spare.models.garage import Service,ServicePrice,JobCard,JobCardItems,Damage,JobCardService
from spare.models.inventory import Category,Item,Measurement,ItemMeasurement

# @admin.register(Service)
# # admin.site.register(Service)
# class ServiceAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description')

# @admin.register(ServicePrice)
# class ServicePrice(admin.ModelAdmin):
#     list_display = ('service', 'car_model', 'amount')


admin.site.register(JobCardService)
admin.site.register(ServicePrice)
admin.site.register(Damage)
admin.site.register(Service)
admin.site.register(JobCard)
admin.site.register(JobCardItems)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Measurement)
admin.site.register(ItemMeasurement)

admin.site.site_header = "Desta Auto Garage"
admin.site.site_title = "Desta Auto Garage"
admin.site.index_title = "Desta Auto Garage"




# Register your models here.
