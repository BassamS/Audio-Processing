import wave

obj = wave.open("sample.wav", "rb")

print("Number of channels", obj.getnchannels())
print("Sample width", obj.getsampwidth())
print("Frame rate", obj.getframerate())
print("Number of Frame", obj.getnframes())
print("Parameters", obj.getparams())

time_audio = obj.getframerate() / obj.getframerate()
print("Time", time_audio)

frames = obj.readframes(-1)
print(type(frames), type(frames[0]))
print(len(frames))
