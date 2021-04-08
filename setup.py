from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='satsim',
    version='0.0.1',
    author_email="info@librecube.org",
    description='Satellite Simulation Modelling Platform',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/librecube/prototypes/python-satsim",
    license='MIT',
    python_requires='>=3.4',
    packages=find_packages(exclude=['docs']),
    install_requires=['simpy'],
)
