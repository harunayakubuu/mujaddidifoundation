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
        ('Secretary', 'Secretary'),
        ('Education and Human Development', 'Education and Human Developmen'),
        ('Humanitarian', 'Humanitarian Services'),
        ('Dawa', 'Chairman'),
        ('Works and Masjid', 'Chairman'),
        ('Auditor', 'Auditor'),
        ('Media and Publicity', 'Media and Publicity'),
    )

    designation = models.CharField(max_length = 50, choices = DESIGNATION_CHOICES)
    words = models.CharField(max_length = 100)
    display_picture = models.ImageField(upload_to = 'pictures/foundation_committee/', help_text = "Width: 800px, Height: 900px")
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


class Event(models.Model):
    title = models.CharField(max_length = 50)
    description = models.TextField()
    event_location = models.CharField(max_length = 100)
    event_picture = models.ImageField(upload_to = 'pictures/events')
    event_date = models.DateField()
    event_start_time = models.TimeField()
    event_end_time = models.TimeField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'