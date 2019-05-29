## Using Graphviz on Windows

This is a special note for using Graphviz on Windows.
For me, using graphviz on Ubuntu is relatively easy since all I did was 
to install graphviz package inside the conda env. 
It becomes a little bit different while I am using Win 10 for this repo.
So here are some tips for myself in case I need to do this again.

1. `conda install python-graphviz`

2. `pip install graphviz`

3. "Control Panel" -> "System and Security" -> "System" ->
    "Advanced System Setting" -> "Environment Variables" -> 
    Edit "Path" under "System variables" -> add new path 
    "C:\Users\the_path_to_Anaconda3\envs\my_env\Library\bin
    \graphviz"

After adding path up, please re-open terminals. This is very important.