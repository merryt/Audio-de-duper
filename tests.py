from deduper import input_audio_file, transcribe_audio, string_are_similar, get_list_of_waves
import unittest
from speech_recognition import AudioData


class newFiles(unittest.TestCase):
    def setUp(self):
        self.audio1 = "so take your seat hand close your eyes and bring your attention to the sensation of certain trish notice how the body appears in consciousness and see if you can relinquish the shape of the potter the feelers shape paid closer attention to each person station as arises and become aware of the cessation of breathing rather than focus on the breath chess notice how it appears headed the other's thoughts horizon once again drop back and simply witness i'm watch what happens to them where they go and then come back to notice and associations of breathing and said in seville at everything b. s.'s in the final minute of the session see if you can be more precise in your notice it really connect with the chips recession okay well as you open your eyes and your experience with or old seeming to rush into consciousness noticed that this is still trust your mom and everything is simply appearing sights sounds two sessions frauds and you go back today to see if you can take a few moments as you transition from one activity to the next to be aware that you are functioning in and as your mind control the calling of the rest of your day will be entirely determined by the color of your mind your experience of the world will be the totality of your reaction to your judgment of the your satisfaction or disappointment with it see if you can remember that and occasionally if only for a moment or to relinquish your reaction to experience something noticing experts and then i'll see you tomorrow for the next session of the which of course"
        self.audio2 = "test"
        self.audio3 = "so take your seat hand close your eyes and bring your attention to the sensation of your break notice how the body appears in consciousness and see if you can relinquish the shape of the mouth the feelers shape paid closer attention to each person station as arises and become aware of the cessation of breathing rather than focus on the breath chess notice how it appears headed the other's thoughts horizon once again drop back and simply witness i'm watch what happens to them where they go and then come back to notice and associations of breathing and said in seville at everything b. s.'s in the final minute of the session see if you can be more precise in your notice it really connect with the chips recession okay well as you open your eyes and your experience with or old seeming to rush into consciousness noticed that this is still trust your mom and everything is simply appearing sights sounds two sessions frauds and you go back today to see if you can take a few moments as you transition from one activity to the next to be aware that you are functioning in and as your mind control the calling of the rest of your day will be entirely determined by the color of your mind your experience of the world will be the totality of your reaction to your judgment of the your satisfaction or disappointment with it see if you can remember that and occasionally if only for a moment or to relinquish your reaction to experience something noticing experts and then i'll see you tomorrow for the next session of the which of course"


    def test_inputing_a_file(self):
        # make sure function exists
        self.assertTrue(input_audio_file)

        # make sure inputing a file is returning audio data
        self.assertEqual(type(input_audio_file("source_files/Daily 2018-11-10.wav")), AudioData)

    def test_transcribing_audio(self):

        # do we have a function
        self.assertTrue(transcribe_audio)

        #does it return words
        sample_audio = input_audio_file("source_files/Daily 2018-11-10.wav")
        self.assertEqual(type(transcribe_audio(sample_audio)), str)

    def test_similarity_of_strings(self):
        self.assertTrue(string_are_similar)
        self.assertFalse(string_are_similar(self.audio1, self.audio2))
        self.assertTrue(string_are_similar(self.audio1, self.audio3))

    def test_getting_list_of_waves(self):
        self.assertTrue(get_list_of_waves)
        self.assertIn("Daily 2018-11-10.wav", get_list_of_waves("source_files"))


if __name__ == '__main__':
    unittest.main(warnings='ignore')
