# Polar Roses 

Plots r = $\sin(n{\theta})$

## Run Book
```bash
# REPO points to root of the repo
cd $REPO/ai/polar_plots

# install python virtual env
python3 -m venv .venv
source .venv/bin/activate
pip install pip-tools

# 1. Compile: Generates requirements.txt with pinned versions and hashes
pip-compile requirements.in

# 2. Sync: Installs exactly what is in requirements.txt and REMOVES anything else
pip-sync requirements.txt

# Ensure Jupyter "sees" the virtual environment as available engine
python3 -m ipykernel install --user --name .venv --display-name "Python3 (.venv)"

# Two Options:
# a. Browser runs Jupyter Lab
# jupyter lab 
# copy URL http://localhost:888... in Browser
# Open .py file so that Jupyter renders it as notebook

# b. VS Code run Jupyter Lab
# code . # Open folder in VS Code
# Open .py file so that VSCode detects the #%% marker and shows "Run Cell" buttons
# When prompted, select .venv kernel 
```
