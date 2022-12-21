import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sanitize_filename",
    version="1.2.2",
    author="Leo Wallentin | J++ Stockholm",
    author_email="mejl@leowallentin.se",
    description="A permissive filename sanitizer.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MaT-PT/sanitize-filename",
    packages=setuptools.find_packages(),
    python_requires='~=3.7',
    package_data = {
        "sanitize_filename": ["py.typed"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
