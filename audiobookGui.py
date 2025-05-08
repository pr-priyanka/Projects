%pip install PyPDF2 pyttsx3 SpeechRecognition fpdf
%conda install -c conda-forge pyaudio -y

import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2
import pyttsx3
import speech_recognition as sr
from fpdf import FPDF

def pdf_to_audio():
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if not pdf_path:
        return
    try:
        reader = PyPDF2.PdfReader(open(pdf_path, 'rb'))
        speaker = pyttsx3.init()
        for page in reader.pages:
            text = page.extract_text()
            if text:
                speaker.say(text)
                speaker.runAndWait()
        messagebox.showinfo("Success", "Finished reading the PDF aloud!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def speech_to_pdf():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    try:
        with mic as source:
            messagebox.showinfo("Recording", "Speak now (10 seconds)...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, phrase_time_limit=10)
        text = recognizer.recognize_google(audio)

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, text)
        save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if save_path:
            pdf.output(save_path)
            messagebox.showinfo("Success", f"Speech saved as PDF: {save_path}")
    except sr.UnknownValueError:
        messagebox.showerror("Error", "Could not understand audio.")
    except sr.RequestError:
        messagebox.showerror("Error", "Speech recognition service unavailable.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Setup
root = tk.Tk()
root.title("PDF ↔ Audio/Speech Tool")
root.geometry("400x250")

label = tk.Label(root, text="Select an Option:", font=("Arial", 14))
label.pack(pady=20)

btn1 = tk.Button(root, text="PDF to Audiobook", font=("Arial", 12), command=pdf_to_audio, width=30)
btn1.pack(pady=10)

btn2 = tk.Button(root, text="Speech to PDF", font=("Arial", 12), command=speech_to_pdf, width=30)
btn2.pack(pady=10)

root.mainloop()



