import unittest
from asciiii.engine.core import run


class TestBasics(unittest.TestCase):
    def test_static(self):
        config = {'file': 'data/1.jpg', 'line': 800, 'eta': 0.15, 'light': False}
        result = run(config)
        self.assertNotEqual(result, '')

    def test_light(self):
        config = {'file': 'data/2.jpg', 'line': 800, 'eta': 0.15, 'light': True}
        result = run(config)
        self.assertNotEqual(result, '')

    def test_all(self):
        config = {'line': 800, 'eta': 0.15, 'light': False}
        result = run(config)
        self.assertNotEqual(result, '')
