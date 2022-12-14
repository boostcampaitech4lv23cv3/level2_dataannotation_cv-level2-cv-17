# [Downloads - ICDAR2017 Competition on Multi-lingual scene text detection and script identification](https://rrc.cvc.uab.es/?ch=8&com=downloads)

Download below the training and validation dataset and associated ground truth information for each of the Tasks.

## Task 1: Multi-script text detection
### Training Set

- The training set comprises 7,200 images (5.77 GB) and is split in 8 files.
  - [Training Set Images 1/8 (311 MB)](https://datasets.cvc.uab.es/rrc/ch8_training_images_1.zip)
  - [Training Set Images 2/8 (467 MB)](https://datasets.cvc.uab.es/rrc/ch8_training_images_2.zip)
  - [Training Set Images 3/8 (1.2 GB)](https://datasets.cvc.uab.es/rrc/ch8_training_images_3.zip)
  - [Training Set Images 4/8 (1.2 GB)](https://datasets.cvc.uab.es/rrc/ch8_training_images_4.zip)
  - [Training Set Images 5/8 (1 GB)](https://datasets.cvc.uab.es/rrc/ch8_training_images_5.zip)
  - [Training Set Images 6/8 (1.01 GB)](https://datasets.cvc.uab.es/rrc/ch8_training_images_6.zip)
  - [Training Set Images 7/8 (532 MB)](https://datasets.cvc.uab.es/rrc/ch8_training_images_7.zip)
  - [Training Set Images 8/8 (61.2 MB)](https://datasets.cvc.uab.es/rrc/ch8_training_images_8.zip)

- [Training Set Localisation, Script and Transcription Ground Truth](https://datasets.cvc.uab.es/rrc/ch8_training_localization_transcription_gt_v2.zip) -- 7,200 text files with word level localisation, script and transcription ground truth

### Validation Set
- [Validation Set Images (1.09 GB)](https://rrc.cvc.uab.es/downloads/ch8_validation_images.zip) - 1,800 images
- [Validation Set Localisation, Script and Transcription Ground Truth](https://datasets.cvc.uab.es/rrc/ch8_validation_localization_transcription_gt_v2.zip) -- 1,800 text files with word level localisation, script and transcription ground truth

### Test Set
- [Test set images for Tasks 1 and 3](https://datasets.cvc.uab.es/rrc/ch8_test_images.zip) (same images for tasks 1 and 3).

## Task 2: Cropped Word Script identification
### Training Set
68,613 cut out word images (4.04 GB) corresponding to the axis oriented bounding boxes of the words are provided along with a single text file with the relative coordinates of the bounding shape within each word image. Script and transcription ground truth is provided in a single txt file.

  - [Training Set Word Images, along with Script Ground truth 1/3](https://datasets.cvc.uab.es/rrc/ch8_training_word_images_gt_part_1.zip) (1.28 GB) words #1 - 23,000
  - [Training Set Word Images, along with Script Ground truth 2/3](https://datasets.cvc.uab.es/rrc/ch8_training_word_images_gt_part_2.zip) (1.89 GB) words #23,001 - 46,000
  - [Training Set Word Images, along with Script Ground truth 3/3](https://datasets.cvc.uab.es/rrc/ch8_training_word_images_gt_part_3.zip) (877 MB) words #46,001 - 68,613

- [Script Groundtruth for word images of the training set](https://datasets.cvc.uab.es/rrc/ch8_training_word_gt_v2.zip)

### Validation Set
- [Validation Set Word Images, along with Script Ground truth (869 MB)](https://rrc.cvc.uab.es/downloads/ch8_validation_word_images_gt.zip) - 16,255 cut out word images corresponding to the axis oriented bounding boxes of the words are provided along with a single text file with the relative coordinates of the bounding shape within each word image. Script and transcription ground truth is provided in a single txt file.

- [Script Groundtruth for word images of the validation set](https://datasets.cvc.uab.es/rrc/ch8_validation_word_gt_v2.zip)

### Test Set
- [Test set images](https://datasets.cvc.uab.es/rrc/ch8_test_word_images.zip)

## Task 3: Joint text detection and script identification
The same datasets and ground truth as Task 1 are to be used (see Task 1, above).

## Terms of Use
The "Multi-lingual Scene Text Detection and Script Identification (MLT)" dataset and corresponding annotations are licensed under a Creative Commons Attribution 4.0 License.

---

## Download Script

```bash
# Multi-script text detection
wget https://datasets.cvc.uab.es/rrc/ch8_training_images_1.zip --no-check-certificate
wget https://datasets.cvc.uab.es/rrc/ch8_training_images_2.zip --no-check-certificate
wget https://datasets.cvc.uab.es/rrc/ch8_training_images_3.zip --no-check-certificate
wget https://datasets.cvc.uab.es/rrc/ch8_training_images_4.zip --no-check-certificate
wget https://datasets.cvc.uab.es/rrc/ch8_training_images_5.zip --no-check-certificate
wget https://datasets.cvc.uab.es/rrc/ch8_training_images_6.zip --no-check-certificate
wget https://datasets.cvc.uab.es/rrc/ch8_training_images_7.zip --no-check-certificate
wget https://datasets.cvc.uab.es/rrc/ch8_training_images_8.zip --no-check-certificate
wget https://datasets.cvc.uab.es/rrc/ch8_training_localization_transcription_gt_v2.zip --no-check-certificate
wget https://rrc.cvc.uab.es/downloads/ch8_validation_images.zip --no-check-certificate
wget https://datasets.cvc.uab.es/rrc/ch8_validation_localization_transcription_gt_v2.zip --no-check-certificate
wget https://datasets.cvc.uab.es/rrc/ch8_test_images.zip --no-check-certificate

# Cropped Word Script identification
wget https://datasets.cvc.uab.es/rrc/ch8_training_word_images_gt_part_1.zip --no-check-certificate
wget https://datasets.cvc.uab.es/rrc/ch8_training_word_images_gt_part_2.zip --no-check-certificate
wget https://datasets.cvc.uab.es/rrc/ch8_training_word_images_gt_part_3.zip --no-check-certificate
wget https://datasets.cvc.uab.es/rrc/ch8_training_word_gt_v2.zip --no-check-certificate
wget https://rrc.cvc.uab.es/downloads/ch8_validation_word_images_gt.zip --no-check-certificate
wget https://datasets.cvc.uab.es/rrc/ch8_validation_word_gt_v2.zip --no-check-certificate
wget https://datasets.cvc.uab.es/rrc/ch8_test_word_images.zip --no-check-certificate
```
