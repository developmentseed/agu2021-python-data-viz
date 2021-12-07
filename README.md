# AGU 2021 Open Science in Action Tutorials: Intro to Python Data Visualization

This repo a tutorial on python libraries for interactive and geospatial data visualization. To get started choose one of the installation options below. You can run the notebook remotely using MyBinder and locally using conda.

## Remote execution with MyBinder

Click: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/developmentseed/agu2021-python-data-viz/HEAD) and wait for a cloud-hosted jupyter lab to be deployed using `environment.yml`.

## Local execution using Conda

1. If you don't have conda (either with Miniconda or the full AnacondaDistribution) already installed we recommend [installing miniconda](http://conda.pydata.org/miniconda.html) for latest Python 3.
2. Then clone this repository and, at the root directory, you will find the environment.yml file. That files is basically the list of packages we are going to install.
3. Now create the environment with `conda env create --file environment.yml`
4. activate the environment with: `conda activate python-dataviz`
5. call `jupyter notebook` and open `tutorial.ipynb` to get started! Happy hacking!!
