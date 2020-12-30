#!/usr/bin/env python3

import setuptools

setuptools.setup(
    name="doxygen-junit",
    version="2.2.1",  # Keep in sync with __version__.
    description="Converts doxygen errors and warnings to JUnit XML format.",
    long_description=open("README.rst").read(),
    keywords="doxygen C C++ JUnit",
    author="John Hagen",
    author_email="johnthagen@gmail.com",
    url="https://github.com/johnthagen/doxygen-junit",
    py_modules=["doxygen_junit"],
    install_requires=open("requirements.txt").readlines(),
    python_requires=">=3.6",
    license="MIT",
    license_files=["LICENSE.txt"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: C",
        "Programming Language :: C++",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Documentation",
        "Topic :: Software Development :: Documentation",
        "Topic :: Software Development :: Quality Assurance",
    ],
    scripts=["doxygen_junit.py"],
    entry_points={
        "console_scripts": [
            "doxygen_junit = doxygen_junit:main",
        ],
    },
)
