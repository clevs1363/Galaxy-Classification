# File Outline
## faster_rcnn.py
Trains and runs a Faster R-CNN detector.

## get_coords.py
Processes the `gz2_hart16.csv` file and returns the ra/dec coordinates for a given number of lines.

## get_labels.py
Uses the Galaxy Zoo 2 database to get the class labels for each galaxy. The galaxy types and the corresponding column names and values are as follows: 

    Elliptical:   t01_smooth_or_features_a01_smooth_flag == 1
    Edge-on Disk: t02_edgeon_a04_yes_flag                == 1
    Oblique Disk: t02_edgeon_a05_no_flag                 == 1
    Spiral Disk:  t04_spiral_a08_spiral_flag             == 1
    Ring:         t08_odd_feature_a19_ring_flag          == 1
    Merger:       t08_odd_feature_a24_merger_flag        == 1

## get_sdss_images.py
Using the labeled galaxies outputted by `get_labels.py`, this file leverages the SDSS database to obtain FITS images of each galaxy. The FITS images are converted to JPG using the `make_lupton_rgb()` function as used by the paper.

## read_data.py
Parses the entire `gz2_hart16.csv` and obtains a list of galaxies and their types.

## train_nn.py
Trains and runs an SSD detector.

# Additional Work
- **Explore Galaxy Zoo datasets**: One of the biggest tasks of this project was exploring and understanding the datasets. The paper studied used the Galaxy Zoo dataset, from which the Galaxy Zoo 2 (GZ2) added onto. It was challenging to get a feel for, obtain, and parse through this new dataset.
- **Researched galaxy types**: Since the dataset used by the paper expressed different galaxy types than GZ2, I needed to understand the different types of galaxies to have a classification set that made sense. I have included a markdown file "Galaxy Types" with my notes.
- **Object detection frameworks**: While I've worked with neural networks before, I've never worked with object detection frameworks, so I got to explore different frameworks for the first time. The paper used YOLO, while two others were Faster R-CNN and SSD. SSD is described in the paper [SSD: Single Shot MultiBox Detector](https://arxiv.org/abs/1512.02325).
