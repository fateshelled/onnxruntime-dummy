
from setuptools import setup, find_packages
from os import path
import re

package_name="onnxruntime"
root_dir = path.abspath(path.dirname(__file__))

version = '99.99.99'

setup(
    name=package_name,
    version=version,
    description="ONNX Runtime Dummy",
    long_description="",
    author="fateshelled",
    author_email="",
    url="https://github.com/fateshelled/onnxruntime-dummy",
    license="MIT License",
    packages=find_packages(),
    platforms=["linux", "unix"],
    python_requires=">=3.6",
    install_requires = [
    ],
)
