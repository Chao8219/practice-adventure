# Practice_Adventure
RPG_type

Please run Take_An_Adventure_GUI to run the game.

Directory /test/ contains test file.

File read_user_info.py could read the info directly.

## Use Venv

You can use python virtual environemt, venv, to create the same env.
Personally I would use conda env instead.
To use venv, you need to have python in your computer.
In this case, python 3.6.
After installing python, you can change directory, i.e. command `cd`, to your repo directory.

1st, use: `python3 -m venv rpg-venv` to create venv folder.

2nd, use: `source rpg-venv/bin/activate` to enter your venv.

3rd, use: `pip install -r requirements.txt` to install all required packages listed in txt file.

4th, if you want to exit the venv, use `deactivate` to exit.

Please notice that venv has sligt difference with conda env.

## Use Conda Env

To use conda env, you need to have anaconda first.
Once installed, you can go to command line to create the same env by locally.

1st, use: `source anaconda3/bin/activate` to activate conda environment.
If you did not add conda to your path.
In case you may have few clues, the path works like shortcut in Windows, which could lead you to the package directly.

2nd, use: `conda env create -f conda-env.yml` to create the same conda environment.
Please notice that if you are using Windows or MacOS, you should run this instead: 
`conda env create -f conda-no-build-env.yml`.
The reason is simple: no-build env is cross-platformed.

3rd, use `conda activate rpg-env` to enter the environment.

For those conda environment yml files, you may see a file named **environment.yml**.
This file is prepared for Binder for which you can check out the Binder section.

## Binder and Nbviewer

If you do not want to clone and load env locally, you may use Binder and Nbviewer for jupyter files.
Nbviewer provides nice view of jupyter notebook, and no installation needed.
Binder, in a more advance way, creates a copy of the required packages on their site, and you can run the scripts online, without any local installation.

Here is the link for [Binder](https://mybinder.org/v2/gh/Chao8219/practice-adventure/master).

Here is the link for [Nbviewer](https://nbviewer.jupyter.org/github/Chao8219/practice-adventure/tree/master/)

Enjoy playing!

## Quickly Update Conda Env

Check out the **bash** directory. 
Please modify the repo location locally, depending on your config.
Then run `. export_conda_env`

## To Do

- [ ] move all py script into jupyter notebook for better preview.
