doxygen JUnit Converter
=======================

.. image:: https://travis-ci.com/johnthagen/doxygen-junit.svg
    :target: https://travis-ci.com/johnthagen/doxygen-junit

.. image:: https://codeclimate.com/github/johnthagen/doxygen-junit/badges/issue_count.svg
   :target: https://codeclimate.com/github/johnthagen/doxygen-junit

.. image:: https://codecov.io/github/johnthagen/doxygen-junit/coverage.svg
    :target: https://codecov.io/github/johnthagen/doxygen-junit

.. image:: https://img.shields.io/pypi/v/doxygen-junit.svg
    :target: https://pypi.python.org/pypi/doxygen-junit

.. image:: https://img.shields.io/pypi/status/doxygen-junit.svg
    :target: https://pypi.python.org/pypi/doxygen-junit

.. image:: https://img.shields.io/pypi/pyversions/doxygen-junit.svg
    :target: https://pypi.python.org/pypi/doxygen-junit/

Tool that converts `Doxygen <http://www.doxygen.org/>`_ XML output to JUnit XML
format. Use on your CI servers to get more helpful feedback.

Installation
------------

You can install, upgrade, and uninstall ``doxygen-junit`` with these commands:

.. code:: shell-session

    $ pip install doxygen-junit
    $ pip install --upgrade doxygen-junit
    $ pip uninstall doxygen-junit

Usage
-----

Redirect ``doxygen`` ``stderr`` to a file:

.. code:: shell-session

    $ doxygen 2> doxygen-stderr.txt

Convert it to JUnit XML format:

.. code:: shell-session

    $ doxygen_junit --input doxygen-stderr.txt --output doxygen-junit.xml

Contributors
------------

Credit to `@theandrewdavis <https://github.com/theandrewdavis>`_ for the initial development of
the conversion tool.

Releases
--------

2.2.0 2020-04-21
^^^^^^^^^^^^^^^^

- Drop support for Python 3.5.

2.1.0 2020-04-18
^^^^^^^^^^^^^^^^

- Add ``--version`` CLI argument.

2.0.0 2020-03-29
^^^^^^^^^^^^^^^^

- Drop Python 2.7.

1.4.0 2019-12-14
^^^^^^^^^^^^^^^^

- Drop Python 3.4 and support Python 3.8.
- Include license file.

1.3.0 - 2018-07-09
^^^^^^^^^^^^^^^^^^

Support Python 3.7.

1.2.0 - 2018-04-03
^^^^^^^^^^^^^^^^^^

- Properly support JUnit XSD.
- Drop Python 3.3 support.

1.1.0 - 2016-12-31
^^^^^^^^^^^^^^^^^^

Support Python 3.6.

1.0.1 - 2016-10-06
^^^^^^^^^^^^^^^^^^

Handle warning labels without a space before the preceding colon.

1.0.0 - 2016-09-13
^^^^^^^^^^^^^^^^^^

First release.
