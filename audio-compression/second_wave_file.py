import numpy as np
import struct
import wave

filename = "second_wave_file.wav"
sample_rate = 44100
duration = 2.0
frequency = 440.0

num_samples = int(sample_rate * duration)

t = np.linspace(0, duration, num_samples, False)

wave_data = 0.5 * np.sin(2 * np.pi * frequency * t)

wave_data_int16 = np.int16(wave_data * 32767)

with wave.open(filename, "w") as wav_file:
    wav_file.setnchannels(1)
    wav_file.setsampwidth(3)
    wav_file.setframerate(sample_rate)
    wav_file.writeframes(wave_data_int16.tobytes())

print(f"WAV file {filename} has been created successfully.") 