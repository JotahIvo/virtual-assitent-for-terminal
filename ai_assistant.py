from password import API_KEY
import requests #pip install requests
import json
import os, sys


headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
link = "https://api.openai.com/v1/chat/completions"
model_id = "gpt-3.5-turbo"


def return_only_code(text):
    first_ocurrence = text.find("```")
    last_ocurrence = text.rfind("```")
    code = text[first_ocurrence:last_ocurrence+1]

    return code


def lu_translate(name, text, lang):
    input_text = f"Chat, traduza para {lang} o seguinte texto: {text}"

    body = {
        "model": model_id,
        "messages": [{"role": "user", "content": input_text}]
    }

    body = json.dumps(body)
    request = requests.post(link, headers=headers, data=body)

    answer = request.json()

    answer_message = answer["choices"][0]["message"]["content"]

    print(f"\nTraduzindo {text} para {lang}: ")
    print(answer_message)    


def dev_lu(name, text, prog_lang):
    input_text = f"Preciso que {text} em {prog_lang} (responda apenas com o código)"

    body = {
        "model": model_id,
        "messages": [{"role": "user", "content": input_text}]
    }

    body = json.dumps(body)
    request = requests.post(link, headers=headers, data=body)

    answer = request.json()

    answer_message = answer["choices"][0]["message"]["content"]

    os.system("clear")

    print(f"\nPronto {name}, aqui está o código em {prog_lang} que resolve o seu problema: \n")

    print(return_only_code(answer_message))