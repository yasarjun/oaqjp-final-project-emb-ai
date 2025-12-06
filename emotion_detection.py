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
    try:
        response = requests.post(url, headers=headers, json=body)
        if response.status_code == 400:
            return {
                "anger": '', 
                "disgust": '', 
                "fear": '', 
                "joy": '', 
                "sadness": '', 
                "dominant_emotion": ''
            }

        
        data = response.json()

        text = data["emotionPredictions"][0]["emotionMentions"][0]["span"]["text"]
        dominant_emotion = ''
        dominant_score = 0
        emotions = {}
        for key, value in data["emotionPredictions"][0]["emotion"].items():
            print(key, value)
            emotions[key] = value
            if dominant_emotion is None:
                dominant_emotion = key
                dominant_score = value
            else:
                if (value > dominant_score):
                    dominant_score = value 
                    dominant_emotion = key
        emotions['dominant_emotion'] = dominant_emotion
        if emotions['dominant_emotion'] is None:
            return 'Invalid text! Please try again!.'
        print(emotions)
        return emotions
    except:
        return 'Something went wrong'
    
    

emotion_detector('I am so happy I am doing this.')