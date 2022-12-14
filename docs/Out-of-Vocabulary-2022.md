
# [Downloads - Out of Vocabulary Scene Text Understanding](https://rrc.cvc.uab.es/?ch=19&com=downloads)

## Obtain the training and validation data

## End-To-End

The datasets that you can use to train and validate on the End-To-End tasks are ICDAR13, ICDAR15, MLT19, COCO-Text, TextOCR, HierText, and OpenImagesText. We provide a **[shell script](https://rrc.cvc.uab.es/?com=downloads&action=download&ch=19&f=aHR0cHM6Ly9kYXRhc2V0cy5jdmMudWFiLmNhdC9UaUUvZ2V0X2RhdGEuc2g=)** to obtain the **training and validation** images from all the above datasets. The test images can be downloaded directly from **[this link](https://datasets.cvc.uab.es/TiE/NEW/testset_mappedv2.zip)**.

## Cropped Word Recognition

Like in the End-To-End task, the datasets that you can use to train and validate on the Cropped Word Recognition task are ICDAR13, ICDAR15, MLT19, COCO-Text, TextOCR, HierText, and OpenImagesText. We provide direct links to download the **[training](https://datasets.cvc.uab.cat/TiE/cropped_text/cropped_train.tar.gz)**, **[validation](https://datasets.cvc.uab.cat/TiE/cropped_text/val.zip)** and **[test](https://datasets.cvc.uab.es/TiE/NEW/test_croppedv2.zip)** splits.

## Annotations

## End-To-End

Since different datasets use slightly different annotation formats, we combine all of the annotations from the datasets mentioned above in a consistent format. We create a list of dictionaries for each image with the corresponding information extracted from each dataset.

```json
[
    {
        "image_name": NAME OF THE IMAGE
        "image_width": IMAGE WIDTH
        "image_height": IMAGE HEIGHT
        "dataset": WHICH DATASET THE IMAGE COMES FROM
        "split": WHICH SPLIT THE IMAGE BELONGS TO
        "text": {
            "transcription" : ...,
            "text_id": ...,
            "vertices": ...
        } ALL THE GROUND TRUTH INFORMATION OF THE OCR TOKENS
        "image_id": UNIQUE IDENTIFIER FOR IMAGE
    },
    ....
]
```

The training annotations for the End-To-End task can be downloaded from **[here](https://datasets.cvc.uab.cat/TiE/tie_train_v1.json)**.

The validation annotations for the End-To-End task can be downloaded from **[here](https://datasets.cvc.uab.cat/TiE/tie_val_v1.json)**.

## Cropped Word Recognition

The training annotations for the Cropped Word Recognition task can be downloaded from **[here](https://datasets.cvc.uab.cat/TiE/cropped_text/cropped_train_v1.json)**.

The validation annotations for the Cropped Word Recognition can be downloaded from **[here](https://datasets.cvc.uab.cat/TiE/cropped_text/cropped_val_v1.json)**.


---

## Download Script

```bash
# Get ICDAR 13
echo 'Downloading icdar 13 (143M)'
mkdir -p icdar13/ | wget https://rrc.cvc.uab.es/downloads/Challenge2_Training_Task12_Images.zip --no-check-certificate
# 142M
unzip Challenge2_Training_Task12_Images.zip -d icdar13/
# 143M
echo 'ICDAR13 Finished!'

# Get ICDAR 15
echo 'Downloading icdar 15 (89M)'
mkdir -p icdar15/ | wget https://rrc.cvc.uab.es/downloads/ch4_training_images.zip --no-check-certificate
# 86M
unzip ch4_training_images -d icdar15/
# 89M
echo 'ICDAR 15 Finished!'

# Get MLT 19
echo 'Downloading MLT 19 (7.0G)'
mkdir -p mlt19/
wget https://datasets.cvc.uab.es/rrc/ImagesPart1.zip --no-check-certificate
wget https://datasets.cvc.uab.es/rrc/ImagesPart2.zip --no-check-certificate
# 3.5G
# 3.3G
unzip 'ImagesPart*' -d mlt19/
mv mlt19/ImagesPart*/* ./mlt19/
rm -rf mlt19/ImagesPart*
echo 'MLT 19 finished!'

# Get COCO Text
echo 'Downloading COCO-Text (13G)'
mkdir -p cocotext/ | wget http://images.cocodataset.org/zips/train2014.zip
# 13G
unzip train2014.zip -d cocotext/
echo 'COCO finished'

# Get HierText
echo 'Downloading HierText (3.2G)'
mkdir hiertext
aws s3 --no-sign-request cp s3://open-images-dataset/ocr/train.tgz .
aws s3 --no-sign-request cp s3://open-images-dataset/ocr/validation.tgz .
# 2.7G (2.6 GiB)
# 551M (550.4 MiB)
tar xf train.tgz -C hiertext/
tar xf validation.tgz -C hiertext/
# 2.7G
# 558M
# Total 3.2G
echo 'HierText finished!'

# Get TextOCR
echo 'Downloading TextOCR (6.7G)'
mkdir textocr
wget https://dl.fbaipublicfiles.com/textvqa/images/train_val_images.zip
# 6.6G
unzip train_val_images.zip -d textocr/
# 6.7G
echo 'TextOCR Finished!'

# Get Open images
# echo 'Downloading OpenImagesText'
# mkdir openimages_v5
# aws s3 --no-sign-request cp s3://open-images-dataset/tar/train_1.tar.gz .
# aws s3 --no-sign-request cp s3://open-images-dataset/tar/train_2.tar.gz .
# aws s3 --no-sign-request cp s3://open-images-dataset/tar/train_5.tar.gz .
# aws s3 --no-sign-request cp s3://open-images-dataset/tar/train_f.tar.gz .
# aws s3 --no-sign-request cp s3://open-images-dataset/tar/validation.tar.gz .
# # 34.4 GiB
# # 33.0 GiB
# # 31.2 GiB
# # 27.9 GiB
# # 12.0 GiB
# for f in *.tar.gz; do tar -xf $f -C openimages_v5/; done
# echo 'OpenImagesText finished!'

echo 'Downloading Annotations (1.2G)'
wget https://datasets.cvc.uab.cat/TiE/tie_train_v1.json --no-check-certificate
wget https://datasets.cvc.uab.cat/TiE/tie_val_v1.json --no-check-certificate
wget https://datasets.cvc.uab.cat/TiE/cropped_text/cropped_train_v1.json --no-check-certificate
wget https://datasets.cvc.uab.cat/TiE/cropped_text/cropped_val_v1.json --no-check-certificate
# 941M
# 25M
# 198M
# 7.6M
```

## aws cli 설치

aws cli를 설치해야 aws s3 명령어를 사용할 수 있다.

- [AWS CLI에서 상위 수준(s3) 명령 사용 - AWS Command Line Interface](https://docs.aws.amazon.com/ko_kr/cli/latest/userguide/cli-services-s3-commands.html)
- [최신 버전의 AWS CLI 설치 또는 업데이트 - AWS Command Line Interface](https://docs.aws.amazon.com/ko_kr/cli/latest/userguide/getting-started-install.html)

```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sh ./aws/install
```

## OpenImages Annotation 제거

openimages가 용량이 커서 활용하지 못하므로, annotations 파일에서도 openimages 데이터를 제거해야 한다.

json 파일이 굉장히 크기 때문에, [jq](https://stedolan.github.io/jq/)를 활용한다.

```bash
# jq 설치
apt-get install -y jq

# train annotation 파일에서 openimages 데이터 제거
jq -s '.[] | map(select(.dataset != "openimages"))' tie_train_v1.json > tie_train_v1_exclude_openimages.json
jq -r tostring tie_train_v1_exclude_openimages.json > tie_train_v1_exclude_openimages_minified.json

# validation annotation 파일에서 openimages 데이터 제거
jq -s '.[] | map(select(.dataset != "openimages"))' tie_val_v1.json > tie_val_v1_exclude_openimages.json
jq -r tostring tie_val_v1_exclude_openimages.json > tie_val_v1_exclude_openimages_minified.json
```

## Annotation Format

Out of Vocabulary 2022의 annotation format은 다음과 같다.

```json
  {
    "image_name": "mlt19/tr_img_05008.jpg",
    "dataset": "mlt19",
    "split": "val",
    "text": [
      {
        "transcription": "원룸임대",
        "text_id": 2667530,
        "legible": true,
        "script": "Korean",
        "vertices": [
          [
            2514,
            1008
          ],
          [
            2917,
            981
          ],
          [
            2983,
            2022
          ],
          [
            2593,
            2028
          ]
        ],
        "oov": true
      },
      ...
    ]
  }
```
