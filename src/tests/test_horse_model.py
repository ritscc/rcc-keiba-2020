# -*- coding: utf-8 -*-
import unittest
import models


class TestHorseModel(unittest.TestCase):
    def setUp(self):
        pass

    def test_create_instance(self):
        id = 0
        name = '競走馬名'
        horse = models.Horse(
            id,
            name,
        )
        self.assertEqual(id, horse.get_id())
        self.assertEqual(name, horse.get_name())
