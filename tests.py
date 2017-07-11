#!/usr/bin/env python
from __future__ import absolute_import
from unittest import main, TestCase

from blurhash import encode


class BlurhashEncodeTestCase(TestCase):

    def test_encode_file(self):
        with open('pic2.png', 'rb') as image_file:
            result = encode(image_file, 4, 3)

        self.assertEqual(result, 'jaMpGa00;;8hjal6hr8yhlmYhkqG')

    def test_encode_with_filename(self):
        result = encode('pic2.png', 4, 3)
        self.assertEqual(result, 'jaMpGa00;;8hjal6hr8yhlmYhkqG')

    def test_invalid_image(self):
        with self.assertRaises(IOError):
            encode('encode.c', 4, 3)

    def test_invalid_x_components(self):
        with self.assertRaises(ValueError):
            encode('pic2.png', 9, 3)

        with self.assertRaises(ValueError):
            encode('pic2.png', 0, 3)

    def test_invalid_y_components(self):
        with self.assertRaises(ValueError):
            encode('pic2.png', 4, 9)

        with self.assertRaises(ValueError):
            encode('pic2.png', 4, 0)


if __name__ == '__main__':
    main()