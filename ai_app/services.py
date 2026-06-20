class SimulatedAIService:
    def generate_response(self, prompt: str) -> str:
        if not prompt:
            raise ValueError("O prompt é obrigatório.")

        return f"Resposta simulada para: {prompt}"


class RealAIService:
    def generate_response(self, prompt: str) -> str:
        if not prompt:
            raise ValueError("O prompt é obrigatório.")

        return f"Resposta de IA para: {prompt}"
