from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

# from ems_auth.decorators import ems_login_required, hr_required
from spare.forms.site_setting import SiteSettingForm
from spare.models.settings import SiteSetting
from spare.selectors.settings import get_all_currencies, get_currency
from spare.services.settings_services import update_currency, create_currency


# @hr_required
# @ems_login_required
def settings_page(request):
    all_currencies = get_all_currencies()
    site_setting = SiteSetting.load()
    if request.method == 'POST':
        form = SiteSettingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Site settings saved')
            return HttpResponseRedirect(reverse('settings_page'))
        else:
            messages.error(request, 'Failed to save site settings')
            return HttpResponseRedirect(reverse('settings_page'))
    else:
        form = SiteSettingForm(instance=site_setting)
    context = {
        "currencies": all_currencies,
        "form": form
    }
    return render(request, 'settings/settings_page.html', context)


def add_currency(request):
    if request.POST:
        code = request.POST.get('code')
        desc = request.POST.get('desc')
        cost = request.POST.get('cost')

        create_currency(code, desc, cost)
        messages.success(request, 'Successfully created currency')

        return HttpResponseRedirect(reverse('settings_page'))
    messages.error(request, 'You sent a get request')
    return HttpResponseRedirect(reverse('settings_page'))


def edit_currency_page(request, currency_id):
    currency = get_currency(currency_id)
    if request.POST:
        code = request.POST.get('code')
        desc = request.POST.get('desc')
        cost = request.POST.get('cost')
        update_currency(currency, code, desc, cost)
        messages.success(request, 'Successfully updated currency')
        return HttpResponseRedirect(reverse('settings_page'))
    context = {
        "currency": currency
    }
    return render(request, 'settings/edit_currency.html', context)


def delete_currency(request, currency_id):
    currency = get_currency(currency_id)
    currency.delete()
    messages.success(request, "Successfully delete currency")
    return HttpResponseRedirect(reverse('settings_page'))
