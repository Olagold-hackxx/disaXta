from rest_framework.routers import DefaultRouter

from app import views

app_name = "disaXta"

router = DefaultRouter()

router.register(r"user", views.UserViewSet, basename="users")
router.register("post", views.PostViewset, basename="posts")
router.register("followers", views.FollowerViewset, basename="followers")
router.register("following", views.FollowingViewset, basename="followings")
router.register("comment", views.CommentViewset, basename="comments")
router.register("like", views.LikeViewset, basename="likes")
router.register("save", views.SaveViewset, basename="save")

urlpatterns = router.urls
