from django.db import models
from django.db.models.expressions import OrderBy
from django.urls import reverse
from spare.models.inventory import Item, ItemMeasurement

class Service(models.Model):
    
    name = models.CharField(verbose_name="Service Name", max_length=50)    
    description = models.TextField()

    class Meta:
        verbose_name = ("Service")
        verbose_name_plural = ("Services")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Service_detail", kwargs={"pk": self.pk})

class ServicePrice(models.Model):
    
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="services")
    car_model = models.CharField(max_length=20)
    amount = models.IntegerField()

    class Meta:
        verbose_name = ("ServicePrice")
        verbose_name_plural = ("ServicePrices")

    def __str__(self):
        return f'{self.car_model} - {self.service} - {self.amount}'

    def get_absolute_url(self):
        return reverse("ServicePrice_detail", kwargs={"pk": self.pk})


class JobCard(models.Model):
    
    code = models.CharField(max_length=10)
    date_in = models.DateField()
    date_out = models.CharField(max_length=10,null=True,blank=True)
    plate_no = models.CharField(max_length=10,null=True, blank=True)
    car_model = models.CharField( max_length=20,null=True, blank=True)
    customer_name = models.CharField(max_length=30,null=True, blank=True)
    customer_contact = models.CharField(max_length=15,null=True, blank=True)
    customer_email = models.EmailField(max_length=254, null=True, blank=True)
    supervisor = models.CharField(max_length=50)
    year = models.CharField(max_length=50,null=True, blank=True)
    mileage_in = models.CharField(max_length=50,null=True, blank=True)
    mileage_out = models.CharField(max_length=50,null=True, blank=True)
    brought_in_by = models.CharField(max_length=50)
    Taken_out_by = models.CharField(max_length=50,null=True, blank=True)
    fuel_gauge_in=models.CharField(max_length=50,null=True, blank=True)
    fuel_gauge_out=models.CharField(max_length=50,null=True, blank=True)
    number_of_nuts = models.IntegerField()
    car_description=models.TextField()
    Aprov_TYPE_CHOICES=[
        ('Approved','Approved'),
        ('Not Approved','Not Approved')
    ]
    customer_approval = models.CharField(choices=Aprov_TYPE_CHOICES,default='Approved',max_length=50)
    DASH_TYPE_CHOICES=[
        ('ON','ON'),
        ('OFF','OFF')
    ]
    dash_light_on = models.CharField(choices=DASH_TYPE_CHOICES,default='ON',max_length=50)
    CAR_TYPE_CHOICES=[
        ('SALOON','SALOON'),
        ('STATION WAGON','STATION WAGON'),
        ('SUV','SUV'),
        ('PICKUP','PICKUP')
        
    ]
    car_type = models.CharField(choices= CAR_TYPE_CHOICES,default='SUV',max_length=50)
    items_in_car =models.TextField()

    class Meta:
        verbose_name = ("jobcard")
        verbose_name_plural = ("jobcards")

    def __str__(self):
        return f'{self.code} - {self.plate_no}'

    def get_absolute_url(self):
        return reverse("jobcard_detail", kwargs={"pk": self.pk})

   
class Expenses(models.Model):

    EXPENSE_STATUS_OPTIONS = [
        ('Car', 'Car'),
        ('Garage', 'Garage'),
        ('Others', 'Others')
        
    ]
    category=models.CharField(choices=EXPENSE_STATUS_OPTIONS,default='Car',max_length=50)
    item=models.CharField(max_length=100)

    quantity= models.IntegerField()
    unit_price=models.IntegerField()
    description = models.TextField(max_length=50,null=True,blank=True)
    date = models.DateField()


    class Meta:
        verbose_name = ("Expense")
        verbose_name_plural = ("Expenses")

    @property
    def total_cost(self):
        total_cost=self.unit_price*self.quantity
        return total_cost

    # def __str__(self):
    #     # return f'{self.jobcard.plate_no} - {self.name} - {self.jobcard.code}'
    #     return f'{self.jobcard.plate_no} - {self.name} - {self.jobcard.code}'

    def get_absolute_url(self):
        return reverse("Expense_detail", kwargs={"pk": self.pk})


class Damage(models.Model):
    jobcard = models.ForeignKey(JobCard, on_delete=models.CASCADE, related_name="Car_Code")
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=50)
    date_in = models.DateField(auto_now=True)
    quantity= models.IntegerField()
    unit_price=models.IntegerField()
    photo=models.ImageField(upload_to='pic')
    

    class Meta:
        verbose_name = ("Damage")
        verbose_name_plural = ("Damages")

    @property
    def total_cost(self):
        total_cost=self.unit_price*self.quantity
        return total_cost

    def __str__(self):
        # return f'{self.jobcard.plate_no} - {self.name} - {self.jobcard.code}'
        return f'{self.jobcard.plate_no} - {self.name} - {self.jobcard.code}'

    def get_absolute_url(self):
        return reverse("jobcard_detail", kwargs={"pk": self.pk})


class JobCardItems(models.Model):

    JOB_STATUS_OPTIONS = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('cancelled', 'Cancelled'),
    ]

    date=models.DateField(auto_now=True)
    
    
    # items = models.ForeignKey(
    #     ItemMeasurement, 
    #     on_delete=models.CASCADE,
    #     related_name = 'items_mesurement'
    # )
    items = models.CharField(max_length=100)    
    jobcard = models.ForeignKey(
        JobCard,
        on_delete=models.CASCADE,
        related_name='job_card_items'
    )
    item_price = models.IntegerField()
    
    quantity = models.IntegerField()
    description = models.TextField(max_length=50)
    status=models.CharField(choices=JOB_STATUS_OPTIONS,default='pending',max_length=50)

    class Meta:
        verbose_name = ("JobCardItem")
        verbose_name_plural = ("JobCardItems")

        

    # def __str__(self):
    #     return self.jobcard.code

    def get_absolute_url(self):
        return reverse("JobCardItem_detail", kwargs={"pk": self.pk})

    @property
    def total_item_cost(self):
        total_item_cost = self.item_price * self.quantity
        return total_item_cost

class JobCardService(models.Model):

    STATUS_OPTIONS = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('cancelled', 'Cancelled'),
    ]

    date=models.DateField(auto_now=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="service")
    service_price = models.ForeignKey(
        ServicePrice, 
        on_delete=models.CASCADE,
        related_name = 'job_card_service'
        )
    
    
    
    jobcard = models.ForeignKey(
        JobCard,
        on_delete=models.CASCADE,
        
    )
    service_price_final = models.IntegerField()
    quantity = models.IntegerField()
    status=models.CharField(choices=STATUS_OPTIONS,default='pending',max_length=50)

    class Meta:
        verbose_name = ("JobCardService")
        verbose_name_plural = ("JobCardServices")

    def __str__(self):
        return self.jobcard.code

    def get_absolute_url(self):
        return reverse("JobCardService_detail", kwargs={"pk": self.pk})

    @property
    def total_cost(self):
        total_cost = self.service_price_final *self.quantity
        return total_cost


