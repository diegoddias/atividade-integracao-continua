import os
from dotenv import load_dotenv
from google import genai

load_dotenv()


class SimulatedAIService:
    def generate_response(self, prompt: str) -> str:
        if not prompt:
            raise ValueError("O prompt é obrigatório.")

        return f"Resposta simulada para: {prompt}"


class RealAIService:
    def generate_response(self, prompt: str) -> str:
        if not prompt:
            raise ValueError("O prompt é obrigatório.")

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("A variável GEMINI_API_KEY não foi configurada.")

        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt,
        )

        return response.text
