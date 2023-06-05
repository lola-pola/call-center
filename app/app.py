from audio_recorder_streamlit import audio_recorder
from sumerize import find_keywords , find_something
from record2text import from_file 
from os.path import isfile, join
from datetime import datetime
import streamlit as st
from os import listdir
import openai
import os 


st.set_page_config(layout="wide")
st.title("Call Center")


st.write("OPENAI RULEZ")
audio_bytes = audio_recorder(
    text="",
    recording_color="#e8b62c",
    neutral_color="#6aa36f",
    icon_name="user",
    icon_size="6x",
)

runner = False
with st.sidebar:
    custom =  st.checkbox('Advance Configuration',False)
    if custom:
        key = st.text_input('API Key', type='password')
        base = st.text_input('API Base', value="https://aks-production.openai.azure.com/" )
        model_name = st.text_input('Model Name')
        runner =  st.checkbox('Submit')

        openai.api_type = "azure"
        openai.api_base = base 
        openai.api_version = "2022-12-01"
        openai.api_key = key
        lang = st.text_input('Model Name',"en-US")
        endpoint_speech = st.text_input('Endpoint Speech',f"wss://speechspeech.cognitiveservices.azure.com/stt/speech/recognition/conversation/cognitiveservices/v1?language={lang}")


        if runner:
            st.success('This is a success message!', icon="✅")
    else:
        model_name = "call-center"
        openai.api_type = "azure"
        openai.api_base = "https://aks-production.openai.azure.com/" 
        openai.api_version = "2022-12-01"
        openai.api_key = os.getenv("KEY_AZURE_AI_DEVINCHI")
        speech_key = os.environ['KEY_AZURE_ML']
        endpoint_speech  =  "wss://speechspeech.cognitiveservices.azure.com/stt/speech/recognition/conversation/cognitiveservices/v1?language=en-US"
        lang = "en-US"
        runner = custom
        st.success('This is a success message!', icon="✅")

if runner:
    selection = st.selectbox("How you want to start using call center :) ?", ["-- select ---", "from file", "from mic", "list existing"])

    if selection == "from mic":
        st.balloons()
        data_file = f'userdata/call-center-{datetime.now().strftime("%Y%m%d-%H%M%S")}.wav'
        audio_bytes = audio_recorder(pause_threshold=30)
        if audio_bytes:
           with open(data_file, "wb") as fs:
                fs.write(audio_bytes)

           st.audio(audio_bytes, format="audio/wav", start_time=0)  
           if st.button("change to text"):
               st.write(from_file(data_file,lang))
           if  st.button("finding key words"):
               st.write("finding key words ...")
               st.write(from_file(data_file,lang))
               st.write(find_keywords(from_file(data_file,lang)),model_name)

    elif selection == "from file":
        st.snow()
        audio_bytes1 = st.file_uploader("Upload Files", type=["wav"],accept_multiple_files=False)

        data_file_location = f'uploaded/call-center-{datetime.now().strftime("%Y%m%d-%H%M%S")}.wav'

        if audio_bytes1:
            # st.write(type(audio_bytes1))
            audio_bytes2 = audio_bytes1.read()
            with open(data_file_location, "wb") as fs:
                fs.write(audio_bytes2)
            if data_file_location:
                st.audio(audio_bytes2, format="audio/wav", start_time=0)
                # if st.button("change to text"):
                #    st.write(from_file(data_file_location))
                if st.button("finding key words"):
                   st.write("finding key words ...")
                   st.write(from_file(data_file_location,lang))
                   st.write(find_keywords(from_file(data_file_location,lang)),model_name)
                if st.checkbox('find spesific something'):
                   something = st.text_input('enter what you would loke to do')
                   lola = from_file(data_file_location,lang)
                   if something:
                    st.write(find_something(lola,something,model_name))

    elif selection == "list existing":
        st.snow()
        selection = st.selectbox("Select file", ['uploaded','userdata'])
        if selection:
            selected = st.selectbox("Select file", [f for f in listdir(selection) if isfile(join(selection, f))])
            if selected:
                full_path = f'{selection}/{selected}'
                audio_file = open(full_path, 'rb')
                audio_bytes = audio_file.read()
                st.audio(audio_bytes, format="audio/wav", start_time=0)
                if st.button("change to text"):
                   st.write(from_file(full_path,lang))
                if st.button("finding key words"):
                   st.write("finding key words ...")
                   st.write(from_file(full_path,lang))
                   st.write(find_keywords(from_file(full_path,lang)),model_name)

