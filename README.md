# SatSim

SatSim is a simulation modelling platform implemented in Python that follows
the recommendations provided in the ECSS Standard [ECSS-E-ST-40-07C](docs/ECSS-E-ST-40-07C.pdf).

It consists of two parts:
- a kernel to run simulations (based on discrete-event simulation and using [SimPy](https://simpy.readthedocs.io))
- a model library to build your system that is to be simulated (adhering to SMP2 modelling specification)

## Installation

Clone the repository and then install via pip:

```
$ git clone https://gitlab.com/librecube/prototypes/python-satsim
$ cd python-satsim
$ virtualenv venv
$ . venv/bin/activate
$ pip install -e .
```

## Example

To be written...

## Documentation

See [here](docs/README.md) for details on how to use SatSim module.

## Contribute

- Issue Tracker: https://gitlab.com/librecube/prototypes/python-satsim/-/issues
- Source Code: https://gitlab.com/librecube/prototypes/python-satsim

To learn more on how to successfully contribute please read the contributing
information in the [LibreCube guidelines](https://gitlab.com/librecube/guidelines).

## Support

If you are having issues, please let us know. Reach us at
[Matrix](https://app.element.io/#/room/#librecube.org:matrix.org)
or via [Email](mailto:info@librecube.org).

## License

The project is licensed under the MIT license. See the [LICENSE](./LICENSE.txt) file for details.
