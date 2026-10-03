from setuptools import setup, find_packages

setup(
    name="python_inspector",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "rich",
        "termgraph",
        "pyttsx3"
    ],
)