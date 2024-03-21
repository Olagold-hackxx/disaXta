from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework import mixins, filters, serializers
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.conf import settings
from app.serializers import (
    UserSerializer,
    UserCreateSerializer,
    UserLoginSerializer,
    UserPasswordChangeSerializer,
    PasswordResetSerializer,
    PostSerializer,
    CommentSerializer,
    FollowerSerializer,
    SubCommentSerializer,
)
from django.core.exceptions import ValidationError

from app.models import User, CustomToken, Follower, Post, Comment
from app.serializers import UserSerializer
from app.tasks import send_activation_email, send_reset_password_email

User = get_user_model()


class UserViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == "login":
            return UserLoginSerializer
        elif self.action == "change_password":
            return UserPasswordChangeSerializer
        elif self.action in ["register", "create"]:
            return UserCreateSerializer
        elif self.action in ["reset_password"]:
            return PasswordResetSerializer
        return UserSerializer

    def get_queryset(self):
        return User.objects.filter(pk=self.request.user.pk)

    @action(methods=["post"], detail=False, permission_classes=(AllowAny,))
    def login(self, request):
        """Login user and return user data and token"""
        serializer = self.get_serializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=["post"], detail=False, permission_classes=(AllowAny,))
    def register(self, request):
        """Register user and return user data and token"""
        serializer = self.get_serializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # send_activation_email.apply_async(args=[user.id])
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return self.create(request)

    @action(methods=["post"], detail=False, permission_classes=(IsAuthenticated,))
    def change_password(self, request):
        """Change user password"""
        serializer = self.get_serializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(
        methods=["get", "put", "patch"],
        detail=False,
        permission_classes=(IsAuthenticated,),
    )
    def me(self, request):
        """Get & Update user data"""
        if request.method in ["PUT", "PATCH"]:
            return self.update(
                request, pk=request.user.pk, partial=request.method == "PATCH"
            )
        return self.retrieve(request, pk=request.user.pk)
        # return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self):
        """Return user object"""
        return self.request.user

    @action(["post"], detail=False)
    def reset_password(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.get_user()
        if user and not settings.TEST_MODE:
            send_reset_password_email.apply_async(kwargs={"user_pk": user.pk})
            # send_reset_password_email(user.pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostViewset(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = None
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = [
        "id",
    ]
    search_fields = filterset_fields

    # def get_queryset(self):
    #    return Post.objects.filter(user=self.request.user)

    # def get_serializer_class(self):
    #    return PostSerializer


class CommentViewset(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer
    pagination_class = None
    queryset = Comment.objects.all()
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = [
        "id",
    ]
    search_fields = filterset_fields

    # def get_queryset(self):
    #    return Comment.objects.filter(user=self.request.user)

    # def get_serializer_class(self):
    #    return CommentSerializer


class SubCommentViewset(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = SubCommentSerializer
    pagination_class = None
    queryset = Comment.objects.all()
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = [
        "id",
    ]
    search_fields = filterset_fields


class FollowerViewset(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = FollowerSerializer
    pagination_class = None
    queryset = Follower.objects.all()
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = [
        "id",
    ]
    search_fields = filterset_fields

    def get_queryset(self):
        user = self.request.user
        return user.followers.all()


class FollowingViewset(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = FollowerSerializer

    def perform_create(self, serializer):
        # Override the default create method to handle follow logic
        following_id = self.request.data.get("user")
        following = User.objects.get(pk=following_id)
        # import pdb; pdb.set_trace()

        # Check if the user is already following
        if following.followings.filter(user=self.request.user.pk).exists():
            raise serializers.ValidationError("You are already following this user")

        following = serializer.save(user=following)
        following.followers.add(self.request.user)

    def destroy(self, request, pk=None, *args, **kwargs):
        # Handle unfollow logic
        try:
            follower = Follower.objects.get(pk=pk, user=request.user)
            follower.delete()
            return Response({"message": "Unfollowed successfully"}, status=200)
        except Follower.DoesNotExist:
            return Response({"error": "Follower object not found"}, status=404)

    def get_queryset(self):
        user = self.request.user
        return user.user_followed


class LikeViewset(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    pagination_class = None
    queryset = Post.objects.all()
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = [
        "id",
    ]
    search_fields = filterset_fields


class SaveViewset(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    pagination_class = None
    queryset = Post.objects.all()
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = [
        "id",
    ]
    search_fields = filterset_fields

    # def get_queryset(self):
    #    return Post.objects.filter(user=self.request.user)

    # def get_serializer_class(self):
    #    return PostSerializer
