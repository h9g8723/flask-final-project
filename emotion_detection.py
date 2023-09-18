import requests
import json
import time

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    print("Preparing to send request...")

    # Log the URL, headers, and input_json before sending the request
    print(f"URL: {url}")
    print(f"Headers: {headers}")
    print(f"Input JSON: {input_json}")

    try:
        print("Sending request...")
        start_time = time.time()
        
        response = requests.post(url, headers=headers, json=input_json, timeout=20)
        
        elapsed_time = time.time() - start_time
        print(f"Time taken for the request: {elapsed_time:.2f} seconds")
        
        print(f"Received response with status code: {response.status_code}")

        if response.status_code == 200:
            output = response.json()
            
            # Extract the emotions and their scores
            emotions = output['emotionPredictions'][0]['emotion']
            dominant_emotion = max(emotions, key=emotions.get)
            
            print("Response content: ", output)
            
            result = {
                'anger': emotions.get('anger', 0),
                'disgust': emotions.get('disgust', 0),
                'fear': emotions.get('fear', 0),
                'joy': emotions.get('joy', 0),
                'sadness': emotions.get('sadness', 0),
                'dominant_emotion': dominant_emotion
            }
            
            return result
        else:
            print(f"Response content: {response.content}")
            return f"Received unexpected status code {response.status_code}: {response.content}"
    except requests.Timeout:
        return "Request timed out"
    except requests.RequestException as error:
        print(f"An error occurred: {error}")
        return f"An error occurred: {error}"

# Test internet connectivity
try:
    test_response = requests.get('https://www.google.com', timeout=20)
    if test_response.status_code == 200:
        print("Internet connection is fine.")
    else:
        print("Received an unexpected status code while testing internet connection.")
except requests.RequestException as e:
    print(f"Unable to access the internet: {e}")

# Optional: You can call the function to test it here
result = emotion_detector("I am so happy I am doing this.")
print(result)
