import pyttsx3
import extract

class TextToSpeech:
    engine: pyttsx3.Engine

    def __init__(self, voice,rate:int, volume: float):
        self.engine = pyttsx3.init()
        if voice:
            self.engine.setProperty('voice',voice)
        self.engine.setProperty('rate',rate)
        self.engine.setProperty('volume',volume)

    def list_available_voices(self):
        voices: list= [self.engine.getProperty('voices')]
        for i, voice in enumerate(voices):
             print(f'{i+1} {voice[i].name} {voice[i].age}: {voice[i].languages} ({voice[i].gender}) [{voice[i].id}]')
 
 
    def text_to_speech(self,text:str,save:bool = False, file_name='output.mp3'):
        self.engine.say(text)
        print('I am speaking....')

        if save:
            self.engine.save_to_file(text, file_name)

        self.engine.runAndWait()

if __name__ == '__main__':
    tts = TextToSpeech('HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0', 200, 1.0)
    #tts.list_available_voices()
    tts.text_to_speech(extract.extract_text_for_audio())
    