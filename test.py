#!/usr/bin/env python

import magic
import unittest

class MagicTest(unittest.TestCase):

    def test_magic_image(self):
        self.assertEqual(magic.from_file('data/image.png'), 'PNG image data, 144 x 60, 8-bit/color RGBA, non-interlaced')

    def test_magic_mime_image(self):
        self.assertEqual(magic.from_file('data/image.png', mime=True), 'image/png')

    def test_magic_doc(self):
        self.assertTrue(magic.from_file('data/word.doc').startswith('Composite Document File V2 Document'))

    def test_magic_mime_doc(self):
        self.assertEqual(magic.from_file('data/word.doc', mime=True), 'application/msword')


if __name__ == "__main__":
    unittest.main()
