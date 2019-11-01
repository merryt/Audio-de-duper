from deduper import input_audio_file, transcribe_audio
import unittest
from speech_recognition import AudioData

class newFiles(unittest.TestCase):
    def setUp(self):
        x = 1+1

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

        self.assertFail("finish tests")

        ## todo
        # follow this tutorial http://blog.justsophie.com/python-speech-to-text-with-pocketsphinx/
        # build bit to check confidence of similarity between two strings




if __name__ == '__main__':
    unittest.main(warnings='ignore')
