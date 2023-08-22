import wave

def decode_audio_to_file(input_audio_path, output_file_path):
    # Read the audio file
    audio_stream = wave.open(input_audio_path, 'r')

    # Read the audio frames as bytes
    audio_frames = audio_stream.readframes(audio_stream.getnframes())

    # Write the audio frames to the output file
    with open(output_file_path, 'wb') as file:
        file.write(audio_frames)

    audio_stream.close()

# Example usage
decode_audio_to_file('audio.wav', 'decoded.exe')
