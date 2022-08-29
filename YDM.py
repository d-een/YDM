from pytube import YouTube

print("Hello, Welcome to my custom Youtube download manager.\n Pss Leave a heart if you like it ;)")
print("Insert download link here: \n")

yt = YouTube(input())

input("Press enter to dowload:\n")

audio = yt.streams.get_audio_only()
video = yt.streams.get_highest_resolution()


audio.download()
video.download()

print("Succesful!")
input("Arigatou! See you :)")