from django.urls import path
from .views import SimulatedPromptView, AiPromptView

urlpatterns = [
    path("prompt/simulado/", SimulatedPromptView.as_view()),
    path("prompt/ia/", AiPromptView.as_view()),
]
