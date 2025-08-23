
# In a Wave file data are stored in a PCM (pulse code modulation) format like 8 bit pcm(unsigned integer), 16 bit pcm(signed integer), 24 bit pcm and 32 bit pcm(floating point data)

import wave
import numpy as np
file1 = "first_wave_file.wav"
file2 = "second_wave_file.wav"

#compare two different wave files: 1. byte by byte

# def compare_function(file1, file2):
#     with open("first_wave_file.wav", mode='rb') as file1, open("second_wave_file.wav", mode='rb') as file2:
#         if(file1.read() == file2.read()):
#             print("Both file are same")
#         else:
#             print("Both files are different") 


# file1 = "first_wave_file.wav"
# file2 = "second_wave_file.wav"

# compare_function(file1,file2)


#2. compare audio data

# def compare_wav_data(file1, file2):
#     with wave.open(file1, mode='rb') as file1, wave.open(file2,mode='r') as file2:
#         if (file1.getnchannels() != file2.getnchannels() |
#         file1.getsampwidth() != file2.getsampwidth() |
#         file1.getframerate() != file2.getframerate()):
#             print("files are not same")
#             return
        
#         frame1 = np.frombuffer(file1.readframes(file1.getnframes()), dtype=np.int16)
#         frame2 = np.frombuffer(file2.readframes(file2.getnframes()), dtype=np.int16)

#         if(np.array_equal(frame1, frame2)):
#             print("files are same")
#         else:
#             print("files are not same")


# compare_wav_data(file1, file2)



