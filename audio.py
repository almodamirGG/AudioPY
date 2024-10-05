from gtts import gTTS

# Data
txt = "bonjour"
langue = 'en'

# pass data as parametre
res = gTTS(text=txt,lang=langue)
res.save("audio mp4")