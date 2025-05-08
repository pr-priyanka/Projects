pip install PyPDF2 pyttsx3 SpeechRecognition fpdf pyaudio


import PyPDF2
import pyttsx3

def pdf_to_audio(pdf_path):
    reader = PyPDF2.PdfReader(open(pdf_path, 'rb'))
    speaker = pyttsx3.init()
    
    for page in reader.pages:
        text = page.extract_text()
        if text:
            speaker.say(text)
            speaker.runAndWait()

pdf_path = 'example.pdf'  # Replace with your PDF file path
pdf_to_audio(pdf_path)


import speech_recognition as sr
from fpdf import FPDF

def speech_to_text(duration=10):
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("Listening...")
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, phrase_time_limit=duration)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""
    except sr.RequestError:
        print("Speech recognition service unavailable.")
        return ""

def save_text_to_pdf(text, filename='output.pdf'):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, text)
    pdf.output(filename)

spoken_text = speech_to_text()
if spoken_text:
    save_text_to_pdf(spoken_text)
