import os
import numpy as np
import soundfile as sf


def apply_hann_window(signal):
    """
    Apply Hann window to the given signal.
    """
    return signal * np.hanning(len(signal))


def process_audio_file(input_path, output_path):
    """
    Process an audio file by applying Hann window and save the result.
    """
    # Read the audio file
    signal, sample_rate = sf.read(input_path)

    # Apply Hann window
    windowed_signal = apply_hann_window(signal)

    # Write the processed signal to a new audio file
    sf.write(output_path, windowed_signal, sample_rate)


def process_audio_directory(input_directory, output_directory):
    """
    Process all audio files in the input directory and save them in the output directory.
    """
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Process each file in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith(".wav"):  # Process only WAV files, you can modify this if needed
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, filename)
            process_audio_file(input_path, output_path)


# Example usage:
input_dir = "rus_segments_overlap"
output_dir = "rus_window_overlap"

process_audio_directory(input_dir, output_dir)