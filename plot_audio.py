import wave
import matplotlib.pyplot as plt
import numpy as np

# Open audio in READ binary mode!
obj = wave.open("sample.wav", "rb")

sample_freq = obj.getframerate()
num_samples = obj.getnframes()
signal_wave = obj.readframes(-1)

obj.close()
