# Chatbot utilizando Gemini AI
Criacao de um Chatbot com o Gemini AI PRO 1.0 e Python 3.12

Instalacao e execucao:
<ol>
    <li> Obter sua Google Api Key [aqui](https://aistudio.google.com/app/apikey)
    <li> Baixar os pacotes do Gemini AI:

```bash
pip install -U google-generativeai
```

<li> Substituir no codigo o campo "SUA_CHAVE_AQUI" pela Key obtida no site (passo 1)
</ol>

> Foi utilizado o Python 3.12

Metodo util para buscar modelos do Gemini AI
```python
for model in genai.list_models():
    if "generateContent" in model.supported_generation_methods:
        print(model.name)
```