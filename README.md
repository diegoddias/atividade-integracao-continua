# Atividade Integradora - Simulando um Ciclo de Integração Contínua

Projeto desenvolvido em Django para demonstrar um fluxo básico de Integração Contínua utilizando GitHub Actions.

Repositório:
https://github.com/diegoddias/atividade-integracao-continua/

## Tecnologias Utilizadas

- Python 3.13
- Django 5.2
- Google Gemini API
- GitHub Actions

## Configuração do Ambiente

### Clonar o repositório

git clone https://github.com/diegoddias/atividade-integracao-continua.git

cd atividade-integracao-continua

### Criar ambiente virtual

Windows:

python -m venv venv

.\venv\Scripts\Activate.ps1

### Instalar dependências

pip install -r requirements.txt

### Configurar variável de ambiente

Criar um arquivo .env na raiz do projeto:

GEMINI_API_KEY=sua_chave_aqui

## Executar a aplicação

python manage.py runserver

A aplicação ficará disponível em:

http://127.0.0.1:8000

## Endpoints

### Resposta Simulada

POST

api/simulado/

Body:

{
"prompt": "Olá"
}

Resposta:

{
"response": "Resposta simulada para: Olá"
}

### Resposta com IA Gemini

POST

api/ia/

Body:

{
"prompt": "Olá"
}

Resposta:

{
"response": "Resposta gerada pela IA"
}

## Executar Testes

python manage.py test

## Pipeline

O projeto utiliza GitHub Actions para:

- Instalar dependências
- Executar testes automatizados
- Validar a aplicação a cada push

## Autor

Diego Dias
