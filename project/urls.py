from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, ModuleViewSet, TaskViewSet, SubmissionViewSet, InputOutputViewSet, EnrollmentViewSet,RegisterViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'modules', ModuleViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'submissions', SubmissionViewSet)
router.register(r'inputs', InputOutputViewSet)
router.register(r'enrollments', EnrollmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/',RegisterViewSet.as_view(),name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
