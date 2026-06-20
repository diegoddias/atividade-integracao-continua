from django.test import TestCase

import json
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

    def test_should_receive_ai_response(self):
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
