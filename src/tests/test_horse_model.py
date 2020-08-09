# -*- coding: utf-8 -*-
import unittest
from models import *


class TestHorseModel(unittest.TestCase):
    def setUp(self):
        pass

    def test_create_instance(self):
        id = 0
        name = '競走馬名'
        horse_ = horse.Horse(
            id,
            name,
        )
        self.assertEqual(id, horse_.get_id())
        self.assertEqual(name, horse_.get_name())
