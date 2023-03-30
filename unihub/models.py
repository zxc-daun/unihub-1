from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class ClubCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')

    def __str__(self):
        return self.name


class Club(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    description = models.TextField()
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    instagram = models.URLField()
    category = models.ForeignKey(ClubCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='club_images')
    constitution = models.FileField(upload_to='club_constitutions')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('club_detail', args=[self.slug])


class ClubEvent(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ClubMember(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    position = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ClubMeeting(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return str(self.date)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_club_creator = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


class UserClub(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    is_following = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user) + ' - ' + str(self.club)
