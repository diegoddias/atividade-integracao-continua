import json

from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .services import SimulatedAIService, RealAIService


@method_decorator(csrf_exempt, name="dispatch")
class BasePromptView(View):
    service_class = None

    def post(self, request):
        try:
            if self.service_class is None:
                return JsonResponse(
                    {"error": "Serviço de IA não configurado."},
                    status=500
                )

            data = json.loads(request.body)
            prompt = data.get("prompt")

            service = self.service_class()
            response = service.generate_response(prompt)

            return JsonResponse({"response": response}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido."}, status=400)

        except ValueError as error:
            return JsonResponse({"error": str(error)}, status=400)

        except EnvironmentError as error:
            return JsonResponse({"error": str(error)}, status=500)

        except RuntimeError as error:
            return JsonResponse({"error": str(error)}, status=502)

        except Exception:
            return JsonResponse(
                {"error": "Erro interno inesperado."},
                status=500
            )


class SimulatedPromptView(BasePromptView):
    service_class = SimulatedAIService


class AiPromptView(BasePromptView):
    service_class = RealAIService
