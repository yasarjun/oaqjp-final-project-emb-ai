''' Main module to handle requests '''
from flask import Flask, render_template
from EmotionDetection.emotion_detection import emotion_detector



app = Flask(__name__)
@app.route('/')
def home():
    ''' Handles default requests '''
    return render_template('index.html')

@app.route('/emotionDetector/<textToAnalyze>')
def run_analysis(textToAnalyze):
    ''' Method to accept incoming text to analyse'''
    response =  emotion_detector(textToAnalyze)
    text = (f"For the given statement, the system response "
            f"is 'anger': {response['anger']}, "
            f"disgust': {response['disgust']}, "
            f"fear': {response['fear']}, "
            f"joy': {response['joy']} and "
            f"sadness': {response['sadness']}. "
            f"The dominant emotion is {response['dominant_emotion']}.")
    return text
if __name__ == '__main__':
    app.run(debug=True)
