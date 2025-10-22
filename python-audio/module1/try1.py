from datetime import datetime as dt
import sounddevice as sd
from scipy.io.wavfile import write
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
import speech_recognition as sr

from pydub import AudioSegment

def capture_audio():
    try:
        duration = 5
        sample_freq = 44100
        recording = sd.rec(int(duration * 44100), dtype="int16", samplerate=sample_freq, channels=2)
        sd.wait()
        write(f"T{dt.now().timestamp() * 1000}.wav", sample_freq, recording)
        print(f"Audio captured")
    except Exception as e:
        print(f"failed to capture sound \nproblem: {e}")

# capture_audio()


def audio_conversion():
    try:
        audio_file = "C:\\Users\\madha\\Music\\Tum_Ho_Toh.mp3"
        output_format = f"T_MP3{dt.now().timestamp() * 1000}.wav"
        audio = AudioSegment.from_mp3(audio_file)
        audio.export(output_format, format="wav")
        print(f"converted and save as {output_format}")

    except Exception as e:
        raise Exception(f"failed to convert audio file \nproblem: {e}")
# audio_conversion()

def analyze_audio():
    try:
        fs, data = wavfile.read("T1761151211568.709.wav")
        amplitudes = np.abs(data)
        print(f"sample frequency: {fs}\naverage amplitude: {np.mean(amplitudes)}")

        print(f"\nvisualize wave\n")

        plt.plot(data)
        plt.title("audio waveform")
        plt.show()
    except Exception as e:
        raise Exception(f"failed to analyze audio file \nproblem: {e}")
    
# analyze_audio()


def identify_audio():
    try:
        # help(sr.Recognizer.recognize_google)
        recog = sr.Recognizer()

        sound = AudioSegment.from_file("harvard.wav")
        print(f"sound frame rate: {sound.frame_rate}\nsound channels: {sound.channels}\nsound sample width: {sound.sample_width}")
        sound = sound.set_channels(1).set_frame_rate(16000)
        sound.export("harvard.wav", format="wav")
        print(f"audio converted to mono successfully")

        with sr.AudioFile("harvard.wav") as source:
            audio = recog.record(source=source, duration=60)
            text = recog.recognize_google(audio, language="en-US")
            print(f"\ndetected speech: {text}")
    except Exception as e:
        raise Exception(f"failed to identify audio \nproblem: {e}")
    
identify_audio()