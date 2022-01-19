import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    readme = fh.read()

setuptools.setup(
    name='satsim',
    version='0.0.1',
    description="ECSS-Based Satellite Simulation Modelling Platform",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://xxxx",
    author="LibreCube",
    author_email="info@librecube.org",
    license="GPL",
    packages=setuptools.find_namespace_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.6",
    install_requires=["simpy"],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'server=server:server',
            'cli=cli:cli',
        ]
    }
)
