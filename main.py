import wave

obj = wave.open("sample.wave", "rb")

print("Number of channels", obj.getnchannels())
print("Sample width", obj.getsampwidth())
print("Frame rate", obj.getframerate())
print("Number of Frame", obj.getnframes())
