from setuptools import setup, find_packages

setup(
    name="nigerian-states",
    version="0.1.0",
    packages=find_packages(),
    package_data={"nigerian_states.states": ["data/states_lgas.json"]},
    include_package_data=True,
    author="Mark Ekperi",
    description="A Python package for Nigerian states and LGAs.",
    url="https://github.com/doubi3/nigerian-states",
    install_requires=[],
    python_requires=">=3.6",
)