from pydub import AudioSegment
import os


def split_audio_into_segments(input_folder, output_folder, segment_length_ms=3000, overlap_ms=500):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Process each audio file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".wav"):
            # Load the audio file
            input_file = os.path.join(input_folder, filename)
            audio = AudioSegment.from_file(input_file)

            # Calculate the total number of segments
            num_segments = (len(audio) - overlap_ms) // (segment_length_ms - overlap_ms)

            # Split audio into segments
            for i in range(num_segments):
                start_time = i * (segment_length_ms - overlap_ms)
                end_time = start_time + segment_length_ms
                segment = audio[start_time:end_time]

                # Export segment to a file
                output_file = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_segment_{i+1}.wav")
                segment.export(output_file, format="wav")

            print(f"{num_segments} segments created for {filename}.")

# Example usage:
input_folder = "rus_wav"
output_folder = "rus_segments_overlap"
segment_length_ms = 3000
overlap_ms = 100
split_audio_into_segments(input_folder, output_folder, segment_length_ms, overlap_ms)