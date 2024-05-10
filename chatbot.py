import os

import google.generativeai as genai

CHAVE = "SUA_CHAVE_AQUI"

genai.configure(api_key=CHAVE)

for m in genai.list_models():
    if "generateContent" in m.supported_generation_methods:
        print(m.name)

generation_config = {
    "candidate_count": 1,
    "temperature": 0.5,
}

safety_settings = {
    "HATE": "BLOCK_NONE",
    "HARASSMENT": "BLOCK_NONE",
    "SEXUAL": "BLOCK_NONE",
    "DANGEROUS": "BLOCK_NONE",
}

model = genai.GenerativeModel(
    model_name="gemini-1.0-pro",
    generation_config=generation_config,
    safety_settings=safety_settings,
)

chat = model.start_chat(history=[])

prompt = input("Esperando prompt: ")

while prompt != "fim":
    response = chat.send_message(prompt)
    print("Resposta:", response.text, "\n")
    prompt = input("Esperando prompt: ")
