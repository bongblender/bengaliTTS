import pyttsx3
'''pip install pyttsx3'''


def converTTS(text):
    # Hindi FM HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_hiIN_KalpanaM
    # Hindi M HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_hiIN_HemantM
    engine = pyttsx3.init("sapi5")
    engine.setProperty(
        "voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_hiIN_HemantM")
    engine.setProperty("rate", 150)
    '''SET YOUR DIRECTORY HERE, WHERE YOUR AUDIO SHOULD BE EXPORTED'''
    engine.save_to_file(text, 'CHOOSE DIRECTORY/audio.mp3')
    engine.runAndWait()
