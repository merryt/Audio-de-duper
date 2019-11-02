from deduper import input_audio_file, transcribe_audio, string_are_similar, get_list_of_waves, compaire_list, has_file_been_transcribed, write_transcription_to_disk
import unittest
from speech_recognition import AudioData
import json

class newFiles(unittest.TestCase):
    def setUp(self):
        self.audio1 = "again said however is comparable then become aware of the feeling of your body rest in space you're back against the share your hands and knees see if you can arrive immediately trust fully commit the next ten minutes there's nothing i think about nothing to plan you have the rest of your day for that feel the energy of your body notice how sounds up here and disappear amateur mind to like a mirror that doesn't move to reflect what appears in a defense simply appears on it's surface and rather than try to approach the breath as though from a point outsider just let it appear in the space of warner's no need to lean into it or attempt to get closer to it shows receive a man as with the breath so too with other sensations and sounds trust with them appear on their own noticeably do in fact appear on their own and by appearing they articulate this space of consciousness as you pay attention to sensations in the body and sounds anything dogs occasional you look for the siege of attention for us isn't a very moment of hearing my voice has the sound is impinging on new year's prom as it appears in consciousness look who the one who was during his theory here in addition to the fact of hearing turn attention back on itself he even while notice in the next appearance unconscious once again cape where is wide open noticed sensations and sounds and then periodically trampling to omega struggle of that book from the one that's noticing that in that first moment of turn and see if you can observe what notice and is like what is hearing like in the first instant of looking for the one who was hearing in the last man of the practice to put you up all effort unnoticed whatever is the turnout will once again thank you for your practice house either tomorrow for the next session of the working of course"
        self.audio2 = "okay just a comparable in this matter whether on a chair or couch or a question on the floor in a position we can deal or as fine hand closed her eyes and become aware of your visual field staring to the darkness of the costars nonlinear gays in that space become very wide homes fuck you take you in your peripheral vision with your eyes closed and feel the sensation of having ahead through like most people know how this man stood the visual field the darkness into which are staring us in some way constrained by your head the evidence for which you experience not officially but cares equity you feel his position in space somehow usual tension temperature pressure and you notice his hands what should make a further observation that all of this is just appearing in consciousness consciousness is not the inside your head consciousness is not the inside or the high end the visual field everything's just appearing once again noticed your visual field notices not quite dark nurse lying he even in that darkness that somehow shimmering pay attention to all the changes you cannot thermometer lost in thought look for phone itself watch what happens to him unrest has the space in which images and sensations simply appear the last man of the session feel yourself said in which are gonna resolve and to a cloud of suspicion and moderate interest here on shown okay well again thank you for the average here making year then i'll see you tomorrow for the next session of the which of course"
        self.audio3 = "again said however is comparable then become aware of the feeling of your body rest in space you're back against the share your hands and knees see if you can arrive immediately trust fully commit the next ten minutes there's nothing i think about nothing to plan you have the rest of your day for that feel the energy of your body notice how sounds up here and disappear amateur mind you like a mirror that doesn't move to reflect what appears in a given simply appears on it's surface and rather than try to approach the breath as though from appointed outsider just let it appear in the space of warner's no need to lean into it or attempt to get closer to it just received a man as with the breath so too with other sensations and sounds trust with them appear on their own notice of the do in fact appear on their own and by appearing they articulate this base of consciousness as you pay attention to sensations in the body and sounds and even dogs occasional you look for the seat of attention from susan a very moment of hearing my voice has the sound is impinging on new year's prom as it appears in consciousness look for the one who was here in this area here in addition to the fact of hearing turn attention back on itself he even while notice in the next appearance unconscious once again cape where is wide open noticed sensations and sounds and then periodically trampling to omega struggle of that book for the one that's noticing that in that first moment of turn and see if you can observe what notice and is like what is hearing like in the first instant of looking for the one who was hearing in the last man of the practice to fuck you up all effort and notice whatever is the turnout will once again thank you for your practice house either tomorrow for the next session of the wedding of course"
        self.audio4 = "okay sit comfortably and closer eyes and tickets he knew deep breaths and become aware of this is stations a brave men were refill the most clearly hands if you can trust cover the breath in each moment we're orange skated in what that just happened rather than apply an effort or focus herself from outside the breath trust received he chooses asian n. point of course is not the breath is to call a awareness that you can find will pay attention to it and i can open up their awareness to every sensation to spot the body appear as afloat energy tangling pressure temperature whatever pierced man now become aware of any mood or motion that might be present for setting have feeling tone in your mind at the small take that to us an object of foreigners and still is with fanny fox the horizon notices undercurrent of phone has continually buffeting your attention look for the thinker hundred turn attention upon itself noticed that each next on rises entirely on sean you're not offering them and notice to this feeling of being the source of attention this feeling of being the subject confronted by objects this feeling of on a warm me is also an appearance in consciousness it feels a certain way to feel like you're directing the attention to the drawback nearly be the space in which that feeling to his horizon for alas men of the session open your eyes and gays and your visual field the trick is bigger wide and simply look at this vision of cholera why unnoticed at it too was an apparent unconscious knows everything you know in this moment is in some sense made of consciousness is no aberration of the u. to play upon him to rest as bad condition in which everything is apparent as you gaze into space taking everything and look for the center look for yourself look for your head turn attention upon itself briefly can you find your mind he is there a center to consciousness well once again thank you for taking the time to practice and it is an honor to practice with you huh i'll see you tomorrow for the next session of the wicked of course"
        self.audio5 = "once again find a comfortable posture than you might take a few deep breaths and gently close your eyes amateur mind come ter rest on the cessation of sit in the new mindset a little straighter than you were han niger spring your attention to the suspicions are britain and seated in the very attentive to what the mind is like the moment my voice intrudes was that first moment like that cashing you in a fog for the next few minutes so if you can make your attention more precise by focusing on the breath till the next inhalation from the moment it appears and cover each breath with your attention as you focus on the breath see if you feel all that you were doing that from some place safe attention itself feels located where are you paying attention to the breath from canada feels like there's some structure there for feels like patrol asian ship between the tension it's object noticed that that to his appearance in consciousness there's no place else for something to be felt were observed or noticed in any way at all hunters rest is that condition and if you notice we've been lost in thought entirely forgotten about the practice meditation is no need to judge that moment the canisters another moment the lost and gone best start again to observe whatever comes next in the last minute of the session skidded into a really precise attention to whatever spearing once again thank you for your practice our senior tomorrow for the next session of the wicked of course"
        self.list_of_files = [
            {"name": "file1.wav", "transcription": self.audio1},
            {"name": "file2.wav", "transcription": self.audio2},
            {"name": "file3.wav", "transcription": self.audio3},
            {"name": "file4.wav", "transcription": self.audio4},
            {"name": "file5.wav ", "transcription": self.audio5},
        ]
        new_file = open('testtranscriptions.json', 'w')
        new_file.write(json.dumps(self.list_of_files))

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

    def test_compairing_list_of_transcriptions(self):
        self.assertTrue(compaire_list)
        self.assertTrue(compaire_list(self.list_of_files))


    def test_reading_file_from_disk(self):
        self.assertTrue(has_file_been_transcribed)
        self.assertTrue(has_file_been_transcribed('testtranscriptions.json', 'file1.wav'), "transcription.json isn't getting read correctly from disk")

if __name__ == '__main__':
    unittest.main(warnings='ignore')
