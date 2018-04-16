# Grains Recognition


## About
The project was implemented during 24h hackaton competition in Brno organised
by [UnIT Brno](https://unitbrno.cz/) in .


## Task
Implement an application which is able to load and analyze a picture
containing grains in TIFF format. The application is supposed to find all
grains and calculate their properties which will be exported in CSV format.

Requirements:
1. CLI parameters:
    - Path to a file to be analyzed (--image-path)
    - Path to a CSV file for exporting the calculations (--csv-path)

2. Each line of the CSV file contains informations about one grain.
3. Information about grains to be collected:
    - Width = it's a width of a
[bounded box](https://en.wikipedia.org/wiki/Minimum_bounding_box) in pixels
    - Height = it's a height of a
[bounded box](https://en.wikipedia.org/wiki/Minimum_bounding_box) in pixels
    - Max Length = flowline of the most distance between two points on the
grain, the flowline can go through outside of the grain - in case of a
irregular shape of the grain
    - Thickness = perpendicular flowline on the Max Length distance,
the flowline mustn't go outside of the grain

4. Usage of opensource libraries for image recognition, filtration is not
allowed. They can be used only for loading an image.
5. The grains which are located at the borders of the image - only a part of
the grain is shown and the rest is outside of the image - can't be processed
6. The grains which are overlapping are processed as one grain.


### Prerequisites

- Python 3.6 or higher (but it may work even with older versions of Python 3)
- pip3


## Install

1. Install requirements which are listed in the requirements.txt
    ```
    $ ./tools/install_venv.sh
    ```
2. The script creates a .venv where all requirements are installed, source it:
    ```
    $ source .venv/bin/activate
    ```


## Run

    $ ./main.py [-h] --image-path IMAGE_PATH --csv-path CSV_PATH [--resize RESIZE]


## Options

-  -h, --help => show this help message and exit
-  --image-path IMAGE\_PATH =>  Path to an image to be processed
-  --csv-path CSV\_PATH => Path where csv file will be stored
-  --resize RESIZE => Percentage to scale picture down


## Process Flow

1. An image in .TIFF format is loaded
2. **(optional)** If `--resize` argument is present, the loaded image is resized
3. Blur filter is applied
4. Threshold is calculated by [OTSU algorithm](https://en.wikipedia.org/wiki/Otsu's_method)
5. Thresholding - the threshold is applied on the image
6. Each grain is wrapped inside a [bounded box](https://en.wikipedia.org/wiki/Minimum_bounding_box)
7. Border points are discovered
8. Lengths and thickness are calculated


## Authors
[Martin Kopec](https://github.com/kopecmartin)
[Maroš Kopec](https://github.com/Madeyro)
[Patrik Segedy](https://github.com/psegedy)
[Tomáš Sýkora](https://github.com/tomassykora)
