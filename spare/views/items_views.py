from django.shortcuts import render,reverse,redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from spare.utils import render_to_pdf
from django.http import HttpResponse
from spare.render import Render

from django.template.defaulttags import register

from django.contrib.auth.models import User,auth,Group
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.admin.views.decorators import staff_member_required







from spare.selectors.garage_selectors.jobcard_selector import  (get_jobcards,
generate_auto_serialnumber,get_jobcard,get_services,get_service_price,
get_job_card_on_request,get_jobx_card_on_request,get_job_card_on_request_item_inv,
get_jobcard_item_edit,get_jobcard_service_edit,get_jobx_card_on_request_service_inv, 
get_job_card_item_total, get_job_card_service_total)
from spare.selectors.garage_selectors.expense_selector import(get_expense,get_expenses)

from spare.forms.garage_forms.jobcard_form import JobcardForm
from spare.forms.garage_forms.service_form import ServiceForm
from spare.forms.garage_forms.damage_form import DamageForm
from spare.forms.garage_forms.job_item_form import JobItemForm
from spare.forms.garage_forms.job_service_form import JobServiceForm
from spare.forms.garage_forms.expense_form import ExpenseForm





def index_page_view(request):
    return render(request, "login.html")

def index_page(request):
    return render(request, "index.html")



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index_page')
        else:
            messages.info(request,'Invalid Login Credentials')
            return redirect('login')
    
    else:
        return render (request,'login.html') 


def manage_jobcard(request):
    
    auto_no = generate_auto_serialnumber()
    request_serial_number = auto_no
    card_form = JobcardForm(initial={"code": request_serial_number})
    get_cards = get_jobcards()

    if request.method == "POST":
        card_form=JobcardForm(request.POST,request.FILES)
        if card_form.is_valid():
            card_form.save()
            messages.success(request,'JobCard Record saved Successfully!')
        else:
            messages.WARNING(request,'Operation Not Successfull')
        return HttpResponseRedirect(reverse(manage_jobcard))

        # return HttpResponseRedirect(reverse(manage_jobcard(request)))

    context = {
         "card_form": card_form,
        "get_cards": get_cards
    }
    return render(request, "jobcard/jobcard_registration.html", context)

def manage_service(request):

    service_form = ServiceForm()
    get_service = get_services()

    if request.method == "POST":
        service_form=ServiceForm(request.POST,request.FILES)
        if service_form.is_valid():
            service_form.save()
            messages.success(request,'Service Record saved Successfully!')
        else:
            messages.WARNING(request,'Operation Not Successfull')
        return HttpResponseRedirect(reverse(manage_service))

        # return HttpResponseRedirect(reverse(manage_jobcard(request)))

    context = {
         "service_form":service_form,
        "get_services":get_service
    }
    return render(request, "jobcard/service_registration.html", context)


def manage_expense(request):

    expense_form = ExpenseForm()
    get_expense = get_expenses()

    if request.method == "POST":
        expense_form=ExpenseForm(request.POST,request.FILES)
        if expense_form.is_valid():
            expense_form.save()
            messages.success(request,'Expense Record saved Successfully!')
        else:
            messages.WARNING(request,'Operation Not Successfull')
        return HttpResponseRedirect(reverse(manage_expense))

        # return HttpResponseRedirect(reverse(manage_jobcard(request)))

    context = {
         "expense_form":expense_form,
        "get_expenses":get_expenses
    }
    return render(request, "jobcard/manage_expenses.html", context)

def edit_jobcard(request,jobcard_id):
    get_card = get_jobcard(jobcard_id)
    card_form = JobcardForm(instance=get_card)

    if request.method == "POST":
        card_form=JobcardForm(request.POST,request.FILES,instance=get_card)
        if card_form.is_valid():
            card_form.save()
            messages.success(request,'JobCard Changes saved Successfully!')
        else:
            messages.WARNING(request,'Operation Not Successfull')
        return HttpResponseRedirect(reverse(manage_jobcard))

        # return HttpResponseRedirect(reverse(manage_jobcard(request)))

    context = {
         "card_form": card_form,
        "get_card": get_card
    }
    return render(request, "jobcard/jobcard_edit.html", context)

def job_card_detail(request, jobcard_id):
    job_card_request = get_jobcard(jobcard_id)

    context = {
       
        "job_card_request": job_card_request
    }
    # pdf = render_to_pdf('enforcement/reports/field_enforcment_detail_report.html', context)
    # return HttpResponse(pdf, content_type='application/pdf')
    return render(request, "jobcard/jobcard_detail.html", context)

