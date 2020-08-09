# -*- coding: utf-8 -*-
import unittest
from models import elements

class TestModelElements(unittest.TestCase):
    def setUp(self):
        pass

    def test_id_create(self):
        id_ = elements.ID(0)
        self.assertEqual(0, id_.get_id())

    def test_name_create(self):
        name = elements.Name('競走馬名')
        self.assertEqual('競走馬名', name.get_name())
