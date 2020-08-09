# -*- coding: utf-8 -*-
import unittest
from models import attributes

class TestModelAttributes(unittest.TestCase):
    def setUp(self):
        pass

    def test_id_create(self):
        id_ = attributes.ID(0)
        self.assertEqual(0, id_.get_attr())

    def test_name_create(self):
        name = attributes.Name('競走馬名')
        self.assertEqual('競走馬名', name.get_attr())
