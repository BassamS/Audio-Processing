import wave

# Open audio in READ binary mode!
obj = wave.open("sample.wav", "rb")

print("Number of channels", obj.getnchannels())
print("Sample width", obj.getsampwidth())
print("Frame rate", obj.getframerate())
print("Number of Frame", obj.getnframes())
print("Parameters", obj.getparams())

time_audio = obj.getframerate() / obj.getframerate()
print(time_audio)

frames = obj.readframes(-1)
print(type(frames), type(frames[0]))
print(len(frames) / 2)

obj.close()

# Open audio in WRITE binary mode!
obj_new = wave.open("new_sample.wav", "wb")

obj_new.setnchannels(1)
obj_new.setsampwidth(2)
obj_new.setframerate(8000.0)

obj_new.writeframes(frames)

obj_new.close()
