#!/usr/bin/env python

import magic
import unittest

class MagicTest(unittest.TestCase):

    def test_magic(self):
        self.assertEqual(magic.from_file('image.png'), 'PNG image data, 144 x 60, 8-bit/color RGBA, non-interlaced')

    def test_magic_mime(self):
        self.assertEqual(magic.from_file('image.png', mime=True), 'image/png')


if __name__ == "__main__":
    unittest.main()
