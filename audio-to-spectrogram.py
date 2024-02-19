import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

def create_spectrogram(audio_file):
    # Load the audio file
    y, sr = librosa.load(audio_file)
    print(audio_file)
    # Generate a Mel-scaled power spectrogram
    spectrogram = librosa.feature.melspectrogram(y=y, sr=sr)

    # Convert to log scale (dB)
    log_spectrogram = librosa.power_to_db(spectrogram, ref=np.max)

    # Display the spectrogram
    plt.figure(figsize=(12, 4))
    librosa.display.specshow(log_spectrogram, sr=sr, x_axis='time', y_axis='mel')
    plt.title('Mel power spectrogram')
    plt.colorbar(format='%+02.0f dB')
    plt.tight_layout()
    plt.show()


# Replace 'audio_file.wav' with your audio file
create_spectrogram('test_spectrogram/b.wav')