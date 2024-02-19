import os
import librosa
import numpy as np

def extract_mfcc(audio_path, output_dir):
    # Load audio file
    y, sr = librosa.load(audio_path, sr=None)

    # Extract MFCC features
    mfcc = librosa.feature.mfcc(y=y, sr=sr)

    # Save MFCC features to a file
    output_filename = os.path.basename(audio_path).split('.')[0] + '.npy'
    output_path = os.path.join(output_dir, output_filename)
    np.save(output_path, mfcc)

def process_audio_files(input_dir, output_dir):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Process each audio file in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith('.wav'):  # Adjust file extension if necessary
            audio_path = os.path.join(input_dir, filename)
            extract_mfcc(audio_path, output_dir)


if __name__ == "__main__":
    input_directory = "eng_window_overlap"  # Directory containing audio files
    output_directory = "eng_MFCC"  # Directory to save MFCC files

    process_audio_files(input_directory, output_directory)