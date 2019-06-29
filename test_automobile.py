import unittest
from automobile import Automobile
from unittest import TestCase


class TestAutomobile(TestCase):
    def test_ID(self):
        autoId = Automobile(123, 'sedan', 'merceedes', 'red', 1994, 2000)
        self.assertEqual(self.auto.vehicle_id, autoId)

    def test_Model(self):
        model = Automobile(123, 'sedan', 'merceedes', 'red', 1994, 2000)
        self.assertEqual(self.auto.get_model(), 'sedan')


if __name__ == '__main__':
    unittest.main()
