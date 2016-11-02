from django.contrib import admin
from Person.models import Person, Blog, Post
admin.site.register(Person)
admin.site.register(Blog)
admin.site.register(Post)
# Register your models here.
