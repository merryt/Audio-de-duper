import speech_recognition as sr
from difflib import SequenceMatcher
import glob


r = sr.Recognizer()

def input_audio_file(filename):
    audio_file = sr.AudioFile(filename)
    with audio_file as source:
        audio = r.record(source)
    return audio


def transcribe_audio(audio):
    # transcription = r.recognize_sphinx(audio)
    transcription = "so take your seat hand close your eyes and bring your attention to the sensation of certain trish notice how the body appears in consciousness and see if you can relinquish the shape of the potter the feelers shape paid closer attention to each person station as arises and become aware of the cessation of breathing rather than focus on the breath chess notice how it appears headed the other's thoughts horizon once again drop back and simply witness i'm watch what happens to them where they go and then come back to notice and associations of breathing and said in seville at everything b. s.'s in the final minute of the session see if you can be more precise in your notice it really connect with the chips recession okay well as you open your eyes and your experience with or old seeming to rush into consciousness noticed that this is still trust your mom and everything is simply appearing sights sounds two sessions frauds and you go back today to see if you can take a few moments as you transition from one activity to the next to be aware that you are functioning in and as your mind control the calling of the rest of your day will be entirely determined by the color of your mind your experience of the world will be the totality of your reaction to your judgment of the your satisfaction or disappointment with it see if you can remember that and occasionally if only for a moment or to relinquish your reaction to experience something noticing experts and then i'll see you tomorrow for the next session of the which of course"
    return transcription


def string_are_similar(string_one, string_two):
    if(SequenceMatcher(None, string_one, string_two).ratio() < .5):
        return False
    else:
        return True

def get_list_of_waves(directory):
    lenth_of_directory = len(directory)
    return [f[lenth_of_directory+1:] for f in glob.glob(f"{directory}/*.wav")]

# firstfile = input_audio_file("source_files/Daily 2018-11-10.wav")
# transcribe_audio(firstfile)
