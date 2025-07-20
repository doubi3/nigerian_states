from setuptools import setup, find_packages

setup(
    name="nigerian-states",
    version="0.1.0",
    packages=find_packages(),
    package_data={"nigerian_states": ["data/*.json"]},  # Include JSON file
    author="Mark Ekperi",
    description="A Python package for Nigerian states and LGAs.",
    url="https://github.com/doubi3/nigerian-states",
    install_requires=[],  # Add dependencies if needed
    python_requires=">=3.6",
)