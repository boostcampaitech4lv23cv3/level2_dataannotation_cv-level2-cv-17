# [Downloads - Incidental Scene Text 2015](https://rrc.cvc.uab.es/?ch=4&com=downloads)
Download below the training dataset and associated ground truth information for each of the Tasks.

## Task 4.1: Text Localization (2015 edition)
### Training Set
- [Training Set Images (88.5MB)](https://rrc.cvc.uab.es/downloads/ch4_training_images.zip)- 1000 images obtained with wearable cameras
- [Training Set Localisation and Transcription Ground Truth (157KB)](https://rrc.cvc.uab.es/downloads/ch4_training_localization_transcription_gt.zip)- 1000 text files with word level localisation and transcription ground truth

### Test Set
- [Test Set Images (43.3MB)](https://rrc.cvc.uab.es/downloads/ch4_test_images.zip)- 500 images obtained with wearable cameras. You can submit your results for this Task over the images of the test set through the My Methods section.
- [Test Set Ground Truth (244Kb)](https://rrc.cvc.uab.es/downloads/Challenge4_Test_Task1_GT.zip) - 500 text files with text localisation bounding boxes for the images of the test set.


## Task 4.2: Text Segmentation (N/A)
Not available.

## Task 4.3: Word Recognition (2015 edition)
### Training Set
- [Training Set Word Images, along with Transcriptions Ground truth (40.5MB)](https://rrc.cvc.uab.es/downloads/ch4_training_word_images_gt.zip) - ~4468 cut out word images corresponding to the axis oriented bounding boxes of the words are provided along with a single text file with the relative coordinates of the bounding shape within each word image. Transcription ground truth is provided in a single txt file.

### Test Set
- [Test Set Word Images (21.5MB)](https://rrc.cvc.uab.es/downloads/ch4_test_word_images_gt.zip) - 2077 cut out word images corresponding to the axis oriented bounding boxes of the words are provided along with a single text file with the relative coordinates of the bounding shape within each word image. You can submit your results for this Task over the images of the test set through the My Methods section.
- [Test Set Ground Truth (49Kb)](https://rrc.cvc.uab.es/downloads/Challenge4_Test_Task3_GT.txt) - A single text file with the transcriptions of the 2077 images of the test set. Each line corresponds to an image of the test set.

## Task 4.4: End to End (2015 edition)
### Training Set
- [Training Set Images (88.5MB)](https://rrc.cvc.uab.es/downloads/ch4_training_images.zip) - 1000 images obtained with wearable cameras
- [Training Set Vocabulary (16KB)](https://rrc.cvc.uab.es/downloads/ch4_training_vocabulary.txt) - Vocabulary of all words (words of 3 characters or longer comprising only letters) appearing in the training set
- [Training Set Per-image Vocabularies (504KB)](https://rrc.cvc.uab.es/downloads/ch4_training_vocabularies_per_image.zip) - Vocabularies of 100 words per image, comprising the words appearing in the image plus distractors
- [Training Set Localisation and Transcription Ground Truth (157KB)](https://rrc.cvc.uab.es/downloads/ch4_training_localization_transcription_gt.zip) - 1000 text files with word level localisation and transcription ground truth

### Test Set
- [Test Set Images (43.3MB)](https://rrc.cvc.uab.es/downloads/ch4_test_images.zip) - 500 images obtained with wearable cameras. You can submit your results for this Task over the images of the test set through the My Methods section.
- [Test Set Vocabulary (8KB)](https://rrc.cvc.uab.es/downloads/ch4_test_vocabulary.txt) - Vocabulary of all words (words of 3 characters or longer comprising only letters) appearing in the test set
- [Test Set Per-image Vocabularies (248KB)](https://rrc.cvc.uab.es/downloads/ch4_test_vocabularies_per_image.zip) - Vocabularies of 100 words per image, comprising the words appearing in the image plus distractors
- [Test Set Ground Truth (244Kb)](https://rrc.cvc.uab.es/downloads/Challenge4_Test_Task4_GT.zip) - 500 text files with text localisation bounding boxes for the images of the test set.

### Other
- [Generic Vocabulary (796KB)](https://rrc.cvc.uab.es/downloads/GenericVocabulary.txt) - A vocabulary of about 90k words derived from the dataset publicly available here. Please consult \[1,2\] for further information as well as the disclaimer in the vocabulary file itself.

## Terms of Use
- The "Incidental Scene Text" dataset and corresponding annotations are licensed under a Creative Commons Attribution 4.0 License.

## References
- M. Jaderberg, K. Simonyan, A. Vedaldi, and A. Zisserman, "Synthetic data and artificial neural networks for natural scene text recognition", arXiv preprint arXiv:1406.2227, 2014
- M. Jaderberg, K. Simonyan, A. Vedaldi, and A. Zisserman, "Reading Text in the Wild with Convolutional Neural Networks", arXiv preprint arXiv:1412.1842, 2014

---

## Download Script

```bash
wget https://rrc.cvc.uab.es/downloads/ch4_training_images.zip --no-check-certificate
wget https://rrc.cvc.uab.es/downloads/ch4_training_localization_transcription_gt.zip --no-check-certificate
wget https://rrc.cvc.uab.es/downloads/ch4_test_images.zip --no-check-certificate
wget https://rrc.cvc.uab.es/downloads/Challenge4_Test_Task1_GT.zip --no-check-certificate
wget https://rrc.cvc.uab.es/downloads/ch4_training_word_images_gt.zip --no-check-certificate
wget https://rrc.cvc.uab.es/downloads/ch4_test_word_images_gt.zip --no-check-certificate
wget https://rrc.cvc.uab.es/downloads/Challenge4_Test_Task3_GT.txt --no-check-certificate
wget https://rrc.cvc.uab.es/downloads/ch4_training_images.zip --no-check-certificate
wget https://rrc.cvc.uab.es/downloads/ch4_training_vocabulary.txt --no-check-certificate
wget https://rrc.cvc.uab.es/downloads/ch4_training_vocabularies_per_image.zip --no-check-certificate
wget https://rrc.cvc.uab.es/downloads/ch4_training_localization_transcription_gt.zip --no-check-certificate
wget https://rrc.cvc.uab.es/downloads/ch4_test_images.zip --no-check-certificate
wget https://rrc.cvc.uab.es/downloads/ch4_test_vocabulary.txt --no-check-certificate
wget https://rrc.cvc.uab.es/downloads/ch4_test_vocabularies_per_image.zip --no-check-certificate
wget https://rrc.cvc.uab.es/downloads/Challenge4_Test_Task4_GT.zip --no-check-certificate
wget https://rrc.cvc.uab.es/downloads/GenericVocabulary.txt --no-check-certificate
```
