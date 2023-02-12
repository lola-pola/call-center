import streamlit as st
from record2text import from_file 
from audio_recorder_streamlit import audio_recorder
from sumerize import find_keywords
from datetime import datetime
from os import listdir
from os.path import isfile, join

st.set_page_config(layout="wide")
st.title("Call Center")

audio_bytes = audio_recorder(
    text="",
    recording_color="#e8b62c",
    neutral_color="#6aa36f",
    icon_name="user",
    icon_size="6x",
)


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
           st.write(from_file(data_file))
       if  st.button("finding key words"):
           st.write("finding key words ...")
           st.write(from_file(data_file))
           st.write(find_keywords(from_file(data_file)))

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
            if st.button("change to text"):
               st.write(from_file(data_file_location))
            if st.button("finding key words"):
               st.write("finding key words ...")
               st.write(from_file(data_file_location))
               st.write(find_keywords(from_file(data_file_location)))


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
               st.write(from_file(full_path))
            if st.button("finding key words"):
               st.write("finding key words ...")
               st.write(from_file(full_path))
               st.write(find_keywords(from_file(full_path)))
                
            


