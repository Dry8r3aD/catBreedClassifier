# catBreedClassifier
* Image Classifier for Cat Breed
* End-Term Project for AI course @ Inha University

# Project
1. Data Collecting
2. Data Argumentation
3. Model Architecting
4. Integrating Model (Web Service)

## Data Collecting
* https://www.kaggle.com/ma7555/cat-breeds-dataset
 * 70,988 Images (67 Cat Breeds)
* https://www.robots.ox.ac.uk/~vgg/data/pets/
 * 2,403 Images (12 Cat Breeds)

## Data Argumentation
* 64 Cases (2 * 4 * 2 * 4)
 * Blur (Filter Size = 3, 5)
 * Noise (Gaussian Noise, STD. Deviation = 5, 10 ,15, 20)
 * Translation (Coordinate Translation (0, 0) -> (N, N), N = 5, 10)
 * Rotation (Rotation by- 10, -5, 5, 10 Degree)

