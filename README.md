# Pydoc example

https://projects.raspberrypi.org/en/projects/documenting-your-code/

Start with a fresh Conda environment or virtualenv.

`conda create --name pydocs python=3.6`

`activate pydocs`

## Generate the documentation

`python -m pydoc -w .\card.py`

## Now try with Sphinx

### Install

`conda install -c anaconda sphinx`

### Create a Sphinx site

`sphinx-quickstart`

`make html`

