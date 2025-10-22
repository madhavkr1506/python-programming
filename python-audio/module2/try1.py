import sounddevice as sd
from scipy.io.wavfile import read, write
from pydub import AudioSegment

import numpy as np
from datetime import datetime as dt
import logging

class VoiceAssistance:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.log = logging.getLogger(f" {dt.now().timestamp() * 1000} ")

        self.sample_frequency = 44100
        self.channels = 2
        self.duration = 5

        self.recording = None

        self.audio_captured = False

        self.wav_audio = "audio.wav"

        self.audio_adjusted = False

        self.freq_adjusted = 16000
        self.channels_adjusted = 1

        self.frame_duration = 0.02



    def capture_audio(self):
        try:
            self.recording = sd.rec(
                frames=int(self.duration * self.sample_frequency), samplerate=self.sample_frequency, channels=self.channels, dtype="int16"
            )
            sd.wait()
            self.audio_captured = True
            self.log.info(f"Capture system done its execution")

        except Exception as e:
            raise Exception(f"failed! capture audio system\nproblem: {e}")
        
    def save_captured_audio(self):
        try:
            if self.audio_captured:
                write(self.wav_audio, self.sample_frequency, self.recording)
                self.log.info("Captured audio save successfully")

        except Exception as e:
            raise Exception(f"failed! can't save captured audio\nproblem: {e}")
        
    def voice_activity_detection(self):
        try:
            def adjust_audio():
                try:
                    sound = AudioSegment.from_file(self.wav_audio, format="wav")
                    sound = sound.set_channels(self.channels_adjusted).set_frame_rate(self.freq_adjusted)
                    sound.export(self.wav_audio, format="wav")

                    self.log.info(f"sound sample rate adjusted to: {sound.frame_rate}Hz\nsound channels adjusted to: {sound.channels}")

                    if sound.channels > 1:
                        self.audio_adjusted = False
                        return
                    self.audio_adjusted = True
                    
                except Exception as e:
                    raise Exception(f"failed! can't adjust audio\nproblem: {e}")
            adjust_audio()

            def read_wav() -> np.array:
                try:
                    _, data = read(self.wav_audio)
                    if isinstance(data, np.ndarray):
                        return data
                    else:
                        raise Exception("invalid data type found, not a numpy array")
                except Exception as e:
                    raise Exception(f"failed! can't read audio file\nproblem: {e}")
            data = read_wav()
            self.log.info(f"audio data received: {data}")

            if self.audio_adjusted:
                frame_size = int(self.sample_frequency * self.frame_duration)

                self.log.info(f"Length of data: {len(data)}\nFrame size: {frame_size}")
                
                frames = []
                for i in range(0, len(data), frame_size):
                    frame = data[i:i+frame_size]
                    # self.log.info(f"Frame type: {type(frame)}\nLength of frame: {len(frame)}")
                    if len(frame == frame_size):
                        frames.append(frame)

            def find_root_mean_square():
                try:
                    rms_mean = [np.sqrt(np.mean(frame.astype(float) ** 2)) for frame in frames]
                    # self.log.info(f"Root Mean Square: {rms_mean}")
                    return rms_mean
                except Exception as e:
                    raise Exception(f"failed! can't identify power in speech\nproblem: {e}")
            rms_mean = find_root_mean_square()


        except Exception as e:
            raise Exception(f"failed! can't detect voice activity\nproblem: {e}")
        

def main():
    try:
        vs = VoiceAssistance()
        vs.capture_audio()
        vs.save_captured_audio()
        vs.voice_activity_detection()
    except Exception as e:
        print(f"Message: {e}")


if __name__ == "__main__":
    main()