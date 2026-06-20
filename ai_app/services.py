import os
from dotenv import load_dotenv
from google import genai
from google.genai import errors

load_dotenv()


class SimulatedAIService:
    def generate_response(self, prompt: str) -> str:
        if not prompt or not prompt.strip():
            raise ValueError("O prompt é obrigatório.")

        return f"Resposta simulada para: {prompt}"


class RealAIService:
    def generate_response(self, prompt: str) -> str:
        if not prompt or not prompt.strip():
            raise ValueError("O prompt é obrigatório.")

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise EnvironmentError(
                "A variável GEMINI_API_KEY não foi configurada.")

        try:
            client = genai.Client(api_key=api_key)

            response = client.models.generate_content(
                model="gemini-3.5-flash",
                contents=prompt.strip(),
            )

            if not response.text:
                raise RuntimeError("A API não retornou uma resposta válida.")

            return response.text

        except errors.APIError as error:
            raise RuntimeError(
                f"Erro ao se comunicar com a API Gemini: {error}")

        except Exception as error:
            raise RuntimeError(
                f"Erro inesperado ao gerar resposta da IA: {error}")
