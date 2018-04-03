""""doxygen-junit tests."""

import sys
import unittest

from doxygen_junit import DoxygenError, generate_test_suite, parse_arguments, parse_doxygen

if sys.version_info < (3, 3):  # pragma: no cover
    import mock
else:  # pragma: no cover
    from unittest import mock


class ParseDoxygenTestCase(unittest.TestCase):
    def test_single_file_warning(self):
        file_errors = parse_doxygen(
            'C:/Users/John Hagen/ClionProjects/test/main.cpp:40: warning: '
            'Compound Class is not documented.')
        self.assertEqual(len(file_errors), 1)
        for i, (filename, errors) in enumerate(file_errors.items()):
            if i == 0:  # pragma: no branch
                self.assertEqual(filename, 'C:/Users/John Hagen/ClionProjects/test/main.cpp')
                for j, error in enumerate(errors):
                    if j == 0:  # pragma: no branch
                        self.assertEqual(error.line, 40)
                        self.assertEqual(error.message, 'Compound Class is not documented.')

    def test_single_doxygen_warning(self):
        file_errors = parse_doxygen('error: Doxyfile not found and no input file specified!')
        self.assertEqual(len(file_errors), 1)
        for i, (filename, errors) in enumerate(file_errors.items()):
            if i == 0:  # pragma: no branch
                self.assertEqual(filename, 'doxygen')
                for j, error in enumerate(errors):
                    if j == 0:  # pragma: no branch
                        self.assertEqual(error.line, 0)
                        self.assertEqual(error.message,
                                         'Doxyfile not found and no input file specified!')

    def test_single_doxygen_warning_no_space(self):
        file_errors = parse_doxygen(
            r"bar.h:3:warning: the name 'FOO' supplied as the second argument in the \file "
            r'statement is not an input file')
        self.assertEqual(len(file_errors), 1)
        for i, (filename, errors) in enumerate(file_errors.items()):
            if i == 0:  # pragma: no branch
                self.assertEqual(filename, 'bar.h')
                for j, error in enumerate(errors):
                    if j == 0:  # pragma: no branch
                        self.assertEqual(error.line, 3)
                        self.assertEqual(error.message,
                                         r"the name 'FOO' supplied as the second "
                                         r'argument in the \file statement is not an input file')

    def test_single_malformed(self):
        file_errors = parse_doxygen('MALFORMED STRING')
        self.assertEqual(len(file_errors), 0)


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


class GenerateTestSuiteTestCase(unittest.TestCase):
    def test_no_errors(self):
        tree = generate_test_suite({})
        root = tree.getroot()

        self.assertEqual(root.get('errors'), str(0))
        self.assertEqual(root.get('failures'), str(0))
        self.assertEqual(root.get('tests'), str(1))
        self.assertEqual(root.get('time'), str(0))

        test_case_element = root.find('testcase')
        self.assertEqual(test_case_element.get('name'), 'no errors')

    def test_single(self):
        errors = {'file_name':
                  [DoxygenError(line=40,
                                message='Compound Class is not documented.')]}
        tree = generate_test_suite(errors)
        root = tree.getroot()
        self.assertEqual(root.get('errors'), str(1))
        self.assertEqual(root.get('failures'), str(0))
        self.assertEqual(root.get('tests'), str(1))
        self.assertEqual(root.get('time'), str(0))

        test_case_element = root.find('testcase')
        self.assertEqual(test_case_element.get('name'), 'file_name')
        self.assertEqual(test_case_element.get('file'), 'file_name')
        self.assertEqual(test_case_element.get('line'), str(40))

        error_element = test_case_element.find('error')
        self.assertEqual(error_element.get('message'), '40: Compound Class is not documented.')


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
