import azure.cognitiveservices.speech as speechsdk
import os

def from_file(data_file,lang,endpoint_speech):
    speech_config = speechsdk.SpeechConfig(subscription=speech_key,
                                           endpoint= endpoint_speech,
                                           speech_recognition_language=lang
                                           )
    audio_input = speechsdk.AudioConfig(filename=data_file)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config,
                                                   audio_config=audio_input,
                                                   language=lang
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
