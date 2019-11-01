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
    transcription = r.recognize_sphinx(audio)
    # transcription = "so take your seat hand close your eyes and bring your attention to the sensation of certain trish notice how the body appears in consciousness and see if you can relinquish the shape of the potter the feelers shape paid closer attention to each person station as arises and become aware of the cessation of breathing rather than focus on the breath chess notice how it appears headed the other's thoughts horizon once again drop back and simply witness i'm watch what happens to them where they go and then come back to notice and associations of breathing and said in seville at everything b. s.'s in the final minute of the session see if you can be more precise in your notice it really connect with the chips recession okay well as you open your eyes and your experience with or old seeming to rush into consciousness noticed that this is still trust your mom and everything is simply appearing sights sounds two sessions frauds and you go back today to see if you can take a few moments as you transition from one activity to the next to be aware that you are functioning in and as your mind control the calling of the rest of your day will be entirely determined by the color of your mind your experience of the world will be the totality of your reaction to your judgment of the your satisfaction or disappointment with it see if you can remember that and occasionally if only for a moment or to relinquish your reaction to experience something noticing experts and then i'll see you tomorrow for the next session of the which of course"
    return transcription


def string_are_similar(string_one, string_two):
    if(SequenceMatcher(None, string_one, string_two).ratio() < .5):
        return False
    else:
        return True


def get_list_of_waves(directory, maintain_subdirectory=False):
    if maintain_subdirectory:
        length_of_directory_offset = 0
    else:
        length_of_directory_offset = len(directory) + 1
    return [f[length_of_directory_offset:] for f in glob.glob(f"{directory}/*.wav")]


def build_list_of_transcriptions(list_of_files):
    list_of_transcriptions = []
    for file in list_of_files:
        audio = input_audio_file(file)
        transcription = transcribe_audio(audio)
        list_of_transcriptions.append({'name': file, 'transcript': transcription})

    return list_of_transcriptions


def compaire_list(list_of_transcripts):
    """
    expects a list like
        [
            {"name": "file name", "transcript":"this is a long string},
            {"name": "anouther file name", "transcript": "here is a different string"},
        ]

    it will return the name of files that are similar
    """
    list_of_similarities = []
    while (len(list_of_transcripts) > 0):
        first_item = list_of_transcripts[0]
        for i in range(1, len(list_of_transcripts)):
            current_item = list_of_transcripts[i]
            # print(f"{len(first_item['transcript'])} is the length of item one")
            # print(f"{len(current_item['transcript'])} is the length of item one")
            if(string_are_similar(first_item["transcript"], current_item["transcript"])):
                similarity = f"{first_item['name']} is similar to {current_item['name']}"
                print(similarity)
                list_of_similarities.append(similarity)
        list_of_transcripts = list_of_transcripts[1:]

    return list_of_similarities

waking_up_episodes = get_list_of_waves("source_files", maintain_subdirectory=True)
waking_up_transcriptions = build_list_of_transcriptions(waking_up_episodes)
print(compaire_list(waking_up_transcriptions))

# firstfile = input_audio_file("source_files/Daily 2018-11-10.wav")
# transcribe_audio(firstfile)
