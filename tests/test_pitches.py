import unittest
from app.models import Pitches,User
from app import db

class PitchesModelTest(unittest.TestCase):

    def setUp(self):
        self.user_James = User(username = 'James', email = 'james@ms.com')

        self.new_pitch = Pitches(title = 'New Pitch', pitch = 'This is a new pitch',category = 'interview')

    def tearDown(self):
        Pitches.query.delete()
        User.query.delete()

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitches.query.all())>0)