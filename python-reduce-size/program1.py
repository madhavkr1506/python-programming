

import sys
import os
import json
import shutil
import subprocess
import signal
from pydub import AudioSegment
from PIL import Image

class Compression:
    def __init__(self, **kwargs):
        args = sys.argv[1:]
        if len(args) <= 0:
            raise Exception(f"Missing file path!\nPlease follow sequence while running job: python script.py filePath..")
        self.filePath = args[0]
    
    def getInputOutputPath(self):
        try:
            filePath, fileExtension = os.path.splitext(self.filePath)
            inputPath = filePath + fileExtension
            outputPath = filePath + "_copy" + fileExtension

            return inputPath, outputPath, fileExtension
        except Exception as e:
            raise Exception(f"getInputOutputPath failure {str(e)}")
        
    class Process:
        def __init__(self, com):
            self.inputPath, self.outputPath, self.FileExtension  = com.getInputOutputPath()
            print(f"inputPath: {self.inputPath}\noutputPath: {self.outputPath}\nfileExtension: {self.FileExtension}")

            self.matchingExtension()
        
        def matchingExtension(self):
            try:
                match (self.FileExtension.lower()):
                    case ('.jpg' | '.png'):
                        self.startImageProcessing(inputPath = self.inputPath, outputPath = self.outputPath)
                    case ('.wav' | '.mp3'):
                        self.startAudioProcessing(inputPath = self.inputPath, outputPath = self.outputPath, format = self.FileExtension.lower())
                    case ('.mp4'):
                        self.startVideoProcessing(inputPath = self.inputPath, outputPath = self.outputPath)
                    case _:
                        raise Exception(f"file extension not matched")
                    
            except Exception as e:
                raise Exception(f"matchingExtension failure {str(e)}")
        
        def startImageProcessing(self, inputPath, outputPath):
            try:
                img = Image.open(inputPath)
                img.save(outputPath, optimized = True, quality = 70)
                print(f"successMessage: file compression done with quality 70 percent")
            except Exception as e:
                raise Exception(str(e))
        
        def startAudioProcessing(self, inputPath, outputPath, format):
            process = None
            try:
                match format:
                    case '.mp3':
                        # audio = AudioSegment.from_file(inputPath, format="mp3")
                        # capturedAudioLen = len(audio)
                        # print(f"captured audio length: {capturedAudioLen} milli seconds")
                        # audioChannels = audio.channels
                        # print(f"captured audio channels: {audioChannels}")
                        # audioFramerate = audio.frame_rate
                        # print(f"captured audio frame rate: {audioFramerate}")
                        # audioSampleWidth = audio.sample_width
                        # audioSampleWidth = audioSampleWidth * 8
                        # print(f"captured audio sample width: {audioSampleWidth} bits audio")

                        ffprobeExe = shutil.which("ffprobe")
                        if not ffprobeExe:
                            raise Exception(f"ffprobe not found in PATH. Install ffmpeg and add to PATH or provide full path to ffprobe.exe")
                        
                        verifyCmd = ["ffprobe", "-v", "error", "-show_format", "-show_streams", "-print_format", "json", inputPath]
                        processOutput = subprocess.check_output(verifyCmd, text=True)
                        meta = json.dumps(json.loads(processOutput), indent=4)
                        print(f"audio file metadata: {meta}")


                        cmd = [
                            "ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", f"{inputPath}", "-b:a", "96k", "-ac", "1", "-ar", "22050", "-sample_fmt", "s16", "-progress", "pipe:1", "-nostats", f"{outputPath}"
                        ]

                        if os.name == "nt":
                            process = subprocess.Popen(cmd, shell=False, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                        else:
                            process = subprocess.Popen(cmd, shell=False, start_new_session=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                        stdout, stderr = process.communicate()
                        if process.returncode != 0:
                            raise Exception(f"ffmpeg failed: {stderr}")
                        else:
                            print(f"process standard output: {stdout}")

                            verifyCmd = ["ffprobe", "-v", "error", "-show_format", "-show_streams", "-print_format", "json", outputPath]
                            processOutput = subprocess.check_output(verifyCmd, text=True)
                            meta = json.dumps(json.loads(processOutput), indent=4)
                            print(f"compressed audio metadata: {meta}")

                        
            except Exception as e:
                raise Exception(str(e))
            except KeyboardInterrupt:
                if process and process.poll() is None:
                    if os.name == "nt":
                        process.send_signal(signal.CTRL_BREAK_EVENT)
                    else:
                        os.killpg(process.pid, signal.SIGTERM)
                    try:
                        process.wait(timeout=5)
                    except subprocess.TimeoutExpired:
                        process.kill()

        
        def startVideoProcessing(self, inputPath, outputPath):
            try:
                pass
            except Exception as e:
                raise Exception(str(e))

def main():
    try:
        com = Compression()
        pro = com.Process(com)
        # com.getExtension()
    except Exception as e:
        print(f"Message: {str(e)}")

if __name__ == "__main__":
    main()