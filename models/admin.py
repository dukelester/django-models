from django.contrib import admin
from .models import Person, Musician, Album, Runner, Group, Membership, Ox, Student, Place, Resturant

# Register your models here.

admin.site.register(Person)
admin.site.register(Musician)
admin.site.register(Album)
admin.site.register(Runner)
# admin.site.register(Fruit)
admin.site.register(Group)
admin.site.register(Membership)
admin.site.register(Ox)
admin.site.register(Student)

admin.site.register(Place)
admin.site.register(Resturant)
