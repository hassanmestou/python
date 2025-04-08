import playsound
playsound.init()
playsound.mixer.music.load('down.mp3')
playsound.mixer.music.play()
playsound.event.wait()