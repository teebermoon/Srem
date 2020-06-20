import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="space-remover-teeber", 
    version="0.0.1",
    author="teeber",
    author_email="oldmacdonald114@yahoo.com",
    description="A program to remove spaces from a text file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/teebermoon/Srem",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
