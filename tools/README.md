# Tools


## install\_ven.sh

A script which creates a python3 virtualenv and installs there all
of the requirements needed for running this project.
The location of the virtualenv is the directory the script is run from.
**Usage:**
1. Run the script root directory of the project.
    ```
    $ ./tools/install\_venv.sh
    ```
2. Source the virtualenv:
    ```
    $ source .venv/bin/activate
    ```


## tools.py

It's a python file which contains a method called mask\_thresh. The method
can be used for comparison of an original image and a processed image.
The processed image is put over the original one, so that, we can check if
the elements of the one picture are equals to the other which means, no
pixels were lost during the process.

