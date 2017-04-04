import unittest


from dataframe_builder import build_dataframe


class TestBuilder(unittest.TestCase):
    def test_returns_3_frames(self):
        result = build_dataframe()
        self.assertEqual(len(result), 3)
