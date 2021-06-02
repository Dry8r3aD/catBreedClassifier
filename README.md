# catBreedClassifier
* Image Classifier for Cat Breed
* End-Term Project for AI course @ Inha University

# Project
1. Data Collecting
2. Data Augmentation
3. Model Architecting
4. Integrating Model (Web Service)

## Data Collecting
* https://www.kaggle.com/ma7555/cat-breeds-dataset
  * 70,988 Images (67 Cat Breeds)
* https://www.robots.ox.ac.uk/~vgg/data/pets/
  * 2,403 Images (12 Cat Breeds)

### Classifying Cat Breeds
* Abyssinian
* American Bobtail
* American Curl
* American Shorthair
* Applehead Siamese
* Balinese
* Bengal
* Birman
* Bombay
* British Shorthair
* Burmese
* Calico
* Cornish Rex
* Devon Rex
* Dilute Calico
* Dilute Tortoiseshell
* Egyptian Mau
* Exotic Shorthair
* Extra-Toes Cat - Hemingway Polydactyl
* Havana
* Himalayan
* Japanese Bobtail
* Maine Coon
* Manx
* Munchkin
* Nebelung
* Norwegian Forest Cat
* Ocicat
* Oriental Short Hair
* Oriental Tabby
* Persian
* Pixiebob
* Ragamuffin
* Ragdoll
* Russian Blue
* Scottish Fold
* Siamese
* Siberian
* Snowshoe
* Sphynx - Hairless Cat
* Tabby
* Tiger
* Tonkinese
* Torbie
* Tortoiseshell
* Turkish Angora
* Turkish Van
* Tuxedo

### Excluded Cat Breeds
* Due to small training images ( < 100 )
  * York Chocolate
  * Chinchilla
  * Canadian Hairless
  * Burmilla
  * LaPerm
  * Cymric
  * American Wirehair
  * Singapura
  * Chausie
  * Javanese
  * Somali
  * Oriental Long Hair
  * Korat
  * Selkirik Res
  * Chartreux
  * Silver
* Due to difficulty of distinguishing (e.g. Mixed Breeds)
  * Domestic Short / Medeium / Long Hair 

## Data Augmentation
* 64 Cases (2 * 4 * 2 * 4)
  * Blur (Filter Size = 3, 5)
  * Noise (Gaussian Noise, STD. Deviation = 5, 10 ,15, 20)
  * Translation (Coordinate Translation (0, 0) -> (N, N), N = 5, 10)
  * Rotation (Rotation by- 10, -5, 5, 10 Degree)

