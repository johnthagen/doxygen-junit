""""doxygen-junit tests."""

import sys
import unittest

from doxygen_junit import DoxygenError, parse_arguments, parse_doxygen

if sys.version_info < (3, 3):
    import mock
else:
    from unittest import mock


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


class DoxygenErrorTestCase(unittest.TestCase):
    def test_eq(self):
        self.assertEqual(DoxygenError(0, 'message'), DoxygenError(0, 'message'))

    def test_ne(self):
        self.assertNotEqual(DoxygenError(0, 'message'), DoxygenError(0, ''))
        self.assertNotEqual(DoxygenError(1, 'message'), DoxygenError(0, 'message'))
        self.assertNotEqual(DoxygenError(1, 'message'), DoxygenError(0, ''))

    def test_constructor(self):
        error = DoxygenError(0, 'message')
        self.assertEqual(error.line, 0)
        self.assertEqual(error.message, 'message')


class ParseArgumentsTestCase(unittest.TestCase):
    def test_parse_arguments(self):
        with mock.patch('doxygen_junit.argparse.ArgumentParser', autospec=True,
                        spec_set=True) as mock_argument_parser:
            args = parse_arguments()
            mock_argument_parser.assert_called_once_with(
                description='Convert doxygen output to JUnit XML format.')
            self.assertEqual(mock_argument_parser.return_value.add_argument.call_count, 2)
            mock_argument_parser.return_value.parse_args.assert_called_once_with()
            self.assertIsNotNone(args)
