from django.db import models


# Create your models here.

class Person(models.Model):
    first_name = models.CharField("First name", max_length=30)
    last_name = models.CharField("Last Name ", max_length=30)
    full_name = models.CharField("Full Name ", max_length=30, null=True)

    SHIRT_SIZES = (
        ('L', 'Large'),
        ('M', 'Medium'),
        ('S', 'Small')
    )
    shirt_sizes = models.CharField(max_length=1, choices=SHIRT_SIZES, null=True)

    def __str__(self):
        return self.full_name


class Musician(models.Model):
    first_name = models.CharField("First name ", max_length=30)
    last_name = models.CharField("Last Name", max_length=30)
    instruments = models.CharField("Instrument", max_length=30)

    def __str__(self):
        return self.first_name


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE, verbose_name="Artist Name")
    name = models.CharField("Album Name ", max_length=30)
    release_date = models.DateTimeField('date released')
    number_stars = models.IntegerField("stars ", default=0)

    def __str__(self):
        return self.name


class Runner(models.Model):
    medalType = models.TextChoices('Medal types ', 'GOLD SILVER BRONZE')
    name = models.CharField("Runner Name ", max_length=30)
    medal = models.CharField("The Medal ", blank=True, choices=medalType.choices, max_length=20)

    def __str__(self):
        return self.name


#
# class Fruit(models.Model):
#     name = models.CharField(max_length=200, primary_key=True)
#     # fruit_code = models.CharField(max_length=20, unique=True)


class Group(models.Model):
    group_name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through="Membership")

    def __str__(self):
        return self.group_name


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateTimeField()
    invited_reason = models.CharField(max_length=120)

    def __str__(self):
        return self.group


class Ox(models.Model):
    horn_length = models.IntegerField()

    class Meta:
        ordering = ['horn_length']
        verbose_name_plural = 'oxen'


# model inheritance
class CommonInfo(models.Model):
    name = models.CharField(max_length=120)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True
        ordering = ['name']


class Student(CommonInfo):
    home_group = models.CharField(max_length=45)

    def __str__(self):
        return self.name

    class Meta(CommonInfo.Meta):
        db_table = 'Student_info'


class Place(models.Model):
    name = models.CharField(max_length=90)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Resturant(Place):
    serves_hot_dog = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)
