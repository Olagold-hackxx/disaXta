from django.db.models.signals import m2m_changed
from django.db import models
from django.contrib.auth.models import AbstractUser
from django_extensions.db.models import TimeStampedModel
import bcrypt
import uuid


class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        null=True,  # Nullable field
        help_text=(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        error_messages={"unique": ("A user with that username already exists.")},
    )
    id = models.CharField(
        primary_key=True, default=uuid.uuid4, editable=False, max_length=150
    )

    profile_pic = models.ImageField(
        upload_to="profile_pic/", blank=True, null=True, max_length=300
    )

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    bio = models.TextField(max_length=160, blank=True, null=True)
    cover = models.ImageField(
        upload_to="covers/", blank=True, null=True, max_length=300
    )
    password = models.TextField(max_length=255, null=True)

    email = models.EmailField(unique=True)
    profession = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(
        max_length=15, blank=True, null=True
    )  # Fixed 'blank' syntax error
    last_location = models.CharField(max_length=255, blank=True, null=True)
    is_google_user = models.BooleanField(default=False, null=True)
    is_linkedin_user = models.BooleanField(default=False, null=True)
    is_github_user = models.BooleanField(default=False, null=True)
    is_verified = models.BooleanField(default=False, blank=True)
    is_twitter_user = models.BooleanField(default=False, null=True)
    is_facebook_user = models.BooleanField(default=False, null=True)
    is_active = models.BooleanField(default=True, null=True)
    # Timestamp fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS: list[str] = []
    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username

    def serialize(self):
        # Method to serialize user data for use in API responses
        return {
            "id": self.id,
            "username": self.username,
            "profile_pic": self.profile_pic.url,
            "first_name": self.first_name,
            "last_name": self.last_name,
        }


# Post model for user-generated posts
class Post(TimeStampedModel):
    # User who created the post
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="posts/%Y/%m/%d", blank=True, null=True)
    likers = models.ManyToManyField(User, related_name="liked_posts", blank=True)
    savers = models.ManyToManyField(User, related_name="saved_posts", blank=True)
    following = models.ManyToManyField(User, related_name="following", blank=True)
    category = models.CharField(
        max_length=20,
        choices=[
            ("community", "Community"),
            ("education", "Education"),
            ("reports", "Reports"),
        ],
        default="community",
    )
    location = models.CharField(max_length=255, blank=True, null=True)

    # Method to get the image URL
    def img_url(self):
        if self.content_image and hasattr(self.content_image, "url"):
            return self.content_image.url

    def like_post(self, user):
        self.likers.add(user)

    def unlike_post(self, user):
        self.likers.remove(user)

    def save_post(self, user):
        self.savers.add(user)

    def unsave_post(self, user):
        self.savers.remove(user)


# Comment model for comments on user posts
class Comment(TimeStampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="parent_comment",
    )
    subcomments = models.ManyToManyField("self", blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenters")
    image = models.ImageField(upload_to="comment/", blank=True, null=True)
    content = models.TextField(max_length=90)


class Follower(TimeStampedModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_followed"
    )
    followers = models.ManyToManyField(User, blank=True, related_name="followings")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}"
    
    class Meta:
        ordering = ["-created_at"]  # Order followers by creation date (latest first)



class CustomToken(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="token")
    is_valid = models.BooleanField(default=False)
    token = models.CharField(max_length=2048)
