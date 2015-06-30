"""
test_meta:
==========

A module intended for use with Nose.

"""
import random
import string
from unittest import TestCase

import plotly.plotly as py
from plotly.exceptions import PlotlyRequestError


class FolderAPITestCase(TestCase):

    def setUp(self):
        py.sign_in('PythonTest', '9v9f20pext')

    def _random_filename(self):
        random_chars = [random.choice(string.ascii_uppercase)
                        for _ in range(5)]
        unique_filename = 'Valid Folder'+''.join(random_chars)
        return unique_filename

    def test_create_folder(self):
        try:
            py.file_ops.mkdirs(self._random_filename())
        except PlotlyRequestError as e:
            self.fail('Expected this *not* to fail! Status: {}'
                      .format(e.status_code))

    def test_create_nested_folders(self):
        first_folder = self._random_filename()
        nested_folder = '{0}/{1}'.format(first_folder, self._random_filename())
        try:
            py.file_ops.mkdirs(nested_folder)
        except PlotlyRequestError as e:
            self.fail('Expected this *not* to fail! Status: {}'
                      .format(e.status_code))

    def test_duplicate_folders(self):
        first_folder = self._random_filename()
        py.file_ops.mkdirs(first_folder)
        try:
            py.file_ops.mkdirs(first_folder)
        except PlotlyRequestError as e:
            self.assertTrue(400 <= e.status_code < 500)
        else:
            self.fail('Expected this to fail!')
