import os
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import random

from tqdm import tqdm

for split in ["train", "test"]:
    images_dir = os.path.join(split, "images")
    images = os.listdir(images_dir)

    for image in tqdm(images, desc=f"Processing {split} set"):
        img = plt.imread(os.path.join(images_dir, image))

        if img.shape == (1080, 1920, 3):
            # Resize to 540x960
            img = img[::2, ::2]
            plt.imsave(os.path.join(images_dir, image), img)
