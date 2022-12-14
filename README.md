# 🌠 Sixth Sense 팀의 데이터 제작 프로젝트

학습 데이터 추가 및 수정을 통한 이미지 속 글자 검출 성능 개선 대회

> 기간 : 2022.12.08 ~ 2022.12.15

![부스트 캠프 AI Tech 4기](https://img.shields.io/badge/%EB%B6%80%EC%8A%A4%ED%8A%B8%EC%BA%A0%ED%94%84%20AI%20Tech-4%EA%B8%B0-red)
![Level 2](https://img.shields.io/badge/Level-2-yellow)
![CV 17조](https://img.shields.io/badge/CV-17%EC%A1%B0-brightgreen)
![Object Detection 대회](https://img.shields.io/badge/%EB%8C%80%ED%9A%8C-%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%A0%9C%EC%9E%91-blue)

![stages ai_competitions_224_overview_description](https://user-images.githubusercontent.com/9074297/205859800-9d74718a-3534-446e-b017-424706495ac9.png)

## 😎 Members
<table>
    <thead>
        <tr>
            <th>박선규</th>
            <th>박세준</th>
            <th>서장원</th>
            <th>이광민</th>
            <th>장국빈</th>
            <th>조태환</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td width="16%"><img src="https://user-images.githubusercontent.com/9074297/207550543-a4a35f97-c647-4013-b440-dbfec61b01d7.png" width="100%"/></td>
            <td width="16%"><img src="https://user-images.githubusercontent.com/9074297/207550381-3f2deddb-ffef-4249-8738-66d27c83ea79.png" width="100%"/></td>
            <td width="16%"><img src="https://user-images.githubusercontent.com/9074297/207550023-28ad4754-e60b-4a0c-835e-ea3c32108703.png" width="100%"/></td>
            <td width="16%"><img src="https://user-images.githubusercontent.com/9074297/207551768-ca68e744-70bf-452d-bd61-f4db912e59ee.png" width="100%"/></td>
            <td width="16%"><img src="https://user-images.githubusercontent.com/9074297/207583484-e4cff046-7656-4c27-90c9-0ce116418e70.png" width="100%"/></td>
            <td width="16%"><img src="https://user-images.githubusercontent.com/9074297/207550298-4dd75fe8-137d-4bad-accf-d56363c01895.png" width="100%"/></td>
        </tr>
        <tr>
            <td align="center"><a href="https://github.com/Sungyu-Park"><sub><sup>@Sungyu-Park</sup></sub></a></td>
            <td align="center"><a href="https://github.com/sjleo1"><sub><sup>@sjleo1</sup></sub></a></td>
            <td align="center"><a href="https://github.com/nanpuhaha"><sub><sup>@nanpuhaha</sup></sub></a></td>
            <td align="center"><a href="https://github.com/lkm6871"><sub><sup>@lkm6871</sup></sub></a></td>
            <td align="center"><a href="https://github.com/JKbin"><sub><sup>@JKbin</sup></sub></a></td>
            <td align="center"><a href="https://github.com/OMMANT"><sub><sup>@OMMANT</sup></sub></a></td>
        </tr>
    </tbody>
</table>

## 🧑‍💻 Contributions

- 박선규 :
- 박세준 :
- 서장원 :
- 이광민 :
- 장국빈 :
- 조태환 :

<br>

## :earth_asia: Project Overview
스마트폰으로 카드를 결제하거나, 카메라로 카드를 인식할 경우 자동으로 카드 번호가 입력되는 경우가 있습니다. 또 주차장에 들어가면 차량 번호가 자동으로 인식되는 경우도 흔히 있습니다. 이처럼 OCR (Optimal Character Recognition) 기술은 사람이 직접 쓰거나 이미지 속에 있는 문자를 얻은 다음 이를 컴퓨터가 인식할 수 있도록 하는 기술로, 컴퓨터 비전 분야에서 현재 널리 쓰이는 대표적인 기술 중 하나입니다.

<img src="https://user-images.githubusercontent.com/9074297/207525540-79be879f-371e-476f-9849-031feba508cb.png" height="250px"/>

OCR task는 글자 검출 (text detection), 글자 인식 (text recognition), 정렬기 (Serializer) 등의 모듈로 이루어져 있습니다.

본 대회는 아래와 같은 특징과 제약 사항이 있습니다.
- 본 대회에서는 '글자 검출' task 만을 해결하게 됩니다.
- 예측 csv 파일 제출 (Evaluation) 방식이 아닌 model checkpoint 와 inference.py 를 제출하여 채점하는 방식입니다. (Inference) 상세 제출 방법은 AI Stages 가이드 문서를 참고해 주세요!
- 대회 기간과 task 난이도를 고려하여 코드 작성에 제약사항이 있습니다. 상세 내용은 베이스라인 코드 탭 하단의 설명을 참고해주세요.

<br>

- Input : 글자가 포함된 전체 이미지
- Output : bbox 좌표가 포함된 UFO Format (상세 제출 포맷은 평가 방법 탭 및 강의 5강 참조)

<br>

## 🚨 Competition Rules

본 대회는 데이터를 구성하고 활용하는 방법에 집중하는 것을 장려하는 취지에서, 제공되는 베이스 코드 중 모델과 관련한 부분을 변경하는 것이 금지되어 있습니다. 이에 대한 세부적인 규칙은 아래와 같습니다.

- 베이스라인 모델인 EAST 모델이 정의되어 있는 아래 파일들은 변경사항 없이 그대로 이용해야 합니다.
    - model.py
    - loss.py
    - east_dataset.py
    - detect.py
- 변경이 금지된 파일들의 내용을 이용하지 않고 모델 관련 내용을 새로 작성해서 이용하는 것도 대회 규정에 어긋나는 행위입니다.
- 이외의 다른 파일을 변경하거나 새로운 파일을 작성하는 것은 자유롭게 진행하셔도 됩니다.
    - [예시] dataset.py에서 pre-processing, data augmentation 부분을 변경
    - [예시] train.py에서 learning rate scheduling 부분을 변경

<br>

## 💾 Dataset

### 기본 제공된 데이터셋
- ICDAR17_Korean (서버 기본 데이터셋)
- Campers (캠퍼들이 Upstage OCR Annotation Tool로 라벨링한 데이터셋)

### 추가로 활용한 외부 데이터셋
- [ICDAR 2017 MLT :link:](https://rrc.cvc.uab.es/?ch=8)
- [ICDAR 2019 MLT :link:](https://rrc.cvc.uab.es/?ch=15)
- [Out of Vocabulary 2022 :link:](https://rrc.cvc.uab.es/?ch=19)
  - ICDAR13, ICDAR15, MLT19, COCO-Text, TextOCR, HierText, ~~OpenImagesText~~
- AI-Hub [다양한 형태의 한글 문자 OCR (39.61 GB) :link:](https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=91)

<br>

## 💻 Develop Environment
- OS : Ubuntu 18.04.5 LTS (bionic)
- CPU : Intel(R) Xeon(R) Gold 5120 CPU @ 2.20GHz (8 Cores, 8 Threads)
- RAM : 90GB
- GPU : Tesla V100-PCIE-32GB
- Storage : 100GB
- Python : 3.8.5 (Anaconda)
- CUDA : 11.0
- NVIDIA : 450.80.02

<br>

## 📂 Project Structure

<details>
<summary>프로젝트 구조 살펴보기</summary>

```bash
.
├──🔗code -> 📁/opt/ml/level2_dataannotation_cv-level2-cv-17/src
├──📁input
│   └──📁data
│       ├──📁ICDAR17_Korean
│       │   ├──🖼️img_1001.jpg
│       │   └──🖼️...
│       ├──📄ICDAR17_Korean_UFO.json
│       ├──📄ICDAR17_Korean_UFO_train.json
│       ├──📄ICDAR17_Korean_UFO_valid.json
│       ├──📁campers
│       │   ├──🖼️01.jpg
│       │   └──🖼️...
│       ├──📄campers_UFO.json
│       ├──📄campers_UFO_train.json
│       ├──📄campers_UFO_valid.json
│       ├──📁cocotext
│       │   └── train2014
│       │       ├──🖼️COCO_train2014_000000187823.jpg
│       │       └──🖼️...
│       ├──📁hiertext
│       │   ├──📁train
│       │   │   ├──🖼️dad729bb808f6b05.jpg
│       │   │   └──🖼️...
│       │   └──📁validation
│       │       ├──🖼️cc7423ec2a7adb30.jpg
│       │       └──🖼️...
│       ├──📁icdar13
│       │   ├──🖼️100.jpg
│       │   └──🖼️...
│       ├──📁icdar15
│       │   ├──🖼️img_966.jpg
│       │   └──🖼️...
│       ├──📁mlt19
│       │   ├──🖼️tr_img_03540.jpg
│       │   └──🖼️...
│       ├──📁textocr
│       │   └──📁train_images
│       │       ├──🖼️2413a55b0323deb0.jpg
│       │       └──🖼️...
│       ├──📄OOV_UFO_train.json
│       ├──📄OOV_UFO_valid.json
│       ├──📄ICDAR17Korean_Campers_OOV_train.json
│       ├──📄ICDAR17Korean_Campers_OOV_valid.json
│       ├──🔗train.json -> 📄ICDAR17Korean_Campers_OOV_train.json
│       └──🔗valid.json -> 📄ICDAR17Korean_Campers_OOV_valid.json
├──📁level2_dataannotation_cv-level2-cv-17
│   └──📁src
│       ├──📁trained_models
│       │   └──📄latest.pth
│       ├──📄convert_mlt.py
│       ├──📄dataset.py
│       ├──📄detect.py ---------- 변경 금지 ⚠️
│       ├──📄deteval.py
│       ├──📄east_dataset.py ---- 변경 금지 ⚠️
│       ├──📄inference.py
│       ├──📄loss.py ------------ 변경 금지 ⚠️
│       ├──📄model.py ----------- 변경 금지 ⚠️
│       └──📄train.py
└──📁pths
    └──📄vgg16_bn-6c64b313.pth
```

</details>

<br>

## 👨‍🏫 Evaluation Methods
평가방법은 DetEval 방식으로 계산되어 진행됩니다.

DetEval은, 이미지 레벨에서 정답 박스가 여러개 존재하고, 예측한 박스가 여러개가 있을 경우, 박스끼리의 다중 매칭을 허용하여 점수를 주는 평가방법 중 하나 입니다.

<details>
<summary>평가 방법 자세히 살펴보기</summary>

### 제출포맷

`inference.py`의 결과로 생성되는 `output.csv`의 형식은 UFO(Upstage Format for OCR)로 작성되도록 해야합니다.

단, inference에서는 글자 영역에 대한 bounding box 정보 외의 다른 정보는 필요로 하지 않기 때문에 전체 UFO 형식 중 "points"에 해당하는 값들만 포함하고 있으면 됩니다.

베이스 코드로 제공되는 `inference.py`는 기본적으로 평가 데이터에 대한 UFO를 출력하도록 작성되어있으며 다음은 출력된 결과물의 예시입니다.

```python
{
    "images": {
        "X_google_0058.jpg": {
            "words": {
                "0": {
                    "points": [
                        [
                            157.06430053710938,
                            2181.391357421875
                        ],
                        [
                            1026.414794921875,
                            2080.502685546875
                        ],
                        [
                            1078.5938720703125,
                            2522.3408203125
                        ],
                        [
                            209.24400329589844,
                            2623.228271484375
                        ]
                    ]
                },
                "1": {
                    "points": [
                        [
                            870.1994018554688,
                            620.5530395507812
                        ],
                        [
                            1584.752685546875,
                            679.5577392578125
                        ],
                        [
                            1567.9024658203125,
                            896.4556274414062
                        ],
                        [
                            853.3502197265625,
                            837.4486083984375
                        ]
                    ]
                },
                ...
            }
        },
        ...
    }
}
```

### 평가방법

평가방법은 DetEval 방식으로 계산되어 진행됩니다.

DetEval은, 이미지 레벨에서 정답 박스가 여러개 존재하고, 예측한 박스가 여러개가 있을 경우, 박스끼리의 다중 매칭을 허용하여 점수를 주는 평가방법 중 하나입니다.

평가가 이루어지는 방법은 다음과 같습니다.

<br>

#### 1) 모든 정답/예측박스들에 대해서 Area Recall, Area Precision을 미리 계산해냅니다.

여기서 Area Recall, Area Precision은 다음과 같습니다.
- Area Recall = 정답과 예측박스가 겹치는 영역 / 정답 박스의 영역
- Area Precision = 정답과 예측박스가 겹치는 영역 / 예측 박스의 영역

<img src="https://user-images.githubusercontent.com/9074297/207590718-511f6daa-b948-4bc9-b2ee-d5eb9aee31ab.png" height="250px"/>

<br>

#### 2) 모든 정답 박스와 예측 박스를 순회하면서, 매칭이 되었는지 판단하여 박스 레벨로 정답 여부를 측정합니다.

박스들이 매칭이 되는 조건은 박스들을 순회하면서, 위에서 계산한 Area Recall, Area Precision이 0 이상일 경우 매칭 여부를 판단하게 되며, 박스의 정답 여부는 Area Recall 0.8 이상, Area Precision 0.4 이상을 기준으로 하고 있습니다.

매칭이 되었는가 대한 조건은 크게 3가지 조건이 있습니다.

1. one-to-one match: 정답 박스 1개와 예측 박스 1개가 매칭 && 기본조건 성립
2. one-to-many match: 정답 박스 1개와 예측 박스 여러개가 매칭되는 경우
3. many-to-one match: 정답 박스 여러개와 예측박스 1개가 매칭되는 경우

여기서, one-to-many match 경우에 한해서, 박스 recall / precision 에 0.8 로 penalty가 적용됩니다.

<br>
<br>

아래의 이미지를 통해 평가방법의 설명을 보충합니다.

<br>

그림에서 왼쪽과 같이 다음과 같은 정답박스가 존재하는 이미지에 대해서, 오른쪽과 같이 예측하였다고 가정합니다.

<img src="https://user-images.githubusercontent.com/9074297/207590705-030a9976-e9f5-4285-a8a7-26c23b8de070.png" height="250px"/>

<br>

1)의 과정을 통하여, 모든 박스들 사이의 Area Recall, Area Precision을 계산해 놓습니다. 이해를 쉽게 하기 위해서, 왼쪽에 정답박스와 예측박스를 겹쳐서 그렸습니다.

<img src="https://user-images.githubusercontent.com/9074297/207590690-45ef2028-fc22-44a0-ae9d-823c0aa2d09f.png" height="250px"/>

<br>

G1과 P1은 one-to-one match가 성립되었고, Area Recall, Area Precision 모두 0.99로 threshold 이상이므로, 정답으로 책정됩니다.

G2, G3와 P2는 many-to-one match가 성립되었고, Area Recall 0.9(0.81+0.99)/2, Area Precision 0.91(0.41+0.5) 로 threshold 이상으로 정답으로 책정되었습니다.

G4와 P3, P4는 one-to-many match가 성립되었고, Area Recall 0.88(0.46+0.42), Area Precision 0.96(1.0+0.92)/2 로 threshold 이상으로 정답으로 책정되었습니다.

따라서, 현재 이미지에서의 Recall, Precision, H-mean(F1 score)을 구해보면

- $Recall = ( 1 \times G1 + 1 \times G2 + 1 \times G3 + 0.8 \times G4) \div 4(len(gt)) = 0.95$
- $Precision = (1 \times P1 + 1 \times P2 + 0.8 \times P3 + 0.8 \times P4) \div 4(len(prediction)) = 0.9$
- $H-mean = 2 \times 0.95 \times 0.9 \div (0.95 + 0.9) = 0.92$

가 되어, 해당 이미지에 대해서 최종적으로 0.92점을 부여하게 됩니다.

<br>

#### 3) 모든 이미지에 대하여 Recall, Precision을 구한 이후, 최종 F1-Score은 모든 이미지 레벨에서 측정 값의 평균으로 측정됩니다.

테스트 셋은 여러장의 이미지로 구성되어있는데요, 위의 예시에서처럼 모든 이미지들에 대해서 Recall, Precision, 점수를 구한 이후, 모든 이미지들에 대해서 해당 값을 평균내어 최종 점수를 구하게 됩니다.

예) image1, image2 두개의 테스트 이미지가 존재하고, 계산의 편의성을 위해서 image1은 위의 예시와 동일, image2는 정답/예측박스가 1개이고 맞았다고 가정하고 계산해보면

- $Final Recall = (1 + 1 + 1 + 0.8 + 1) \div 5 = 0.96$
- $Final Precision = (1 + 1 + 0.8 + 0.8 + 1) \div 5 = 0.92$
- $Final F1 = 2 \times 0.96 \times 0.92 \div (0.96 + 0.92) = 0.94$

(분모가 5인 이유: image1에서 정답/예측박스 4개, image2에서 정답/예측박스가 1개이므로)

해당 테스트 셋에서 최종 점수는 0.94 점이 되겠습니다.

### Reference

- Wolf, C., & Jolion, J. M. (2006). Object count/area graphs for the evaluation of object detection and segmentation algorithms. (IJDAR), 8(4), 280-296.

</details>

<br>

## 👀 How to Start

```bash
$ apt-get update
$ apt-get install ffmpeg libsm6 libxext6  -y
$ git clone https://github.com/boostcampaitech4lv23cv3/level2_objectdetection_cv-level2-cv-17.git
$ mv code/pths pths
$ mv code code0
$ ln -s level2_objectdetection_cv-level2-cv-17/src code
$ cd level2_objectdetection_cv-level2-cv-17
$ conda env create -f "environment.yml"
$ conda activate "boostcamp"
$ sh ./script/download_dataset.sh
```
