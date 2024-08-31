import google.generativeai as genai
import os
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import io
import speech_recognition as sr
from pystyle import Write, Colors
import threading

api_key = "GOOGLE_GEMİNNİ_APİ"
os.environ["API_KEY"] = api_key
genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

def speak_and_print(text):
    tts = gTTS(text=text, lang='tr', slow=False)
    tts_fp = io.BytesIO()
    tts.write_to_fp(tts_fp)
    tts_fp.seek(0)

    audio = AudioSegment.from_file(tts_fp, format="mp3")
    audio = audio.speedup(playback_speed=1.4)

    def print_text():
        for char in text:
            Write.Print(char, Colors.blue_to_cyan, end='', interval=0.06)

    threading.Thread(target=print_text).start()
    
    play(audio)

def listen_to_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak_and_print("Sizi Dinliyorum...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language='tr-TR')
            return text
        except sr.UnknownValueError:
            return "Sesi anlayamadım."
        except sr.RequestError:
            return "Hizmete ulaşılamıyor."

while True:
    user_input = listen_to_audio()

    if user_input.lower() == 'çıkış':
        speak_and_print("Programdan çıkılıyor...")
        print("\nProgramdan çıkılıyor...")
        break

    print(f"\nKullanıcı mesajı: {user_input}")

    response = model.generate_content(user_input)
    ai_response = response.text
    ai_response = ai_response.replace("**", "").replace("*", "")

    print("\nYapay zeka tarafından oluşturulan metin:")
    speak_and_print(ai_response)
def dinle():
    while True:
        komut = input("Dinliyorum: ")
        if komut.lower() == 'hey jeff':
            print("Durdu ve tekrar sizi dinliyorum...")
            continue
        else:
            print("Komut anlaşılamadı. Tekrar deneyin.")

dinle()