#!/usr/bin/env python3

"""doxygen-junit tests."""

import unittest

from doxygen_junit import parse_doxygen


class ParseDoxygenTestCase(unittest.TestCase):
    def test_single_file_warning(self):
        file_errors = parse_doxygen(
            'C:/Users/John Hagen/ClionProjects/test/main.cpp:40: warning: '
            'Compound Class is not documented.')
        for i, (filename, errors) in enumerate(file_errors.items()):
            if i == 0:
                self.assertEqual(filename, 'C:/Users/John Hagen/ClionProjects/test/main.cpp')
                for j, error in enumerate(errors):
                    if j == 0:
                        self.assertEqual(error.line, 40)
                        self.assertEqual(error.message, 'Compound Class is not documented.')

    def test_single_doxygen_warning(self):
        file_errors = parse_doxygen('error: Doxyfile not found and no input file specified!')
        for i, (filename, errors) in enumerate(file_errors.items()):
            if i == 0:
                self.assertEqual(filename, 'doxygen')
                for j, error in enumerate(errors):
                    if j == 0:
                        self.assertEqual(error.line, 0)
                        self.assertEqual(error.message,
                                         'Doxyfile not found and no input file specified!')
