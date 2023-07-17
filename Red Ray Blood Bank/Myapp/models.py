from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Blood_Bank(models.Model):
    branch_id=models.AutoField(primary_key=True)
    stock=models.ManyToManyField('Blood',related_name='stock',through='Inventory')
    branch_name=models.CharField(max_length=30,unique=True)
    location=models.CharField(max_length=50)

    def __str__(self):
        return self.branch_name

class Blood(models.Model):
    blood_group=models.CharField(max_length=3,primary_key=True)

    def __str__(self):
        return self.blood_group

class Inventory(models.Model):
    branch_name = models.ForeignKey(Blood_Bank, to_field='branch_name', on_delete=models.CASCADE,default='Gulshan Branch')
    blood_group=models.ForeignKey(Blood, on_delete=models.CASCADE)
    stock_quantity=models.IntegerField()
    stock_up_date=models.DateField()

    def __str__(self):
        return f"{self.branch_name}, {self.blood_group}"

class Donor(models.Model):
    donor_id=models.AutoField(primary_key=True)
    donates=models.ManyToManyField('Blood',related_name='donors',through='Donation')
    donor_name=models.CharField(max_length=30)
    donor_age=models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(60)])
    donor_gender=models.CharField(max_length=6)
    donor_blood_grp=models.CharField(max_length=3)
    donor_contact_no=models.CharField(max_length=11)

    def __str__(self):
        return self.donor_name

class Donation(models.Model):
    donor_id=models.ForeignKey(Donor, on_delete=models.CASCADE)
    blood_group=models.ForeignKey(Blood, on_delete=models.CASCADE)
    donation_date=models.DateField()
    quantity_donated_ml=models.IntegerField()
    
    def __str__(self):
        return f"{self.donor_id}"

class Recipient(models.Model):
    recipient_id=models.AutoField(primary_key=True)
    recievs=models.ManyToManyField('Blood',related_name='recipients',through='Recieving')
    recipient_name=models.CharField(max_length=30)
    recipient_contact_no=models.CharField(max_length=11)
    recipient_age=models.IntegerField(validators=[MinValueValidator(3), MaxValueValidator(3)])
    recipient_gender=models.CharField(max_length=1)
    recipient_blood_grp=models.CharField(max_length=3)
    
    def __str__(self):
        return self.recipient_name

class Recieving(models.Model):
    recipient_id=models.ForeignKey(Recipient, on_delete=models.CASCADE)
    blood_group=models.ForeignKey(Blood, on_delete=models.CASCADE)
    recieving_date=models.DateField()
    quantity_recieved_ml=models.IntegerField()

    def __str__(self):
        return f"{self.recipient_id}"

class Employee(models.Model):
    employee_id=models.AutoField(primary_key=True)
    works_at=models.ForeignKey(Blood_Bank, on_delete=models.CASCADE)
    employee_name=models.CharField(max_length=30)
    employee_contact_no=models.CharField(max_length=11)
    address=models.CharField(max_length=50)
    salary=models.IntegerField(validators=[MaxValueValidator(10000000)])
    job=models.CharField(max_length=20)

    def __str__(self):
        return self.employee_name

class Technician(Employee):
    specialization = models.CharField(max_length=30,default=None)
    technician_employee = models.OneToOneField(Employee, parent_link=True, on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.employee_name

class Nurse(Employee):
    degree = models.CharField(max_length=30,default=None)
    nurse_employee = models.OneToOneField(Employee, parent_link=True, on_delete=models.CASCADE,default=None)
    
    def __str__(self):
        return self.employee_name

class Shift_Incharge(Employee):
    qualification = models.CharField(max_length=30,default=None)
    shift_incharge_employee = models.OneToOneField(Employee, parent_link=True, on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.employee_name