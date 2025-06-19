# :open_file_folder: Spot the Differences
This project performs comparison between two images and showcase the differences between them. I will be using Pillow library from Python.

## :dango: List all visual or functional differences that might affect testing outcomes or user experience. 
- In the first image being displayed, the spacing is null between the three buttons.  
![image](https://github.com/user-attachments/assets/e6806509-dffd-4006-bfb6-950f3617fed3)

- In the second image is being shown the user’s funds (text) and Title (text) in a thin text style. So in this way users might not notice their funds in the first impression.  
![image](https://github.com/user-attachments/assets/55c47e39-e71a-49e9-98b3-6e209def7319)

- In the second image is being displayed the title as “My Acounts” instead of “My Accounts”  
![image](https://github.com/user-attachments/assets/540443fb-6aef-4044-a13d-8f7d3b3b5932)



## :books: Prerequisites

- **[Python](https://www.python.org/)** - Download and install the latest version with default settings. 
- **[Pillow](https://pillow.readthedocs.io/en/stable/index.html)** - Dependency.

### :pill: Install the library Pillow with pip:
- Open the terminal and write the following command:
```pip install pillow```

### :exclamation: Install Python extension on VSCode

## :desktop_computer:	 Installing the project
You are going to need to clone a copy of the application onto your computer to follow along.

### Cloning with Git
If you are familiar with Git and already have it installed the easiest way to clone the repo is to run this command in your terminal.

> [!IMPORTANT]
> git clone **_https://github.com/zaidiaz23/ImageComparison.git_**


## :green_heart: Run the code
Run the code. You'll see and image displaying the differences for the two images.  
![image](https://github.com/user-attachments/assets/31fc1d53-d965-4488-b4e3-c14302956a2f)


## :star: What does do the code?

- The following script loads an image using your default viewer:
```   
img1 = Image.open('First.jpg')
img2 = Image.open('Second.jpg')
```

- The followingg script returns the absolute value of the pixel-by-pixel difference between the two images.
```PIL.ImageChops.difference(image1: Image, image2: Image) → Image```

- If the images are identical, ```difference.getbbox()``` returns none, meaning there are no differences. If the images have differences, it returns a bounding box ((left, upper, right, lower)) that encloses all differing pixels. So ```bbox``` is used to determine whether two images have differences.

- A new image will be saved with the differences.  
  ![image](https://github.com/user-attachments/assets/39006cd5-0de2-4608-8779-10ff1dc4530e)

