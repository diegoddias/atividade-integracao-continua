import json
from unittest.mock import patch
from django.test import TestCase, Client


class PromptRoutesTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_should_send_prompt_to_simulated_route(self):
        payload = {
            "prompt": "Explique integração contínua"
        }

        response = self.client.post(
            "/api/prompt/simulado/",
            data=json.dumps(payload),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn("response", response.json())

    @patch("ai_app.services.RealAIService.generate_response")
    def test_should_receive_ai_response(self, mock_generate_response):
        mock_generate_response.return_value = "Resposta mockada da IA"

        payload = {
            "prompt": "Explique testes unitários"
        }

        response = self.client.post(
            "/api/prompt/ia/",
            data=json.dumps(payload),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn("response", response.json())
        self.assertEqual(response.json()["response"], "Resposta mockada da IA")
