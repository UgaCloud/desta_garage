from spare.models.settings import Currency, SiteSetting


def get_all_currencies():
    return Currency.objects.all()


def get_currency(currency_id):
    return Currency.objects.get(pk=currency_id)


def get_usd_currency():
    try:
        return Currency.objects.get(code="USD")
    except Currency.DoesNotExist:
        return None


def get_base_currency():
    site_setting = SiteSetting.load()
    country = site_setting.country
    if country == "UG":
        return get_ugx_currency()
    if country == "DRC":
        return get_cdf_currency()

def get_currency_from_code(code):
    try:
        return Currency.objects.get(code=code)
    except Currency.DoesNotExist:
        return None


def get_ugx_currency():
    try:
        return Currency.objects.get(code="UGX")
    except Currency.DoesNotExist:
        return None


def get_cdf_currency():
    try:
        return Currency.objects.get(code="CDF")
    except Currency.DoesNotExist:
        return None