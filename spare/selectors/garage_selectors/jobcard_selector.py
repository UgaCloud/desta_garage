from spare.models.garage import (JobCard,Damage,JobCardItems,
JobCardService,Service,ServicePrice)

from spare.models.inventory import (Category,Item,Measurement,ItemMeasurement)


def get_services():
    return Service.objects.all()

def get_item():
    return Item.objects.all()

def get_measurement():
    return Measurement.objects.all()

def get_item_measurement():
    return Measurement.objects.all()

def get_service_price():
    return ServicePrice.objects.all()

def get_jobcards():
    return JobCard.objects.all()

def get_jobcard(jobcard_id):
    return JobCard.objects.get(pk=jobcard_id)

def get_jobcard_item_edit(jobcard_item_id):
    return JobCardItems.objects.get(pk=jobcard_item_id)

def get_jobcard_service_edit(jobcard_id):
    return JobCardService.objects.get(pk=jobcard_id)

# def get_net():
#     return total.objects.all()

def generate_auto_serialnumber():
    request_count = JobCard.objects.all().count()

    return f"{(request_count+1):04}"

def get_job_card_on_request(job_request):
    return JobCardItems.objects.filter(jobcard=job_request)

def get_job_card_on_request_item_inv(job_request):
    return JobCardItems.objects.filter(jobcard=job_request,status='approved')

def get_jobx_card_on_request(job_request):
    return JobCardService.objects.filter(jobcard=job_request)

def get_jobx_card_on_request_service_inv(job_request):
    return JobCardService.objects.filter(jobcard=job_request,status='approved')

def get_job_card_item_total(job_card):
    job_card_items = JobCardItems.objects.filter(jobcard=job_card)
    total = 0
    for item in job_card_items:
        total += item.total_item_cost
    return total

def get_job_card_service_total(job_card):
    job_card_service = JobCardService.objects.filter(jobcard=job_card)
    total = 0
    for service in job_card_service:
        total += service.total_cost
    return total