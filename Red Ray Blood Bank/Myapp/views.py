from django.shortcuts import render,redirect
from . models import Inventory,Donor,Donation,Blood,Blood_Bank,Recipient,Recieving
import datetime
from .decorators import nurse_required, shift_incharge_required


# Create your views here.
def home(request):
    return render(request,"home.html")

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the entered credentials match a nurse's username and password
        if username == 'nurse' and password == 'nursepassword':
            request.session['role'] = 'nurse'
            return redirect('nurse')  # Redirect to the nurse page

        # Check if the entered credentials match a shift in-charge's username and password
        elif username == 'shiftincharge' and password == 'shiftinchargepassword':
            request.session['role'] = 'shiftincharge'
            return redirect('shiftIncharge')  # Redirect to the shift in-charge page

        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})

    return render(request, 'login.html')

def contact(request):
    return render(request,"contact.html")

@nurse_required
def nurse(request):
    if request.method== 'POST':
        name=request.POST['name']
        gender=request.POST['gender']
        blood_group=request.POST['bloodGroup']
        contact_no=request.POST['contact']
        age=request.POST['age']
        branch=request.POST['branch']
        new_donor=Donor.objects.create(donor_name=name,donor_age=age,donor_gender=gender,donor_blood_grp=blood_group,donor_contact_no=contact_no)
        new_donor.save()

        blood = Blood.objects.get(blood_group=blood_group)

        branch = Blood_Bank.objects.get(branch_name=branch)
        
        donation = Donation.objects.create(donor_id=new_donor,blood_group=blood,donation_date=datetime.date.today(),quantity_donated_ml=470)
        
        try:
            inventory = Inventory.objects.get(branch_name=branch, blood_group=blood)
            inventory.stock_quantity += 470
            inventory.save()
        except Inventory.DoesNotExist:
            inventory = Inventory.objects.create(branch_name=branch,blood_group=blood,stock_quantity=470,stock_up_date=datetime.date.today())

    return render(request,"nurse.html")

@shift_incharge_required
def shiftIncharge(request):
    if request.method== 'POST':
        name=request.POST['name']
        gender=request.POST['gender']
        blood_group=request.POST['bloodGroup']
        contact_no=request.POST['contact']
        age=request.POST['age']
        branch=request.POST['branch']
        new_recipient=Recipient.objects.create(recipient_name=name,recipient_age=age,recipient_gender=gender,recipient_blood_grp=blood_group,recipient_contact_no=contact_no)
        new_recipient.save()

        blood = Blood.objects.get(blood_group=blood_group)

        branch = Blood_Bank.objects.get(branch_name=branch)
        
        recieving = Recieving.objects.create(recipient_id=new_recipient,blood_group=blood,recieving_date=datetime.date.today(),quantity_recieved_ml=470)
        
        try:
            inventory = Inventory.objects.get(branch_name=branch, blood_group=blood)
            inventory.stock_quantity -= 470
            inventory.save()
        except Inventory.DoesNotExist:
            inventory = Inventory.objects.create(branch_name=branch,blood_group=blood,stock_quantity=470,stock_up_date=datetime.date.today())

    return render(request,"shiftIncharge.html")
