from django.db import models


class FoundationCommittee(models.Model):
    name = models.CharField(max_length = 200)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length = 6, choices = GENDER_CHOICES)
    DESIGNATION_CHOICES = (
        ('CHAIRMAN', 'Chairman'),
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
        return self.name

    def get_absolute_url(self):
        return reverse('accounts:committee_member_details', args=[(self.user.username)])
    
    class Meta:
        verbose_name = 'Foundation Committee'
        verbose_name_plural = 'Foundation Committee'