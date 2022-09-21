import pyttsx3

engine = pyttsx3.init()


# voices = engine.getProperty('voices')
# for voice in voices:
#     print("Voice: %s" % voice.name)
#     print(" - ID: %s" % voice.id)
#     print(" - Languages: %s" % voice.languages)
#     print(" - Gender: %s" % voice.gender)
#     print(" - Age: %s" % voice.age)
#     print("\n")

# output:
# Voice: Zuzana
#  - ID: com.apple.speech.synthesis.voice.zuzana
#  - Languages: ['cs_CZ']
#  - Gender: VoiceGenderFemale
#  - Age: 35


# https://stackoverflow.com/questions/65977155/change-pyttsx3-language
def change_voice(engine, language, gender='VoiceGenderFemale'):
    for voice in engine.getProperty('voices'):
        if language in voice.languages and gender == voice.gender:
            engine.setProperty('voice', voice.id)
            return True

    raise RuntimeError("Language '{}' for gender '{}' not found".format(language, gender))

change_voice(engine, "zh_CN", "VoiceGenderFemale")

# engine.say("hello")
# engine.say("你好")
# engine.save_to_file("hello","output.mp3")

f = open("text.txt", "r")
text = f.read()

engine.save_to_file(text, "output.mp3")
engine.runAndWait()
