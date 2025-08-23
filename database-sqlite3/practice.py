import sqlite3
import numpy as np
import wave
import hashlib

class CreateWavFile:
    def __init__(self, file_name, signature_file):
        self.file_name = file_name
        self.signature_file = signature_file

    def set_parameter(self, sample_rate, frequency, duration):
        self.sample_rate = sample_rate
        self.frequency = frequency
        self.duration = duration
        self.num_samples = int(self.sample_rate * self.duration)
        self.time_axis = np.linspace(0, self.duration, self.num_samples, False)
        self.wave_data = 0.5 * np.sin(2 * np.pi * self.frequency * self.time_axis)
        self.wave_data_int16 = np.int16(self.wave_data * 32767)

    def write_in_file(self):
        with wave.open(self.file_name, 'w') as wav_file:
            wav_file.setnchannels(1)
            wav_file.setsampwidth(2)
            wav_file.setframerate(self.sample_rate)
            wav_file.writeframes(self.wave_data_int16.tobytes())

        print(f"{self.file_name} is generated")

    def generate_signature(self):
        try:
            with open(self.file_name, mode='rb') as read_wav_file:
                read_bytes = read_wav_file.read()
                signatures = hashlib.sha256(read_bytes).hexdigest()
                return signatures
        except FileNotFoundError:
            print(f"{self.file_name} is not found")
            return None

    def write_signature_in_file(self, signature):
        with open(file=self.signature_file, mode='w') as signature_file:
            signature_file.write(signature)

    def store_signature_in_db(self, db_filename="s3_bucket.db"):
        connection = sqlite3.connect(db_filename)
        cursor_object = connection.cursor()

        cursor_object.execute("create table if not exists signature_collector (file_name text primary key, signature text)")
        signature = self.generate_signature()
        if signature:
            cursor_object.execute("insert or replace into signature_collector (file_name, signature) values (?, ?)", (self.file_name, signature))
            connection.commit()
            print(f"Signature for '{self.file_name}' stored in database.")
        connection.close()

wav_file_object = CreateWavFile("Wave1001.wav", "Wave1001_sig.txt")
wav_file_object.set_parameter(44100, 440.0, 2.0)
wav_file_object.write_in_file()
wav_file_object.write_signature_in_file(wav_file_object.generate_signature())
wav_file_object.store_signature_in_db()

import sqlite3
import hashlib

def verify_signature(wav_file, signature_file):
    try:
        connection = sqlite3.connect("s3_bucket.db")
        cursor_object = connection.cursor()

        with open(wav_file, mode='rb') as wav_file_read:
            read_bytes = wav_file_read.read()
            calculated_signature = hashlib.sha256(read_bytes).hexdigest()

        cursor_object.execute("select signature FROM signature_collector where file_name = ?", (wav_file,))
        stored_signature_tuple = cursor_object.fetchone()
        connection.close()

        if stored_signature_tuple:
            stored_signature = stored_signature_tuple[0] 

            if stored_signature == calculated_signature:
                print("Signature matched")
            else:
                print("Signature not matched")
        else:
            print(f"Signature for '{wav_file}' not found in database.")

    except Exception as e:
        print(f"An error occurred: {e}")

verify_signature("Wave1001.wav", "Wave1001_sig.txt")