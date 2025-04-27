from setuptools import setup, find_packages
from pathlib import Path

README = (Path(__file__).parent / "README.md").read_text()

setup(
    name="httpcooker",
    version="1.0.2",
    author="Mystic-poop (Xenz)",
    author_email="[YOUR EMAIL]",
    description="High-performance HTTP flood tool for security testing",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/mystic-poop/httpcooker",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        'requests',
        'colorama',
        'urllib3',
        'fake-useragent'
    ],
    entry_points={
        'console_scripts': [
            'httpcooker=httpcooker:main',
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Security",
        "Operating System :: OS Independent",
    ],
    keywords="pentesting security http ddos-tool",
    python_requires=">=3.8",
    include_package_data=True,
)
