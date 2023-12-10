import unittest
from one_hot_encoder import fit_transform


class TestFitTransform(unittest.TestCase):
    def test_empty_input(self):
        with self.assertRaises(TypeError):
            fit_transform()


    def test_simple_input(self):
        result = fit_transform('a')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], ('a', [1]))


    def test_multiple_inputs(self):
        result = fit_transform('a', 'b', 'c', 'a', 'b')
        self.assertEqual(len(result), 5)


    def test_non_string_input(self):
        # TODO
        result = fit_transform(['a', 'b', 'c'])
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0][0], 'a')


    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            fit_transform(1, 2, 3)


    def test_duplicate_input(self):
        result = fit_transform('a', 'b', 'c', 'a', 'b')
        self.assertEqual(len(result), 5)
        self.assertEqual(result[0][0], 'a')
        self.assertEqual(result[0][1], [0, 0, 1])


if __name__ == '__main__':
    unittest.main()
