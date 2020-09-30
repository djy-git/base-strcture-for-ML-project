"""Setup interface

1. Approach to the source code with `python setup.py 'COMMAND'`
2. Append the 'COMMAND' adding `cmdclass` in `setup`
"""


from setuptools import find_packages, setup
from setuptools import Command
from subprocess import call


class MainCommand:
    user_options = []
    def initialize_options(self):   pass
    def finalize_options(self):     pass

    @staticmethod
    def run_main(option=""):
        call(["python", "main.py", option], cwd="src")


class Log(MainCommand, Command):
    description = "Run src/main.py log"
    def run(self):
        super().run_main('log')

class Reset(MainCommand, Command):
    description = "Run src/main.py reset"
    def run(self):
        super().run_main('reset')


with open("README.md", "r") as f:
    long_description = f.read()


setup(
    name="Base project",
    author="Yoon Dongjin",
    author_email="djyoon0223@gmail.com",
    description="Short description of the project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/djy-git/base-strcture-for-ML-project",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        # "License",
        # "Environment :: GPU :: NVIDIA CUDA :: 10.2",
        "Operating System :: POSIX :: Linux"
    ],
    python_requires=">=3.7",
    cmdclass={
        "log"   : Log,
        "reset" : Reset,
    }
)