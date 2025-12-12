import os
import sys
import json
import signal
import shutil
import subprocess
from PIL import Image
from pydub import AudioSegment

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
            raise Exception(f"Get input output path failure {str(e)}")
        
    class Process:
        def __init__(self, com):
            self.inputPath, self.outputPath, self.FileExtension  = com.getInputOutputPath()
            print(f"InputPath: {self.inputPath}\nOutputPath: {self.outputPath}\nFile Extension: {self.FileExtension}")

            self.matchingExtension()
        
        def matchingExtension(self):
            try:
                match (self.FileExtension.lower()):
                    case ('.jpg' | '.png'):
                        self.startImageProcessing(inputPath = self.inputPath, outputPath = self.outputPath)
                    case ('.wav' | '.mp3'):
                        self.startAudioProcessing(inputPath = self.inputPath, outputPath = self.outputPath, format = self.FileExtension.lower())
                    case ('.mp4' | '.mkv'):
                        self.startVideoProcessing(inputPath = self.inputPath, outputPath = self.outputPath, format = self.FileExtension.lower())
                    case _:
                        raise Exception(f"File extension not matched")
                    
            except Exception as e:
                raise Exception(f"Matching extension failure {str(e)}")
        
        def startImageProcessing(self, inputPath, outputPath):
            try:
                img = Image.open(inputPath)
                img.save(outputPath, optimized = True, quality = 70)
                print(f"Success message: file compression done with quality 70 percent")
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
                            raise Exception(f"FFprobe not found in PATH. Install ffmpeg and add to PATH or provide full path to ffprobe.exe")
                        
                        verifyCmd1 = ["ffprobe", "-v", "error", "-show_format", "-show_streams", "-print_format", "json", inputPath]
                        processOutput1 = subprocess.check_output(verifyCmd1, text=True)
                        metadata = json.loads(processOutput1)
                        fileSizeBeforeCompression = int(metadata.get("format", {}).get("size"))
                        print(f"Audio file metadata: {json.dumps(metadata, indent=4)}")
                        print(f"Audio file size before compression: {fileSizeBeforeCompression}")

                        compressionCmd = [
                            "ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", f"{inputPath}", "-b:a", "96k", "-ac", "1", "-ar", "22050", "-sample_fmt", "s16", "-progress", "pipe:1", "-nostats", f"{outputPath}"
                        ]

                        if os.name == "nt":
                            process = subprocess.Popen(compressionCmd, shell=False, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                        else:
                            process = subprocess.Popen(compressionCmd, shell=False, start_new_session=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                        stdout, stderr = process.communicate()
                        if process.returncode != 0:
                            raise Exception(f"FFmpeg failed: {stderr}")
                        else:
                            print(f"Process standard output: {stdout}")

                            verifyCmd2 = ["ffprobe", "-v", "error", "-show_format", "-show_streams", "-print_format", "json", outputPath]
                            processOutput2 = subprocess.check_output(verifyCmd2, text=True)
                            metadata = json.loads(processOutput2)
                            fileSizeAfterCompression = int(metadata.get("format", {}).get("size"))
                            print(f"Compressed audio metadata: {json.dumps(metadata, indent=4)}")
                            print(f"Audio file size after compression: {fileSizeAfterCompression}")

                            if fileSizeAfterCompression < fileSizeBeforeCompression:
                                compressedPercent = self.findCompressionPercentage(valueBefore=fileSizeBeforeCompression, valueAfter=fileSizeAfterCompression)
                                print(f"Compressed percentage: {compressedPercent:.2f}%")

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

        def findCompressionPercentage(self, valueBefore, valueAfter):
            print(f"Figuring out how much a file has been reduced after compression")
            if valueBefore == 0:
                raise Exception("Find compression percentage function raise zero division error")
            
            return float(((valueBefore - valueAfter) / valueBefore) * 100.00)
        
        def startVideoProcessing(self, inputPath, outputPath, format):
            process = None
            try:
                match format:
                    case ".mkv":
                        if os.name == "nt":
                            ffprobeExe = shutil.which("ffprobe")
                            if not ffprobeExe:
                                raise Exception(f"FFprobe not found in PATH. Install ffmpeg and add to PATH or provide full path to ffprobe.exe")
                            
                            videoMetaCheckBeforeCompressionCmd = [
                                "ffprobe",
                                "-v",
                                "error",
                                "-show_format",
                                "-show_streams",
                                "-print_format",
                                "json",
                                inputPath
                            ]

                            processOutput1 = subprocess.check_output(args=videoMetaCheckBeforeCompressionCmd, text=True)
                            metadata = json.loads(processOutput1)
                            fileSizeBeforeCompression = int(metadata.get("format", {}).get("size"))
                            print(f"Video file metadata befor compression: {json.dumps(metadata, indent=4)}")
                            print(f"Video size before compression: {fileSizeBeforeCompression}")
                            
                            videoCompressionCmd = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", inputPath, "-vcodec", "libx264", "-crf", "28", "-preset", "fast", "-acodec", "aac", "-b:a", "96k", outputPath]
                            process = subprocess.run(args=videoCompressionCmd, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

                            stdout, stderr = process.communicate()
                            returnCode = process.returncode
                            if returnCode != 0:
                                raise Exception(f"FFmpeg failed: {stderr}")
                            else:
                                print(f"Video file compression done successfully")
                                print(f"Process standard output: {stdout}")

                                videoMetaCheckAfterCompressionCmd = [
                                "ffprobe",
                                "-v",
                                "error",
                                "-show_format",
                                "-show_streams",
                                "-print_format",
                                "json",
                                outputPath
                            ]

                            processOutput2 = subprocess.check_output(args=videoMetaCheckAfterCompressionCmd, text=True)
                            metadata = json.loads(processOutput2)
                            fileSizeAfterCompression = int(metadata.get("format", {}).get("size"))
                            print(f"Video file metadata after compression: {json.dumps(metadata, indent=4)}")
                            print(f"Video size after compression: {fileSizeAfterCompression}")
                        
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