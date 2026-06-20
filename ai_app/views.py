from django.shortcuts import render

import json
from django.http import JsonResponse
from django.views import View
from .services import SimulatedAIService, RealAIService
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name="dispatch")
class BasePromptView(View):
    service_class = None

    def post(self, request):
        try:
            data = json.loads(request.body)
            prompt = data.get("prompt")

            service = self.service_class()
            response = service.generate_response(prompt)

            return JsonResponse({"response": response}, status=200)

        except ValueError as error:
            return JsonResponse({"error": str(error)}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido."}, status=400)


class SimulatedPromptView(BasePromptView):
    service_class = SimulatedAIService


class AiPromptView(BasePromptView):
    service_class = RealAIService
