# Lab 03: Transforming Textual and Image Data

## Part A: Text Features

### Discussion Questions

1. Each column in the Document-Term Matrix represents a unique word, and each cell shows how many times that word appears in a document.

2. The Document-Term Matrix converts text into numerical vectors that machine learning models can process.

3. Bag-of-Words loses word order, grammar, and contextual meaning.

## Part B: Image Features

### Discussion Questions

1. Grayscale conversion reduces three RGB channels to one intensity channel, reducing the number of features.

2. The flattened vector length is height multiplied by width.

3. Flattening converts a 2D image matrix into a 1D numerical feature vector.

4. Resizing images to the same dimensions ensures that all feature vectors have equal length.

## Home-Lab Exercises

### Exercise 1: N-grams

Using unigrams and bigrams increased the vocabulary size from 11 to 24 because consecutive word pairs were added as features.

### Exercise 2: Repeated Words

Adding a fourth document with five occurrences of "sun" increased the document count but did not change the vocabulary size. Raw word counts can favour longer documents.

### Exercise 3: Image Resizing

The 64x64 grayscale image produces 4096 features, while the 32x32 image produces 1024 features. Smaller images reduce detail and may lose fine textures and small objects.

### Exercise 4: Image Feature Function

The image_to_features function loads an image, resizes it, converts it to grayscale, and flattens it into a numerical vector. Three test images produced vectors of shape (4096,).

## Home Assignment: Dataset

The dataset contains 20 images from two classes.

- X shape: (20, 4096)
- y shape: (20,)
- Image size: 64x64 grayscale
- Total features per image: 4096

A dataset of 20 samples with 4096 features is very small relative to its dimensionality. A machine learning model may overfit, so more labeled images or dimensionality reduction may be needed.

## Conclusion

Text and image data can be transformed into numerical feature vectors. These vectors provide a machine-understandable representation for machine learning tasks.