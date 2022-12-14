# [Downloads - ICDAR 2019 Robust Reading Challenge on Multi-lingual scene text detection and recognition](https://rrc.cvc.uab.es/?ch=15&com=downloads)

Download below the training dataset and the associated ground truth for each of the Tasks.

## Task 1: Multi-script text detection
### Training Set:
The training set is composed of 10,000 images, and can be downloaded from the following 2 links:

- [TrainSetImagesTask1_Part1 (3.5G)](https://datasets.cvc.uab.es/rrc/ImagesPart1.zip)
- [TrainSetImagesTask1_Part2 (3.3G)](https://datasets.cvc.uab.es/rrc/ImagesPart2.zip)

The ground truth is composed 10,000 text files (corresponding to the images) with word-level localization, script and transcription, and can be downloaded from the following link:

- [TrainSetGT (6.5M)](https://datasets.cvc.uab.es/rrc/train_gt_t13.zip)

Note that this task only requires localization results (as indicated in results format in the tasks page), but the ground truth also provides the script id of each bounding box and the transcription. This extra information will be needed in Tasks 3 and 4.

Extra information about the training set (may be useful for researchers who focus on one or only few languages, not all of the multi-lingual set):

The 10,000 images are ordered in the training set such that: each consecutive 1000 images contain text of one main language (and it may of course contain additional text from 1 or 2 other languages, all from the set of the 10 languages)

- 00001 - 01000:  Arabic
- 01001 - 02000:  English
- 02001 - 03000:  French
- 03001 - 04000:  Chinese
- 04001 - 05000:  German
- 05001 - 06000:  Korean
- 06001 - 07000:  Japanese
- 07001 - 08000:  Italian
- 08001 - 09000:  Bangla
- 09001 - 10000:  Hindi

### Test set:
Images (10,000 images):

- [MLT19_TestImagesPart1.zip](https://datasets.cvc.uab.es/rrc/MLT19_TestImagesPart1.zip)
- [MLT19_TestImagesPart2.zip](https://datasets.cvc.uab.es/rrc/MLT19_TestImagesPart2.zip)

## Task 2: Cropped Word Script identification
### Training Set:
- [Word_Images_Part1 (1.06GB)](https://datasets.cvc.uab.es/rrc/words_part_1.zip) (The Ground truth of the word images [2 files] is here too [in the same folder with the images])
- [Word_Images_Part2 (2.77GB)](https://datasets.cvc.uab.es/rrc/words_part_2.zip)
- [Word_Images_Part3 (1.17GB)](https://datasets.cvc.uab.es/rrc/words_part_3.zip)

### Test set:
Cropped word images:

- [MLT19_images_task2.zip (3.0GB)](https://rrc.cvc.uab.es/downloads/MLT19_images_task2.zip)

## Task 3: Joint text detection and script identification
### Training Set:
The same training set and ground truth as in Task 1 (see Task 1, above).

### Test set:
The same test set for Task 1.

## Task-4: End-to-End text detection and recognition
### Training Set:

It has two parts:

1. Real dataset: The same training set and ground truth as in Task 1 (see Task 1, above).
2. Synthetic dataset: We provide a synthetic dataset that matches the real dataset in terms of scripts, to help with the training for this task:
  - Download: Images of the synthetic dataset:
    - [Arabic](http://ptak.felk.cvut.cz/public_datasets/SyntText/Arabic.zip)
    - [Bangla](http://ptak.felk.cvut.cz/public_datasets/SyntText/Bangla.zip)
    - [Chinese](http://ptak.felk.cvut.cz/public_datasets/SyntText/Chinese.zip)
    - [Japanese](http://ptak.felk.cvut.cz/public_datasets/SyntText/Chinese.zip)
    - [Korean](http://ptak.felk.cvut.cz/public_datasets/SyntText/Korean.zip)
    - [Latin](http://ptak.felk.cvut.cz/public_datasets/SyntText/Latin.zip)
    - [Hindi](http://ptak.felk.cvut.cz/public_datasets/SyntText/Hindi.zip)
  - GT of the synthetic dataset (same format as the real dataset):
    - [Arabic](http://ptak.felk.cvut.cz/public_datasets/SyntText/Arabic_gt.zip)
    - [Bangla](http://ptak.felk.cvut.cz/public_datasets/SyntText/Bangla_gt.zip)
    - [Chinese](http://ptak.felk.cvut.cz/public_datasets/SyntText/Chinese_gt.zip)
    - [Japanese](http://ptak.felk.cvut.cz/public_datasets/SyntText/Japanese_gt.zip)
    - [Korean](http://ptak.felk.cvut.cz/public_datasets/SyntText/Korean_gt.zip)
    - [Latin](http://ptak.felk.cvut.cz/public_datasets/SyntText/Latin_gt.zip)
    - [Hindi](http://ptak.felk.cvut.cz/public_datasets/SyntText/Hindi_gt.zip)

Note that we provide a baseline method for this task: E2E-MLT. You can find the details of the method and also the synthetic dataset at:

E2E-MLT - an Unconstrained End-to-End Method for Multi-Language Scene Text: https://arxiv.org/abs/1801.09919

### Test set:
The same test set for Task 1.

## Terms of Use
The "Multi-lingual Scene Text Detection and Script Identification (MLT)" dataset and corresponding annotations are licensed under a Creative Commons Attribution 4.0 License.

---

## Download Script

```bash
wget https://datasets.cvc.uab.es/rrc/ImagesPart1.zip --no-check-certificate
wget https://datasets.cvc.uab.es/rrc/ImagesPart2.zip --no-check-certificate
wget https://datasets.cvc.uab.es/rrc/train_gt_t13.zip --no-check-certificate
wget https://datasets.cvc.uab.es/rrc/MLT19_TestImagesPart1.zip --no-check-certificate
wget https://datasets.cvc.uab.es/rrc/MLT19_TestImagesPart2.zip --no-check-certificate
wget https://datasets.cvc.uab.es/rrc/words_part_1.zip --no-check-certificate
wget https://datasets.cvc.uab.es/rrc/words_part_2.zip --no-check-certificate
wget https://datasets.cvc.uab.es/rrc/words_part_3.zip --no-check-certificate
wget https://rrc.cvc.uab.es/downloads/MLT19_images_task2.zip --no-check-certificate
wget http://ptak.felk.cvut.cz/public_datasets/SyntText/Arabic.zip --no-check-certificate
wget http://ptak.felk.cvut.cz/public_datasets/SyntText/Bangla.zip --no-check-certificate
wget http://ptak.felk.cvut.cz/public_datasets/SyntText/Chinese.zip --no-check-certificate
wget http://ptak.felk.cvut.cz/public_datasets/SyntText/Chinese.zip --no-check-certificate
wget http://ptak.felk.cvut.cz/public_datasets/SyntText/Korean.zip --no-check-certificate
wget http://ptak.felk.cvut.cz/public_datasets/SyntText/Latin.zip --no-check-certificate
wget http://ptak.felk.cvut.cz/public_datasets/SyntText/Hindi.zip --no-check-certificate
wget http://ptak.felk.cvut.cz/public_datasets/SyntText/Arabic_gt.zip --no-check-certificate
wget http://ptak.felk.cvut.cz/public_datasets/SyntText/Bangla_gt.zip --no-check-certificate
wget http://ptak.felk.cvut.cz/public_datasets/SyntText/Chinese_gt.zip --no-check-certificate
wget http://ptak.felk.cvut.cz/public_datasets/SyntText/Japanese_gt.zip --no-check-certificate
wget http://ptak.felk.cvut.cz/public_datasets/SyntText/Korean_gt.zip --no-check-certificate
wget http://ptak.felk.cvut.cz/public_datasets/SyntText/Latin_gt.zip --no-check-certificate
wget http://ptak.felk.cvut.cz/public_datasets/SyntText/Hindi_gt.zip --no-check-certificate
```

### Download and Unzip

```bash
cd /opt/ml/input/data

mkdir -p mlt19/
wget https://datasets.cvc.uab.es/rrc/ImagesPart1.zip --no-check-certificate
wget https://datasets.cvc.uab.es/rrc/ImagesPart2.zip --no-check-certificate
unzip 'ImagesPart*' -d mlt19/
mv mlt19/ImagesPart*/* ./mlt19/
rm -rf mlt19/ImagesPart*

wget https://datasets.cvc.uab.es/rrc/train_gt_t13.zip --no-check-certificate
mkdir -p mlt19_gt/
unzip 'train_gt_t13.zip' -d mlt19_gt/
```
