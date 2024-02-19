import os
from pydub import AudioSegment
from pydub.silence import split_on_silence


def remove_silence(input_directory, output_directory, min_silence_len=1000, silence_thresh=-40):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Process each file in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith(".wav"):  # Adjust the extension if needed
            input_file = os.path.join(input_directory, filename)
            output_file = os.path.join(output_directory, filename)

            # Load the audio file
            audio = AudioSegment.from_file(input_file)

            # Split the audio based on silence
            chunks = split_on_silence(audio, min_silence_len=min_silence_len, silence_thresh=silence_thresh)

            # Concatenate non-silent chunks
            output = sum(chunks, AudioSegment.empty())

            # Export the output audio file
            output.export(output_file, format="wav")
            print("Silence removed and saved as:", output_file)


# Example usage:
input_directory = "input_folder"
output_directory = "output_directory"
remove_silence(input_directory, output_directory)