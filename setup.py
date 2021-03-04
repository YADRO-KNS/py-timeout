import setuptools

with open('README.md', "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name="py-timeout",
    version="0.0.1",
    author="Sergey Parshin",
    author_email="s.parshin@yadro.com",
    description="Process based timeout context decorator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YADRO-KNS/py-timeout",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
