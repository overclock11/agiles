from django.db import models
from django.contrib.auth.models import User as AuthUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class User(models.Model):
    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE)
    photo = models.TextField()
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return "Usuario " + self.name + ", con email " + self.email

@receiver(post_save, sender=AuthUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        User.objects.create(user=instance)

@receiver(post_save, sender=AuthUser)
def save_user_profile(sender, instance, **kwargs):
    instance.user.save()

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Favourite(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return "Favorito del usuario " + self.user.name + " hacia la categoría " + self.category.name

class Promotion(models.Model):
    name = models.CharField(max_length=50)
    value = models.IntegerField()
    description = models.TextField()
    image = models.TextField()
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Commentary(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    promotion = models.ForeignKey(Promotion, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return "Comentario de usuario " + self.user + " en promoción " + self.promotion.name