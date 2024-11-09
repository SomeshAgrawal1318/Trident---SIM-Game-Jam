import os

import pygame

BASE_IMG_PATH = 'data/images/'

def load_image(path, enemy=0):
    """
    Load and scale a single image from the specified path.

    Args:
        path (str): Relative path to the image file within the base directory.

    Returns:
        pygame.Surface: Loaded and scaled image with transparent background set.
    """
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0, 0, 0))  # Set the black color as transparent
    if enemy == 1:
        img = pygame.transform.scale(img, (25, 30))  # Scale the image to 30x30 pixels
        img.set_colorkey((0,0,0))
    return img

def load_images(path,enemy=0):
    """
    Load and scale multiple images from a specified directory.

    Args:
        path (str): Directory path within the base directory containing images.

    Returns:
        list[pygame.Surface]: List of loaded and scaled images.
    """
    images = []
    for img_name in sorted(os.listdir(BASE_IMG_PATH + path)):
        images.append(load_image(path + '/' + img_name, enemy))  # Scale each image to 30x30 pixels
    return images


class Animation:
    def __init__(self, images, img_dur=5, loop=True):
        self.images = images
        self.loop = loop
        self.img_duration = img_dur
        self.done = False
        self.frame = 0
    
    def copy(self):
        return Animation(self.images, self.img_duration, self.loop)
    
    def update(self):
        if self.loop:
            self.frame = (self.frame + 1) % (self.img_duration * len(self.images))
        else:
            self.frame = min(self.frame + 1, self.img_duration * len(self.images) - 1)
            if self.frame >= self.img_duration * len(self.images) - 1:
                self.done = True
    
    def img(self):
        return self.images[int(self.frame / self.img_duration)]