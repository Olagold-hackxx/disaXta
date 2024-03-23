from django.contrib import admin

# from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group
from unfold.admin import ModelAdmin
from app.models import User, Post, Follower, Comment, Token


@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "username",
        "last_name",
        "bio",
        "cover",
        "password",
        "email",
        "profession",
        "phone_number",
        "last_location",
        "is_google_user",
        "is_linkedin_user",
        "is_verified",
        "is_twitter_user",
        "is_facebook_user",
    )
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "bio",
                    "cover",
                    "profession",
                    "phone_number",
                    "last_location",
                    "is_google_user",
                    "is_linkedin_user",
                    "is_verified",
                    "is_twitter_user",
                    "is_facebook_user",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    # "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password", "username"),
            },
        ),
    )
    list_display = ("id", "email", "first_name", "last_name", "is_staff")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("username", "first_name", "last_name", "email")
    ordering = ("email",)


@admin.register(Token)
class TokenAdmin(ModelAdmin):
    list_filter = ("user",)
    search_fields = ("user",)


@admin.register(Post)
class PostAdmin(ModelAdmin):
    list_display = ("id", "content", "image", "user", "category", "location")
    list_filter = ("user",)
    search_fields = ("id",)


@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    list_display = ("id", "content", "image", "post_id", "parent_id")
    search_fields = ("id",)


@admin.register(Follower)
class FollowerAdmin(ModelAdmin):
    list_display = ("id", "user")
    search_fields = ("user",)


admin.site.unregister(Group)
