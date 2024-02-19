import os
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def audio_to_mel_spectrogram(audio_path, output_dir, sr=22050, n_fft=2048, hop_length=512, n_mels=128, resize_shape=(128, 128)):
    # Load audio file
    y, sr = librosa.load(audio_path, sr=sr)

    # Compute Mel-Spectrogram
    mel_spec = librosa.feature.melspectrogram(y=y, sr=sr, n_fft=n_fft, hop_length=hop_length, n_mels=n_mels)

    # Convert to decibels (log scale)
    mel_spec_db = librosa.power_to_db(mel_spec, ref=np.max)

    # Normalize values between 0 and 1
    mel_spec_db -= mel_spec_db.min()
    mel_spec_db /= mel_spec_db.max()

    # Resize spectrogram
    mel_spec_db = np.asarray(Image.fromarray(mel_spec_db).resize(resize_shape))

    # Save as PNG
    output_path = os.path.join(output_dir, os.path.splitext(os.path.basename(audio_path))[0] + '.png')
    plt.imsave(output_path, mel_spec_db, cmap='gray')

def batch_convert_to_mel_spectrograms(input_dir, output_dir):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Process each audio file in the input directory
    for file_name in os.listdir(input_dir):
        if file_name.endswith('.wav'):  # Adjust the extension as needed
            audio_path = os.path.join(input_dir, file_name)
            audio_to_mel_spectrogram(audio_path, output_dir)

# Example usage:
input_directory = "eng_window_overlap"
output_directory = "eng_mel"
batch_convert_to_mel_spectrograms(input_directory, output_directory)