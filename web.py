import streamlit as st
from gtts import gTTS
import os
from io import BytesIO

# Streamlit 앱 설정
st.title("Text-to-Speech (TTS) 서비스")
st.write("텍스트를 입력하면 음성 파일을 다운로드할 수 있습니다.")

# 사용자로부터 텍스트 입력 받기
text_input = st.text_area("음성으로 변환할 텍스트를 입력하세요:", "")

# 음성 파일 생성 함수
def generate_audio(text):
    tts = gTTS(text=text, lang='ko')  # 한국어로 설정 (원하는 언어로 변경 가능)
    
    # 임시 파일로 저장하기
    audio_file_path = "output.mp3"
    tts.save(audio_file_path)
    
    return audio_file_path

# 음성 파일 다운로드 링크 제공
if st.button("음성 파일 생성"):
    if text_input:
        audio_file_path = generate_audio(text_input)
        
        # 파일을 BytesIO로 읽어들여 다운로드 링크 제공
        with open(audio_file_path, "rb") as audio_file:
            audio_bytes = audio_file.read()
        
        st.audio(audio_bytes, format='audio/mp3')  # 스트리밍 재생
        st.download_button(
            label="음성 파일 다운로드",
            data=audio_bytes,
            file_name="output.mp3",
            mime="audio/mp3"
        )
    else:
        st.warning("텍스트를 입력해주세요!")
