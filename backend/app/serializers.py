from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from app.models import User, Post, Comment, CustomToken, Follower, Following

# Serializer for the User model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "profession",
            "phone_number",
            "last_location",
            "is_google_user",
            "is_redhat_user",
            "is_verified",
            "is_linkedin_user",
            "is_facebook_user",
            "is_active",
            "bio",
            "cover",
            "profile_pic",
            "created_at",
            "updated_at",
        )  # Serialize all fields of the User model


# Serializer for the Post model


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post

    def create(self, validated_data):
        user = self.context["request"].user
        return Post.objects.create(user, **validated_data)

# class PostSerializer(serializers.ModelSerializer):
#    comments_count = serializers.SerializerMethodField()
#    likers_count = serializers.SerializerMethodField()
#    savers_count = serializers.SerializerMethodField()

#    class Meta:
#        model = Post
#        fields = '__all__'

#    def get_comments_count(self, obj):
# Calculate and return the comments count for the specific post object
#        return obj.comments.count()
#    def get_likers_count(self, obj):
# Calculate and return the comments count for the specific post object
#        return obj.likers.count()
#    def get_savers_count(self, obj):
# Calculate and return the comments count for the specific post object
#        return obj.savers.count()


class CommentSerializer(serializers.ModelSerializer):
   # subcomments_count = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = "__all__"  # Serialize all fields of the Comment model

    # def get_subcomments_count(self, obj):
    # Calculate and return the comments count for the specific post object
    #    return obj.subcomments.count()


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment

    def create(self, validated_data):
        user = self.context["request"].user
        return Comment.objects.create(user, **validated_data)

# Serializer for the Follower model


class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = "__all__"
    

class FollowerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower

    def create(self, validated_data):
        user = self.context["request"].user
        return Follower.objects.create(user, **validated_data)



# Serializer for changing the user's password
class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Following
        fields = "__all__"  # Serialize all fields of the Follower model


class FollowingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Following

    def create(self, validated_data):
        user = self.context["request"].user
        return Following.objects.create(user, **validated_data)


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"



class SaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
   

class ChangePasswordSerializer(serializers.Serializer):
    # Serializer to change the user's password
    old_password = serializers.CharField(required=True)  # Old password field
    new_password = serializers.CharField(required=True)  # New password field


# Serializer for sending a password reset email


class ResetPasswordEmailSerializer(serializers.Serializer):
    # Serializer to send a password reset email
    # Email field for password reset request
    email = serializers.EmailField(required=True)


class CustomTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomToken
        fields = "__all__"
