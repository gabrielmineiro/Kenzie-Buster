from django.db import models

class GenderPet(models.TextChoices):
    MALE= "Male"
    FEMALE = "Female"
    NOTINFORMED = "Not Informed"

class Pet(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.FloatField()
    sex = models.CharField(max_length=20, choices=GenderPet.choices, default= GenderPet.NOTINFORMED)

    group =models.ForeignKey("groups.Group",on_delete=models.CASCADE, related_name="pets", null=True) 

    traits = models.ManyToManyField("traits.Trait", related_name="pets")
