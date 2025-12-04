from flask import Flask
import requests

def emotion_detector(text):
    text_to_analyse = text
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    body = {
        "raw_document": {
            "text": text_to_analyse
        }
    }
    response = requests.post(url, headers=headers, json=body)
    data = response.json()

    text = data["emotionPredictions"][0]["emotionMentions"][0]["span"]["text"]
    print(text)
    return text

emotion_detector('I love this new technology.')