from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from toDoApp.profiles.forms import ToDoUserChangeForm, ToDoUserCreationForm
from toDoApp.profiles.models import ToDoProfile, ToDoUser
from django.contrib.auth import get_user_model


UserModel = get_user_model()


class ProfileInline(admin.StackedInline):
    model = ToDoProfile
    can_delete = False
    fields = ("age", "tasks", )


@admin.register(UserModel)
class UserModelAdmin(UserAdmin):
    form = ToDoUserChangeForm
    add_form = ToDoUserCreationForm
    inlines = (ProfileInline, )

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", )}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )