from django.urls import re_path, path
from fastperfomance.views import locustapi
from fastperfomance.views import locustapi, locustrun

urlpatterns = [
    path('locustapi/', locustapi.LocustAPIView.as_view({
        "get": "list",
        "post": "add",
        "patch": "update",
        "delete": "delete"
    })),
    path('locustapi/<int:pk>/', locustapi.LocustAPIView.as_view({"get": "single"})),
    path('locustapirun/<int:pk>/', locustrun.LocustRUNAPIView.as_view({
        "get": "run_single",

    })),

]
