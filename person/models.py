from django.db import models

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]

MARITAL_CHOICES = [
    ('Single', 'Single'),
    ('Married', 'Married'),
    ('Divorced', 'Divorced'),
]

BLOOD_GROUP_CHOICES = [
    ('A+', 'A+'), ('A-', 'A-'),
    ('B+', 'B+'), ('B-', 'B-'),
    ('AB+', 'AB+'), ('AB-', 'AB-'),
    ('O+', 'O+'), ('O-', 'O-'),
]

class Advocate(models.Model):
    # Basic Info
    advocate_type = models.CharField(max_length=50, blank=True)
    name_english = models.CharField(max_length=100)
    name_bengali = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='advocate_photos/', blank=True, null=True)
    father_name = models.CharField(max_length=100, blank=True)
    mother_name = models.CharField(max_length=100, blank=True)
    husband_or_wife_name = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    marital_status = models.CharField(max_length=10, choices=MARITAL_CHOICES, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    nid_number = models.CharField(max_length=20, blank=True)
    blood_group = models.CharField(max_length=5, choices=BLOOD_GROUP_CHOICES, blank=True)
    religion = models.CharField(max_length=50, blank=True)

    # Address Info
    current_address = models.TextField(blank=True)
    permanent_address = models.TextField(blank=True)

    # Contact
    phone = models.CharField(max_length=15, blank=True, null= True)
    email = models.EmailField(blank=True, null = True)

    # Education & Bar Info
    education = models.CharField(max_length=200, blank=True)
    bar_registration_number = models.CharField(max_length=50, blank=True)
    enrollment_date_As_lawyer = models.DateField(blank=True, null=True)
    enrollment_date_As_member = models.DateField(blank=True, null=True)
    

    # Court Info
    is_a_ex_employee = models.BooleanField(default=False)
    employment_details = models.TextField(blank=True)
    is_receiing_pension = models.BooleanField(default=False)
    pension_details = models.TextField(blank=True)
    is_from_another_bar = models.BooleanField(default=False)
    practicing_court_name = models.CharField(max_length=100, blank=True)

    # Status
    status = models.CharField(max_length=30, blank=True, null=True)
    retirement_date = models.DateField(blank=True, null=True)
    death_date = models.DateField(blank=True, null=True)

    # Remarks
    remarks = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name_english} ({self.name_bengali})"



class Child(models.Model):
    advocate = models.ForeignKey(Advocate, related_name='children', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
  
    def __str__(self):
        return f"{self.name} ({self.gender})"
    

class Nominee(models.Model):
    advocate = models.ForeignKey(Advocate, related_name='nominees', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.TextField(blank=True)
    relationship = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    birth_year = models.PositiveIntegerField(blank=True, null=True)
    nid = models.CharField(max_length=20, blank=True)
    birth_certificate = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.name} ({self.relationship})"

    

    
class Building(models.Model):
    building_name = models.CharField(max_length=100)
    institute = models.CharField(max_length=100)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return self.building_name
    

class FormModel(models.Model):
    form_name = models.CharField(max_length=100)
    form_rate = models.DecimalField(max_digits=10, decimal_places=2)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return self.form_name
    

class Renter(models.Model):
    renter_name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    from_date = models.DateField(blank=True, null= True)
    to_date = models.DateField(blank=True, null= True)
    category = models.CharField(max_length=100)
    remarks = models.TextField(blank=True)
    building = models.ForeignKey('Building', on_delete=models.CASCADE, related_name='renters')
    floor_no = models.CharField(max_length=10)
    room_no = models.CharField(max_length=10)
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    security_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null= True)

    def __str__(self):
        return self.renter_name
    

class Bank(models.Model):
    bank_name = models.CharField(max_length=100)
    address = models.TextField()
    branch_name = models.CharField(max_length=100)
    account_category = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.bank_name} - {self.branch_name}"
    


class ExpanseCategory(models.Model):
    category = models.CharField(max_length=100)


class IncomeCategory(models.Model):
    category = models.CharField(max_length=100)


class PhotoGallery(models.Model):
    image = models.ImageField(upload_to='img/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    caption=models.TextField(blank=True, null=True)
    TYPE_CHOICES = [
        ("general", "Photos"),
        ("paper-cut", "Paper Cutting"),
    ]
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default="general")

    def __str__(self):
        return f"{self.type} - {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
    


class PositionList(models.Model):
    position = models.CharField(max_length=100, blank=True, null=True)




class CommitteeMember(models.Model):
    year = models.IntegerField()
    bar_registration_number = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    committee_position = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.committee_position}) - {self.year}"



