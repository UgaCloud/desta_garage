from django.urls import path
import spare.views.items_views as item_views
from  django.conf.urls.static import  static
from  django.conf import settings


urlpatterns = [
    path('', item_views.login, name="login"),
    path('login', item_views.login, name="login"),
    
    path('index_page/', item_views.index_page, name='index_page'),
    
    path('ServiceRegistration', item_views.manage_service, name="serviceregister"),
    path('jobcardRegistration', item_views.manage_jobcard, name="jobregister"),
    path('ExpenseRegistration', item_views.manage_expense, name="expregister"),
    path('edit_jobcard/<int:jobcard_id>/',item_views.edit_jobcard, name='edit_job_card'),
    path('jobcard_detail/<int:jobcard_id>/',item_views.job_card_detail, name='job_card_detail'),
    path('manage_damages/<int:job_request_id>/',item_views.manage_damage, name='manage_damage'),
    path('print_pro_inv/<int:job_request_id>/',item_views.print_pro_invoice, name='print_pro_invoices'),
    path('print_inv/<int:job_request_id>/',item_views.print_invoice, name='print_invoice'),
    path('edit_jobcard_item/<int:jobcard_item_id>/',item_views.edit_job_item, name='edit_job_card_item'),
    path('edit_jobcard_service/<int:jobcard_id>/',item_views.edit_job_service, name='edit_job_card_service'),

]
# urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
