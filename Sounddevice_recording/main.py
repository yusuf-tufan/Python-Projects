import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import time

freq=48000
duration=int(input("Enter recording time in seconds:"))
record_name=input("Enter record name:")
print("Recording starts after 3 seconds...")
time.sleep(3)
recording=sd.rec(int(duration * freq),samplerate=freq,channels=2)#1 or 2 channels

sd.wait()

#write("recording0.wav",freq,recording)

wv.write(f"{record_name}.wav",recording,freq,sampwidth=2)
"""
sampwidth=3
1 8-bit Low quality (phone, old games)
2 16-bit CD quality
3 24-bit Studio quality
4 32-bit High resolution, usually float
"""