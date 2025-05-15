import tkinter as tk
import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import random

# Sample vocabulary
words = {
    "hello": "hola",
    "thank you": "gracias",
    "goodbye": "adiós",
    "please": "por favor",
    "yes": "sí",
    "no": "no"
}

# Initialize GUI
window = tk.Tk()
window.title("Language Learning App with Speech Recognition")
window.geometry("400x300")

# Variables
target_word = tk.StringVar()
result = tk.StringVar()
feedback = tk.StringVar()

def speak_text(text):
    tts = gTTS(text=text, lang='en')
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def next_word():
    word = random.choice(list(words.keys()))
    target_word.set(word)
    result.set("")
    feedback.set("")
    speak_text(f"Please say: {word}")

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        result.set("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            recognized = recognizer.recognize_google(audio)
            result.set(f"You said: {recognized}")
            if recognized.lower() == target_word.get().lower():
                feedback.set("✅ Correct pronunciation!")
            else:
                feedback.set("❌ Try again.")
        except sr.UnknownValueError:
            result.set("Sorry, could not understand.")
        except sr.WaitTimeoutError:
            result.set("Timeout. Try again.")

# UI Elements
tk.Label(window, text="Speak the following word in English:").pack(pady=10)
tk.Label(window, textvariable=target_word, font=("Arial", 24)).pack()
tk.Button(window, text="🎤 Speak", command=recognize_speech).pack(pady=10)
tk.Button(window, text="➡️ Next Word", command=next_word).pack(pady=5)
tk.Label(window, textvariable=result, fg="blue").pack(pady=10)
tk.Label(window, textvariable=feedback, font=("Arial", 14)).pack()

# Start
next_word()
window.mainloop()
