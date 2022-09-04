import wave
import matplotlib.pyplot as plt
import numpy as np

# Open audio in READ binary mode!
obj = wave.open("sample.wav", "rb")

sample_freq = obj.getframerate()
num_samples = obj.getnframes()
signal_wave = obj.readframes(-1)

obj.close()

# Length of audio in seconds
t_audio = num_samples / sample_freq

print(t_audio)

signal_array = np.frombuffer(signal_wave, dtype=np.int16)

times = np.linspace(0, t_audio, num=num_samples)

plt.figure(figsize=(15, 5))
plt.plot(times, signal_array)
plt.title("Audio Signal")
plt.ylabel("Signal Wave")
plt.xlabel("Time (s)")
plt.xlim(0, t_audio)
plt.show()
