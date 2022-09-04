from pydub import AudioSegment

# Choose the source format
audio = AudioSegment.from_wav("sample.wav")

# Increase the volume by 6dB
audio = audio + 6

audio = audio * 2

audio = audio.fade_in(2000)

audio.export("mashup.mp3", format="mp3")

audio2 = AudioSegment.from_wav("mashup.mp3")
print("done!")
