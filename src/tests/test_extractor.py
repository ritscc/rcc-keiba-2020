import unittest
import datetime
import model.attribute as attrs
from extractor import RaceExtractor


class TestPostTextBuilder(unittest.TestCase):
    def setUp(self):
        self.race_extractor = RaceExtractor(attrs)

    @unittest.skip('Seleniumを利用した重いテストのため')
    def test_fetch_race_id(self):
        race_id = self.race_extractor.fetch_race_id_list(
            datetime.date(2020, 8, 8))
        self.assertEqual('202004020501', race_id[0].attr)

    def test_fetch_race_data(self):
        race_id = '202004020501'
        race_data = self.race_extractor.fetch_race_data(attrs.RaceID(race_id))
        self.assertEqual('芝', race_data['馬場状態'].attr)
        self.assertEqual(1600, race_data['走距離'].attr)
        self.assertEqual('雨', race_data['天気'].attr)
        self.assertEqual(1, race_data['競走馬'][0]['着順'])
        self.assertEqual(8, race_data['競走馬'][0]['枠'])
        self.assertEqual('牡', race_data['競走馬'][0]['性別'])
        self.assertEqual(2, race_data['競走馬'][0]['年齢'])
        self.assertEqual(54.0, race_data['競走馬'][0]['斤量'])
        self.assertEqual(6.5, race_data['競走馬'][0]['オッズ'])
        self.assertEqual(488, race_data['競走馬'][0]['体重'])
        self.assertEqual(-2, race_data['競走馬'][0]['体重増減'])
