

# :open_file_folder: Spot the Differences
This project performs comparison between two images and showcase the differences between them. I will be using Pillow library from Python.

## List all visual or functional differences that might affect testing outcomes or user experience. 
- Buttons: The spacing between components are almost null. 
- 


## Prerequisites

- **[Python](Download Python(https://www.python.org/)** - Download and install the latest version with default settings. 
- **[Pillow](https://pillow.readthedocs.io/en/stable/index.html)** - Dependency.

### Install the library Pillow with pip:
- Open the terminal and write the following command:
pip install pillow

### Install Python extension on VSCode

## :desktop_computer:	 Installing the project
You are going to need to clone a copy of the application onto your computer to follow along.

### Cloning with Git
If you are familiar with Git and already have it installed the easiest way to clone the repo is to run this command in your terminal.

> [!IMPORTANT]
> git clone **_HERE_**


## Run the code
Run the code. You'll see and image displaying the differences for the two images. 

## What does do the code?

- The following script loads an image using your default viewer:
img1 = Image.open('First.jpg')
img2 = Image.open('Second.jpg')

- The followingg script returns the absolute value of the pixel-by-pixel difference between the two images.
PIL.ImageChops.difference(image1: Image, image2: Image) → Image
- If the images are identical, difference.getbbox() returns None, meaning there are no differences. If the images have differences, it returns a bounding box ((left, upper, right, lower)) that encloses all differing pixels. So bbox is used to determine whether two images have differences.
- The following script shows the differences found
- The following script saves the differences found in a new image
