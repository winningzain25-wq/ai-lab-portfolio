import numpy as np
from PIL import Image

def image_to_features(path, size=(64, 64)):
    """
    Load an image, resize it, convert to grayscale,
    and flatten it into a numerical feature vector.
    """

    image = Image.open(path)
    image = image.resize(size)
    image = image.convert('L')

    image_array = np.array(image)
    features = image_array.flatten()

    return features