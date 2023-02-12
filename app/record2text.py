import azure.cognitiveservices.speech as speechsdk
import os
speech_key, service_region = os.environ['KEY_AZURE_ML'] , "eastus"

def from_file(data_file):
    speech_config = speechsdk.SpeechConfig(subscription=speech_key,
                                           region=service_region ,
                                           speech_recognition_language="en-US"
                                           )
    audio_input = speechsdk.AudioConfig(filename=data_file)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config,
                                                   audio_config=audio_input,
                                                   language="en-US"
    )

    # result = speech_recognizer.recognize_once_async().get()
    result = speech_recognizer.recognize_once()
    
    # Checks result.
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(result.text))
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(result.no_match_details))
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
    
    return(result.text)

