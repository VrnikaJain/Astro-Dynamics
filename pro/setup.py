from setuptools import setup, find_packages

setup(
    name="astrodynamics",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "scipy",
    ],
    author="VRNIKA JAIN",
    author_email="vrnikajain@gmail.com",
    description="A comprehensive library for astrodynamics calculations",
    license="MIT",
    url="https://github.com/Vrnika-Jain/AstroDynamics Calculator",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
