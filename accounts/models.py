# from .utils import generate_code
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse

from phonenumber_field.modelfields import PhoneNumberField


class Account(AbstractUser):
    first_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length = 50, unique = True)
    phone_number = PhoneNumberField()

    USER_ROLES = (
        ('CHAIRMAN', 'Chairman'),
        ('MD', 'Managing Director'),
        ('DAHR', 'Director Admin and Human Resource'),
        ('DMP', 'Director Marketing and Procurement'),
        ('DT', 'Director Technical'),
        ('AGENT', 'Agent'),
        ('DF', 'Director Finance'),
        ('CUSTOMER', 'Customer'),
    )
    role = models.CharField(max_length=50, choices = USER_ROLES)
    
    def get_full_name(self):
        #Return the first_name plus the last_name, with a space in between.
        if self.middle_name:
            full_name = '%s %s %s' %(self.first_name, self.last_name, self.middle_name)
        else:
            full_name = '%s %s' %(self.first_name, self.last_name)

        return full_name.strip()

    def get_short_name(self):
        #Return the short name for the user.
        return self.first_name

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username']


class Profile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to = "pictures/profile_pictures", default="backend/assets/images/users/no-picture.png")
    additional_phone_number = PhoneNumberField(unique=True, null=True, blank=True)

    # state = models.CharField(max_length = 30, choices = STATE_CHOICES, default = 'FCT')
    local_government_area = models.CharField(max_length = 50)
    town = models.CharField(max_length = 50)
    address = models.CharField(max_length = 200)
    
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'{self.user.username} - {self.user.email}'


def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)
        
post_save.connect(post_user_created_signal, sender=Account)


class FoundationCommittee(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    DESIGNATION_CHOICES = (
        ('CHAIRMAN', 'Chairman'),
        ('MD', 'Managing Director'),
        ('DAHR', 'Director Admin and Human Resource'),
        ('DMP', 'Director Marketing and Procurement'),
        ('DT', 'Director Technical'),
        ('AGENT', 'Agent'),
        ('DF', 'Director Finance'),
    )

    designation = models.CharField(max_length = 20, choices = DESIGNATION_CHOICES)
    words = models.CharField(max_length = 100)
    display_picture = models.ImageField(upload_to = 'pictures/foundation_committee/', help_text = "Width: 400px, Height: 400px")
    about = models.TextField()
    QUALIFICATION_CHOICES = (
        ('PhD', 'PhD.'),
        ('Masters', 'Masters'),
        ('Bachelors', 'Bachelors Degree/HND'),
        ('NCE', 'NCE'),
        ('Diploma', 'Diploma'),
        ('SSCE', 'SSCE'),
    )
    qualification = models.CharField(max_length = 200, choices = QUALIFICATION_CHOICES)
    experience = models.PositiveIntegerField(default=1)
    active = models.BooleanField(default = True)
    
    # member_id = models.CharField(max_length = 20, blank = True)

    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)

    # def save(self, *args, **kwargs):
    #     if self.member_id == '':
    #         self.member_id = generate_code()
        
    #     return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - {self.user.email}'

    def get_absolute_url(self):
        return reverse('accounts:committee-member-details', args=[(self.user.username)])
    
    class Meta:
        verbose_name = 'Foundation Committee'
        verbose_name_plural = 'Foundation Committee'