from django.db import models

# Create your models here.


# class User(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=254)
#     zip = models.IntegerField(max_length=5)
#     evacPlan = models.OneToOneField('EvacPlan')
#
#     def __unicode__(self):
#         return self.name


class EvacPlan(models.Model):

    pass

    class Meta:
        verbose_name = "Evac Plan"
        verbose_name_plural = "Evac Plans"

class ToTake(models.Model):
    evacPlan = models.OneToOneField('EvacPlan')

    class Meta:
        verbose_name = "To Take"
        verbose_name_plural = "To Takes"


class Person(models.Model):
    GENDER = (
        ('Male', 'M'),
        ('Female', 'F'),
    )
    parent = models.ForeignKey('ToTake')
    name = models.CharField(max_length=50, blank=True, null=True)
    birthMonth = models.IntegerField(max_length=2, blank=True, null=True)
    birthYear = models.IntegerField(max_length=4, blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER, blank=True, null=True)
    relationship = models.CharField(max_length=50, blank=True, null=True)
    special_conditions = models.ManyToManyField('SpecialConditions')
    supplies = models.ManyToManyField('Supply', blank=True, null=True)

    def __unicode__(self):
        if self.name is None:
            return ""
        return self.name

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "People"


class SpecialConditions(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
        return self.name


class Pet(models.Model):
    parent = models.ForeignKey('ToTake')
    name = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    count = models.CharField(max_length=3, blank=True, null=True)
    breed = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField(max_length=3, blank=True, null=True)
    weight = models.IntegerField(max_length=3, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    preference = models.CharField(max_length=50, blank=True, null=True)
    supplies = models.ManyToManyField('Supply', blank=True, null=True)

    def __unicode__(self):
        if self.name is None:
            return ""
        return self.name


    class Meta:
        verbose_name = "Pet"
        verbose_name_plural = "Pets"


class Route(models.Model):
    destinations = models.ManyToManyField('Stop')
    startPoint = models.CharField(max_length=200)
    transportMode = models.CharField(max_length=50)
    route = models.OneToOneField('EvacPlan')

    class Meta:
        verbose_name = "Route"
        verbose_name_plural = "Routes"


class Stop(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.IntegerField(max_length=10)
    type = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Stop"
        verbose_name_plural = "Stops"


class Supply(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Supply"
        verbose_name_plural = "Supplies"


class Document(Supply):
    pass

    class Meta:
        verbose_name = "Document"
        verbose_name_plural = "Documents"


class TechAndValuable(Supply):
    pass

    class Meta:
        verbose_name = "Tech And Valuable"
        verbose_name_plural = "Tech And Valuables"


class TravelTool(Supply):
    pass

    class Meta:
        verbose_name = "Travel Tool"
        verbose_name_plural = "Travel Tools"


class EmergencySupply(Supply):
    pass

    class Meta:
        verbose_name = "Emergency Supply"
        verbose_name_plural = "Emergency Supplies"

class MapRoute(models.Model):
    name = models.CharField(max_length=200)
    origin = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    waypoints = models.TextField()
    waypoint_names = models.TextField()
    travel_mode = models.CharField(max_length=200)


