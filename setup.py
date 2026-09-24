from pathlib import Path
from setuptools import setup, find_packages

long_description = (Path(__file__).parent / "README.md").read_text(encoding="utf-8")

setup(
    name="nigerian-states",
    version="0.1.1",
    packages=find_packages(exclude=["states", "states.*", "tests", "tests.*"]),
    package_data={"nigerian_states.states": ["data/states_lgas.json"]},
    include_package_data=True,
    author="Mark Ekperi",
    author_email="mark.ekperi@gmail.com",
    description="A Python package for Nigerian states and LGAs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/doubi3/nigerian-states",
    project_urls={
        "Bug Tracker": "https://github.com/doubi3/nigerian-states/issues",
        "Source": "https://github.com/doubi3/nigerian-states",
    },
    license="MIT",
    keywords=["nigeria", "states", "lga", "local-government-areas", "geodata"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[],
    python_requires=">=3.6",
)