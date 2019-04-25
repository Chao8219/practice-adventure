# Practice_Adventure
RPG_type

Please run Take_An_Adventure_GUI to run the game.

Directory /test/ contains test file.

File read_user_info.py could read the info directly.

# Update:

The venv is remodified.

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
