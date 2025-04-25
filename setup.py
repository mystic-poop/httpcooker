from setuptools import setup

setup(
    name="httpcooker",
    version="1.1.1",
    author="Mystic-poop/Xenz",
    description="Advanced UDP Flood Attack Tool",
    long_description="A multi-threaded UDP flood attack tool for network stress testing",
    license="MIT",
    python_requires=">=3.6",
    install_requires=[],
    scripts=['ddos.py'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'httpcooker=httpcooker:main',
        ],
    },
)
