import speech_recognition as sr
from difflib import SequenceMatcher
import glob
import json
import pprint

r = sr.Recognizer()


def write_transcription_to_disk(file_name, transcription, json_file_name='transcriptions.json'):
    audio_pair = {"name": file_name, "transcription": transcription}
    with open(json_file_name, 'r+') as json_outfile:
        contents_of_file = json.load(json_outfile)
        contents_of_file.append(audio_pair)
        json_outfile.seek(0)
        json_outfile.write(json.dumps(contents_of_file))


def has_file_been_transcribed(storage_file_name, audio_file_name):
    """
    Inputs name of a file that has transcriptions, and name of audio file
    opens that file up and checks to see if that audio has been transcribed, if the file doesn't exist it returns false
    """

    with open(storage_file_name) as json_file:
        data = json.load(json_file)
        for audio_pair in data:
            if audio_pair["name"] == audio_file_name:
                return audio_pair

    return False


def input_audio_file(filename):
    audio_file = sr.AudioFile(filename)
    with audio_file as source:
        audio = r.record(source)
    return audio


def transcribe_audio(audio):
    transcription = r.recognize_sphinx(audio)
    #transcription = "so take your seat hand close your eyes and bring your attention to the sensation of certain trish notice how the body appears in consciousness and see if you can relinquish the shape of the potter the feelers shape paid closer attention to each person station as arises and become aware of the cessation of breathing rather than focus on the breath chess notice how it appears headed the other's thoughts horizon once again drop back and simply witness i'm watch what happens to them where they go and then come back to notice and associations of breathing and said in seville at everything b. s.'s in the final minute of the session see if you can be more precise in your notice it really connect with the chips recession okay well as you open your eyes and your experience with or old seeming to rush into consciousness noticed that this is still trust your mom and everything is simply appearing sights sounds two sessions frauds and you go back today to see if you can take a few moments as you transition from one activity to the next to be aware that you are functioning in and as your mind control the calling of the rest of your day will be entirely determined by the color of your mind your experience of the world will be the totality of your reaction to your judgment of the your satisfaction or disappointment with it see if you can remember that and occasionally if only for a moment or to relinquish your reaction to experience something noticing experts and then i'll see you tomorrow for the next session of the which of course"
    return transcription


def string_are_similar(string_one, string_two):
    if (SequenceMatcher(None, string_one, string_two).ratio() < .1):
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
        audio_pair = has_file_been_transcribed("transcriptions.json", file)
        if audio_pair:
            list_of_transcriptions.append(audio_pair)
        else:
            transcription = transcribe_audio(audio)
            write_transcription_to_disk(file, transcription)
            list_of_transcriptions.append({'name': file, 'transcription': transcription})
            pprint.pprint({'name': file, 'transcription': transcription})
    return list_of_transcriptions


def compaire_list(list_of_transcripts):
    """
    expects a list like
        [
            {"name": "file name", "transcription":"this is a long string},
            {"name": "anouther file name", "transcription": "here is a different string"},
        ]

    it will return the name of files that are similar
    """
    list_of_similarities = []
    while (len(list_of_transcripts) > 0):
        first_item = list_of_transcripts[0]
        for i in range(1, len(list_of_transcripts)):
            current_item = list_of_transcripts[i]
            if (string_are_similar(first_item["transcription"], current_item["transcription"])):
                similarity = f"{first_item['name']} is similar to {current_item['name']}"
                list_of_similarities.append(similarity)
        list_of_transcripts = list_of_transcripts[1:]

    return list_of_similarities


try:
    with open('transcriptions.json', 'r') as outfile:
        json.load(outfile)
except:
    new_file = open('transcriptions.json', 'w')
    new_file.write("[]")




# first_file_name = "source_files/Daily 2018-11-10.wav"
# firstfile = input_audio_file(first_file_name)
# transcribed_audio = transcribe_audio(firstfile)
# write_transcription_to_disk(first_file_name, transcribed_audio)




#
#
# waking_up_episodes = get_list_of_waves("source_files", maintain_subdirectory=True)
# waking_up_transcriptions = build_list_of_transcriptions(waking_up_episodes)
# print(compaire_list(waking_up_transcriptions))
