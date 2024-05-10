import os

import google.generativeai as genai

CHAVE = "SUA_CHAVE_AQUI"

genai.configure(api_key=CHAVE)

generation_config = {
    "candidate_count": 1,
    "temperature": 0.8,
}

safety_settings = {
    "HATE": "BLOCK_ONLY_HIGH",
    "HARASSMENT": "BLOCK_ONLY_HIGH",
    "SEXUAL": "BLOCK_ONLY_HIGH",
    "DANGEROUS": "BLOCK_ONLY_HIGH",
}

model = genai.GenerativeModel(
    model_name="gemini-1.0-pro",
    generation_config=generation_config,
    safety_settings=safety_settings,
)

chat = model.start_chat(history=[])

print("Para encerrar o prompt digite: fim ")
prompt = input("Sua pergunta: ")

while prompt != "fim":
    response = chat.send_message(prompt)
    print("Resposta:", response.text, "\n")
    prompt = input("Sua pergunta: ")
