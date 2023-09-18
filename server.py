from flask import Flask, request, render_template, jsonify
# Import your emotion_detector function here
# from <your_module> import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_endpoint():
    try:
        # Get the text from the form input
        text = request.form['text']

        # Call the emotion_detector function
        emotion_result = emotion_detector(text)

        # Handle blank entries
        if emotion_result["status_code"] == 400:
            return jsonify({"output": "Invalid text! Please try again!"})

        # Prepare the output in the required format
        output_string = (
            f"For the given statement, the system response is "
            f"'anger': {emotion_result['anger']}, "
            f"'disgust': {emotion_result['disgust']}, "
            f"'fear': {emotion_result['fear']}, "
            f"'joy': {emotion_result['joy']}, and "
            f"'sadness': {emotion_result['sadness']}. "
            f"The dominant emotion is {emotion_result['dominant_emotion']}."
        )

        return jsonify({"output": output_string})

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
