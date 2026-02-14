"""
Setup configuration for LAN File Share
Allows the project to be installed as a Python package
"""

from setuptools import setup, find_packages

# Read the README file for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="lan-file-share",
    version="1.0.0",
    author="Your Name",
    author_email="thelkotolsantosh@gmail.com",
    description="A simple file sharing application for your local network",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thelkotolsantosh/lan-file-share",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Internet :: File Transfer Protocol (FTP)",
        "Topic :: Internet :: WWW/HTTP",
    ],
    python_requires=">=3.7",
    install_requires=[
        "Flask>=2.3.3",
        "Werkzeug>=2.3.7",
    ],
    entry_points={
        "console_scripts": [
            "lan-file-share=app:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
