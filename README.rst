doxygen JUnit Converter
=======================

.. image:: https://travis-ci.org/johnthagen/doxygen-junit.svg
    :target: https://travis-ci.org/johnthagen/doxygen-junit

.. image:: https://codecov.io/github/johnthagen/doxygen-junit/coverage.svg
    :target: https://codecov.io/github/johnthagen/doxygen-junit

.. image:: https://img.shields.io/pypi/v/doxygen-junit.svg
    :target: https://pypi.python.org/pypi/doxygen-junit

.. image:: https://img.shields.io/pypi/status/doxygen-junit.svg
    :target: https://pypi.python.org/pypi/doxygen-junit

.. image:: https://img.shields.io/pypi/pyversions/doxygen-junit.svg
    :target: https://pypi.python.org/pypi/doxygen-junit/

.. image:: https://img.shields.io/pypi/dm/doxygen-junit.svg
    :target: https://pypi.python.org/pypi/doxygen-junit/

Tool that converts `doxygen <http://www.stack.nl/~dimitri/doxygen/>`_ XML output to JUnit XML format.
Use on your CI servers to get more helpful feedback.

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

    $ doxygen_junit doxygen-stderr.txt doxygen-junit.xml

Releases
--------

1.0.0 - 2016-03-05
^^^^^^^^^^^^^^^^^^

First release.
