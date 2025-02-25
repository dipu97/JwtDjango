from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import  gettext_lazy as _
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User
# Register your models here.

class UserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    model = User
    list_display = ['email', 'first_name', 'last_name','is_active', 'is_staff','date_joined']
    search_fields = ['email', 'username']
    ordering = ['email']
    list_display_links = ['email']
    list_filter = ['first_name', 'last_name','email','is_active']
    list_editable = ['first_name', 'last_name', 'is_active']
    search_fields=['email', 'username']
    fieldsets = (
        (_('Login Credentials'), {'fields': ('email', 'password')},
         ),
        (_('Personal Information'), {'fields': ('first_name', 'last_name',)},
         ),
        (_('Permissions and Groups'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups','user_permissions')},
         ),
        (_('Important Dates'), {'fields': ('last_login',)},
         ),

    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name','last_name', 'password1', 'password2','is_active','is_staff'),
        },),
    )

admin.site.register(User, UserAdmin)
