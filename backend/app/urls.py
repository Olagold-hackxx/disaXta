from rest_framework.routers import DefaultRouter
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from django.urls import path
from app import views

urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("doc/", SpectacularRedocView.as_view(url_name="schema"), name="schema-redoc"),
    path(
        "swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="schema-swagger",
    ),
]
router = DefaultRouter()

router.register("user", views.UserViewSet, basename="users")
router.register("post", views.PostViewset, basename="posts")
router.register("followers", views.FollowerViewset, basename="followers")
router.register("following", views.FollowingViewset, basename="followings")
router.register("comment", views.CommentViewset, basename="comments")
router.register("subcomment", views.SubCommentViewset, basename="subcomments")
router.register("like", views.LikeViewset, basename="likes")
router.register("save", views.SaveViewset, basename="save")

urlpatterns += router.urls



