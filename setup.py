import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sanitize_filename",
    version="1.2.0",
    author="Leo Wallentin | J++ Stockholm",
    author_email="mejl@leowallentin.se",
    description="A permissive filename sanitizer.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/jplusplus/sanitize-filename",
    packages=setuptools.find_packages(),
    python_requires='~=3.7',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
