import numpy as np
import wave

file_name = "tone.wav"
sample_rate = 48000
duration = 2.0
frequency=440.0

def create_tone(file, sample_rate, dur, freq):
    number_of_samples = int(sample_rate * duration)
    time_axis = np.linspace(0, dur, number_of_samples, False)
    # wave_data = 0.5 * np.sin(2 * np.pi * freq * time_axis)
    left_channel = 0.5 * np.sin(2 * np.pi * 440.0 * time_axis)
    right_channel = 0.5 * np.sin(2 * np.pi * 880.0 * time_axis)

    # wave_data_int16 = np.int16(wave_data * 32767)
    wave_data_int16_1 = np.int16(left_channel * 32767)
    wave_data_int16_2 = np.int16(right_channel * 32767)

    # stereo_wave = np.column_stack((wave_data_int16, wave_data_int16))

    stereo_wave = np.column_stack((wave_data_int16_1, wave_data_int16_2))

    with wave.open(file, mode='w') as wav_file:
        wav_file.setnchannels(2)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(stereo_wave.tobytes())

        print(f"WAV file {file} has been created")


create_tone(file_name, sample_rate, duration, frequency)