def manage_damage(request,job_request_id):
    job_request = get_jobcard(job_request_id)
    
    job_item_form = JobItemForm(initial={"jobcard":job_request})
    job_item_request = get_job_card_on_request(job_request)  
    
    item_service_form = JobServiceForm(initial={"jobcard":job_request})
    item_in_service = get_jobx_card_on_request(job_request)

    if request.method == "POST":
        job_item_form=JobItemForm(request.POST,request.FILES)
        item_service_form=JobServiceForm(request.POST,request.FILES)
        if job_item_form.is_valid():
            job_item_form.save()
            messages.success(request,'Job Item Record saved Successfully!')
        # else:

        elif item_service_form.is_valid():
            item_service_form.save()
            messages.success(request,'Item Service Record saved Successfully!')
        else:
            messages.WARNING(request,'Operation Not Successfull')
        return HttpResponseRedirect(reverse(manage_damage,args=[job_request_id]))

        

    item_total = get_job_card_item_total(job_request)
    service_total = get_job_card_service_total(job_request)

    total = item_total + service_total

    context = {
        "job_item_f":job_item_form,
        "job_item":job_item_request,
        "service_form":item_service_form,
        "service_items":item_in_service,
        "job_request":job_request,
        "total": total,
    }
    return render(request,"jobcard/manage_damages.html", context)

def edit_job_item(request,jobcard_item_id):
    job_card_item = get_jobcard_item_edit(jobcard_item_id)
    job_item_form = JobItemForm(instance=job_card_item)
    

    if request.method == "POST":
        job_item_form=JobItemForm(request.POST,request.FILES,instance = job_card_item)
        if job_item_form.is_valid():
            job_item_form.save()
            messages.success(request,'JobCard Changes saved Successfully!')
        else:
            messages.WARNING(request,'Operation Not Successfull')
        return HttpResponseRedirect(reverse(manage_damage,args=[job_card_item.jobcard.id]))

        # return HttpResponseRedirect(reverse(manage_jobcard(request)))

    context = {
        "job_item_form":job_item_form,
        "job_card_item":job_card_item
    }
    return render(request, "jobcard/job_card_item_edit.html", context)
    
def edit_job_service(request,jobcard_id):
    job_requests = get_jobcard_service_edit(jobcard_id)
    job_service_formx = JobServiceForm(instance=job_requests)
    

    if request.method == "POST":
        job_service_formx = JobServiceForm(request.POST,request.FILES,instance = job_requests)
        if job_service_formx.is_valid():
            job_service_formx.save()
            messages.success(request,'JobService Changes saved Successfully!')
        else:
            messages.WARNING(request,'Operation Not Successfull')
        return HttpResponseRedirect(reverse(manage_damage,args=[job_requests.jobcard.id]))

        # return HttpResponseRedirect(reverse(manage_jobcard(request)))

    context = {
         "job_service_formx":job_service_formx,
        "job_requests":job_requests
    }
    return render(request, "jobcard/job_card_service_edit.html", context)

def print_pro_invoice(request,job_request_id):

    job_request = get_jobcard(job_request_id)
    job_item_request = get_job_card_on_request(job_request)  
    item_in_service = get_jobx_card_on_request(job_request)


    item_total = get_job_card_item_total(job_request)
    service_total = get_job_card_service_total(job_request)

    total = item_total + service_total


   

    context = {
        
        "job_item":job_item_request,
        "service_items":item_in_service,
        "job_request":job_request,
        "total": total
    }

   
    return render(request,"report/pro_invoice.html", context)

def print_invoice(request,job_request_id):

    job_request = get_jobcard(job_request_id)
    job_item_request = get_job_card_on_request_item_inv(job_request)  
    item_in_service = get_jobx_card_on_request_service_inv(job_request)


    item_total = get_job_card_item_total(job_request)
    service_total = get_job_card_service_total(job_request)

    total = item_total + service_total

    context = {
        
        "job_item":job_item_request,
        "service_items":item_in_service,
        "job_request":job_request,
        "total": total
    }

   
    return render(request,"report/invoice.html", context)

@register.filter(name='has_group')
def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False

    def manage_item_in_car(request,itemcar_request_id):
        job_request = get_jobcard(itemcar_request_id)
    
        # auto_no = generate_auto_serialnumber()
        # request_serial_number = auto_no
        item_in_car_form = ItemInCarForm(initial={"jobcard":job_request})
        item_in_car = get_jobx_card_on_request(job_request)
        # get_dmgs = get_damages()

        if request.method == "POST":
            item_in_car_form=ItemInCarForm(request.POST,request.FILES)
            if item_in_car_form.is_valid():
                item_in_car_form.save()
                messages.success(request,'Items Record saved Successfully!')
            else:
                messages.WARNING(request,'Operation Not Successfull')
            return HttpResponseRedirect(reverse(manage_damage,args=[job_request_id]))

            # return HttpResponseRedirect(reverse(manage_jobcard(request)))

        context = {
            "car":item_in_car_form,
            "item_car":item_in_car
        }
        return render(request,"jobcard/manage_damages.html", context)


    