from spare.models.garage import Expenses


def get_expenses():
    return Expenses.objects.all()

def get_expense(exp_id):
    return Expenses.objects.get(pk=exp_id)