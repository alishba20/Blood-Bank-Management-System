from django.contrib import admin
from .models import Donor, Recipient, Blood, Blood_Bank, Employee, Shift_Incharge, Technician, Nurse, Donation, Inventory,Recieving

# Register your models here.
admin.site.register(Donor)
admin.site.register(Recipient)
admin.site.register(Blood)
admin.site.register(Blood_Bank)
admin.site.register(Employee)
admin.site.register(Shift_Incharge)
admin.site.register(Technician)
admin.site.register(Nurse)
admin.site.register(Donation)
admin.site.register(Inventory)
admin.site.register(Recieving)
