import numpy as np
import wave
import sys
import os
import time
from moviepy.editor import AudioFileClip, ColorClip, CompositeVideoClip, TextClip, concatenate_videoclips



# python file-audio.py <input.file> <output.wav>

#input_file = sys.argv[1]
#output_file = sys.argv[2]

input_file="graphics.png"
output_file = "ENCODED.wav"



def encode_file_to_audio(input_file_path, output_audio_path):
    # Read the input file as binary or text
    with open(input_file_path, 'rb') as file:
        file_data = file.read()

    # Convert the file data to a numpy array
    audio_data = np.frombuffer(file_data, dtype=np.uint8)

    # Create a mono audio stream with the audio data
    audio_stream = wave.open(output_audio_path, 'w')
    audio_stream.setnchannels(1)
    audio_stream.setsampwidth(1)
    audio_stream.setframerate(44100)  # Standard audio frequency

    # Write the audio data to the audio stream
    audio_stream.writeframes(audio_data.tobytes())
    audio_stream.close()

# Example usage
try:
    encode_file_to_audio(input_file, output_file)
except:
    print("File not found!")

print("done encoding to audio.")


exit()


# Path to the input .wav file
input_audio_file = "temp.wav"

# Duration of the blank video (in seconds) based on the audio duration
audio_clip = AudioFileClip(input_audio_file)
duration = audio_clip.duration

# Create a blank video with the same duration as the audio
video_clip = ColorClip(size=(100, 100), color=(5, 10, 13), duration=duration)

# Set the audio of the blank video as the input audio
video_clip = video_clip.set_audio(audio_clip)

# Set the frames per second for the output video
fps = 24

# Output path for the final .mp4 file
output_video_file = input_file + ".mp4"

# Save the final video file
video_clip.write_videofile(output_video_file, codec="libx264", audio_codec="aac", fps=fps)

#os.remove("temp.wav")


