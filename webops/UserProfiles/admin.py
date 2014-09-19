from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.
from UserProfiles.models import Student, Interests

class StudentAdmin(admin.StackedInline):
	model = Student
	can_delete = False

class UserAdmin(UserAdmin):
	inlines = (StudentAdmin, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Interests)
