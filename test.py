#!/usr/bin/env python

import magic
import unittest
import subprocess

class MagicTest(unittest.TestCase):

    def test_magic_mime_image(self):
        self.assertEqual(magic.from_file('data/image.png', mime=True), 'image/png')

    def test_magic_mime_doc(self):
        self.assertEqual(magic.from_file('data/word.doc', mime=True), 'application/msword')

    def test_file_image(self):
        cmd = ['file', '--mime-type', 'data/image.png']
        r = subprocess.check_output(['file', '--mime-type', 'data/image.png'])
        mime_type = r.split(":")[1].strip()
        self.assertEqual(mime_type, 'image/png')

    def test_file_doc(self):
        cmd = ['file', '--mime-type', 'data/word.doc']
        r = subprocess.check_output(['file', '--mime-type', 'data/word.doc']).strip()
        mime_type = r.split(":")[1].strip()
        self.assertEqual(mime_type, 'application/msword')



       


if __name__ == "__main__":
    unittest.main()
