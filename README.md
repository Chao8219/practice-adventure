# Practice_Adventure
This is a demo rpg game under the tkinter GUI frame.
Please run the jupyter notebook to give it a try.

Here are several ways to run the jupyter notebook if you don't have 
any idea about it.

## 1 Use Venv

You can use python virtual environemt, venv, to create the same env.
Personally I would use conda env instead.
To use venv, you need to have python in your computer.
In this case, python 3.6.
After installing python, you can change directory, i.e. command 
`cd`, to your repo directory.

1st, use: `python3 -m venv rpg-venv` to create venv folder.

2nd, use: `source rpg-venv/bin/activate` to enter your venv.

3rd, use: `pip install -r requirements.txt` to install all required 
packages listed in txt file.

4th, if you want to exit the venv, use `deactivate` to exit.

Please notice that venv has sligt difference with conda env.

## 2 Use Conda Env

### 2.1 Basic Instruction

To use conda env, you need to have anaconda first.
Once installed, you can go to command line to create the same env by locally.

1st, use: `source anaconda3/bin/activate` to activate conda environment.
If you did not add conda to your path.
In case you may have few clues, the path works like shortcut in Windows, 
which could lead you to the package directly.

2nd, use: `conda env create -f conda-env.yml` to create the same conda 
environment.
Please notice that if you are using Windows or MacOS, you should run 
this instead: 
`conda env create -f conda-no-build-env.yml`.
The reason is simple: no-build env is cross-platformed.

3rd, use `conda activate rpg-env` to enter the environment.

For those conda environment yml files, you may see a file named 
**environment.yml**.
This file is prepared for Binder for which you can check out the Binder 
section.

### 2.2 Quickly Export Conda Env

Check out the **bash** directory. 
Please modify the repo location locally, depending on your config.
Then run `. export_conda_env`

### 2.3 Binder and Nbviewer

If you do not want to clone and load env locally, you may use Binder 
and Nbviewer for jupyter files.
Nbviewer provides nice view of jupyter notebook, and no installation needed.
Binder, in a more advance way, creates a copy of the required packages 
on their site, and you can run the scripts online, without any local 
installation.

Here is the link for 
[Binder](https://mybinder.org/v2/gh/Chao8219/practice-adventure/master).
One thing to notice is that, the tkinter seems does not support well with 
online docker image, which means you may not be able to try this repo 
directly through Binder.
The best way to do so is to clone it locally and create the same conda-env 
through the environment txt list file.

Here is the link for 
[Nbviewer](https://nbviewer.jupyter.org/github/Chao8219/practice-adventure/tree/master/)

Enjoy playing!

Update:
Right now the tkinter couldn't run well on Binder, which means you may 
need to do it locally.

## 3 To Do
### 3.1 To-do Task

- [x] integrate player_class into user_io
- [ ] add exception handling feature
- [x] modify jupyter path to relative one

### 3.2 Known Issues
- [x] conda-env has some dependency issue

## 4 Wrap It Up! Project

A new project that is based on this project called "Wrap It Up!" is online 
right now. 
This project is to give this repo a good ending since I decided to change 
my gears and use other methods or packages to accomplish the game design.

As you may see the above to-do list, the ultimate goal of this "Wrap It Up!" 
project is trying to fix all mistakes I have made in the past when I was 
young with only little knowledge about how to write codes.
Although I am definitely not an expert on coding and the way I will 
present in scripts is not the most elegent and efficient, I still want to, 
at least, try to make it better.

In the future commits, I will use **WIU** to indicate the changes is 
related with this "Wrap It Up!" project.

## 5 Tkinter Tips

There are several websites that might be useful to help to develop the GUI 
that is based on tkinter.

See:
[tkdocs.com](https://tkdocs.com/index.html)