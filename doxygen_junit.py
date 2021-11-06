#!/usr/bin/env python3

"""Converts doxygen errors and warnings to Junit format."""

import argparse
import collections
import re
import sys
from typing import Dict, Set
from xml.etree import ElementTree

from exitstatus import ExitStatus

__version__ = "2.3.0"


class DoxygenError:
    def __init__(self, line: int, message: str) -> None:
        """Constructor.

        Args:
            line: Line number of error.
            message: Message associated with the error.
        """
        self.line = line
        self.message = message

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.line, self.message))


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Convert doxygen output to JUnit XML format.")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument("-i", "--input", required=True, help="Doxygen stderr file to parse.")

    default_output_file = "doxygen-junit.xml"
    parser.add_argument(
        "-o",
        "--output",
        default=default_output_file,
        help="Output JUnit XML file. (Default: {})".format(default_output_file),
    )
    return parser.parse_args()


def main() -> ExitStatus:  # pragma: no cover
    """Run doxygen_junit.

    When a doxygen stderr file is passed with --input, parse the file and write it to the file
    passed with --output in JUnit XML format.

    Returns:
        ExitStatus.success if successful, ExitStatus.failure if failed.
    """
    args = parse_arguments()

    try:
        tree = generate_test_suite(parse_doxygen(open(args.input).read()))
        tree.write(args.output, encoding="utf-8", xml_declaration=True)
    except IOError as e:
        print(str(e), file=sys.stderr)
        return ExitStatus.failure

    return ExitStatus.success


def parse_doxygen(error_text: str) -> Dict[str, Set[DoxygenError]]:
    """Parses doxygen output.

    Generic doxygen messages use 'doxygen' as the file name.

    Args:
        error_text: doxygen stderr.

    Returns:
        Doxygen errors grouped by file name.
    """
    errors = collections.defaultdict(set)
    for line in error_text.split("\n"):
        line = line.rstrip()
        match = re.search(r"(.+):(\d+):\s*(error|warning):\s+(.*)", line)
        if match is not None:
            filename = match.group(1)
            errors[filename].add(DoxygenError(line=int(match.group(2)), message=match.group(4)))
        else:
            match = re.search(r"^(error|warning):\s+(.*)$", line)
            if match is not None:
                errors["doxygen"].add(DoxygenError(line=0, message=match.group(2)))
    return errors


def generate_test_suite(
    errors_by_filename: Dict[str, Set[DoxygenError]]
) -> ElementTree.ElementTree:
    """Generates JUnit XML file from parsed errors.

    Args:
        errors_by_filename: Doxygen errors.

    Returns:
        XML test suite.
    """
    test_suite = ElementTree.Element("testsuite")
    test_suite.attrib["failures"] = str(0)
    test_suite.attrib["name"] = "doxygen"
    test_suite.attrib["time"] = str(0)

    # If no errors, create a blank test case.
    if len(errors_by_filename) == 0:
        test_suite.attrib["tests"] = str(1)
        test_suite.attrib["errors"] = str(0)
        ElementTree.SubElement(test_suite, "testcase", name="no errors")
    else:
        test_suite.attrib["errors"] = str(len(errors_by_filename))
        test_suite.attrib["tests"] = str(len(errors_by_filename))
        for filename, errors in errors_by_filename.items():
            for error in errors:
                test_case = ElementTree.SubElement(
                    test_suite, "testcase", name=filename, file=filename, line=str(error.line)
                )
                ElementTree.SubElement(
                    test_case, "error", message="{}: {}".format(error.line, error.message)
                )

    return ElementTree.ElementTree(test_suite)


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
