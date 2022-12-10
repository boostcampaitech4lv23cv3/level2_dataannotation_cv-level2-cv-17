# 서버 폴더 구조 유지하면서 Git으로 협업하기

GitHub를 통해 협업을 해야 하는데,

이번 대회는 서버 스냅샷으로 제출하기 때문에 서버의 폴더 구조를 유지해야 한다.

어떻게 할 수 있을까? 🤔

---

## ⚡ 심플 가이드 ⚡

1. 서버에 있던 code 폴더를 code0로 폴더명 변경을 한다.
2. level2_dataannotation_cv-level2-cv-17 프로젝트를 git clone 한다.
3. level2_dataannotation_cv-level2-cv-17 안의 src 폴더를 code 이름으로 심볼릭링크(바로가기)를 만든다.
4. 심볼릭링크(바로가기)가 잘 만들어졌는지 확인한다.
5. 기존에 협업하듯이 level2_dataannotation_cv-level2-cv-17에서 작업한다.

---

## ✨ 상세 가이드 ✨

<br>

### 1. 서버의 기본 code 폴더를 code0로 변경하자.

VSCode에서 우클릭으로 폴더명을 변경할 수 있다. (또는 `move code code0` 명령어를 쓰면 된다.)

<p float="left">
  <img src="https://user-images.githubusercontent.com/9074297/206821911-b0ab8577-6ce3-4ce0-bae9-79760979a34c.png" width="250" />
  <img src="https://user-images.githubusercontent.com/9074297/206821895-1f68e20c-803b-477d-9992-82b49d12154c.png" width="250" />
</p>

<br>

### 2. level2_dataannotation_cv-level2-cv-17 프로젝트를 git clone 한다.

터미널에서 git clone 명령어로 프로젝트를 받아온다.

```shell
git clone https://github.com/boostcampaitech4lv23cv3/level2_dataannotation_cv-level2-cv-17.git
```

VSCode에서 level2_dataannotation_cv-level2-cv-17 폴더가 생긴 것을 볼 수 있고,

그 안에 src 폴더도 볼 수 있다.    (제가 미리 baseline code를 src 폴더 안에 넣어놨습니다.)

<p float="left">
  <img src="https://user-images.githubusercontent.com/9074297/206821899-95066ebb-a935-4155-9612-fe92b33c75f7.png" width="250" />
  <img src="https://user-images.githubusercontent.com/9074297/206821900-6b2b1cd8-48be-434b-a9e7-a786f206a32e.png" width="250" />
</p>

<br>

### 3. src 폴더를 code 이름으로 심볼릭링크(바로가기)를 만든다.

level2_dataannotation_cv-level2-cv-17 안에 있는 src 폴더의 심볼릭링크(바로가기)를 만들어서 /opt/ml/code가 있는 것처럼 만들 수 있다.

홈 위치(`/opt/ml`)에서 `ln -s level2_dataannotation_cv-level2-cv-17/src code` 와 같이 상대경로로 만들거나,

현재 경로가 어딘지 상관없이 절대경로로 만들 수 있다.

```shell
# 홈 위치에서 상대경로로 만들기
root@c77c3b449fd8:~# ln -s level2_dataannotation_cv-level2-cv-17/src code

# 전체경로로 만들기
ln -s /opt/ml/level2_dataannotation_cv-level2-cv-17/src /opt/ml/code
```

<br>

### 4. 심볼릭링크(바로가기)가 잘 만들어졌는지 확인한다.

심볼릭링크(바로가기)가 잘 만들어졌는지 정확하게 확인하기 위해서는 터미널에서 확인해야 한다.

홈 위치(`/opt/ml`)에서 `ls -al` 명령어을 통해 확인할 수 있다.


![Untitled 4](https://user-images.githubusercontent.com/9074297/206821903-6fd4fa3a-6608-400b-a408-4788f58eaa41.png)

또는 절대경로로 아래와 같이 확인할 수도 있다.


![Untitled 5](https://user-images.githubusercontent.com/9074297/206821904-742d623c-d8e1-49d4-97b4-bd5aee1e5a4e.png)

주로 VSCode로 작업을 하니, VSCode에서도 정상 작동하는지 확인해보자.

code 밑에 새로운 파일을 만들면, src 밑에 그 파일이 보일 것이다. (안 보이면 새로고침을 해보자)

거꾸로 src 밑에 새로운 파일을 만들면, code 밑에 그 파일이 보일 것이다.

<p float="left">
  <img src="https://user-images.githubusercontent.com/9074297/206821908-f1350887-55de-408d-ba06-e01318db95df.png" width="250" />
  <img src="https://user-images.githubusercontent.com/9074297/206821909-d9f4ae5a-7d2a-4df5-80d2-a5db98843acb.png" width="250" />
</p>

<br>

### 5. 기존에 협업하듯이 level2_dataannotation_cv-level2-cv-17에서 작업한다.

지난 대회에서 협업하듯이 clone한 폴더에서 작업을 하면 되고, 제출할 때에도 그대로 서버 저장 후 제출하면 된다.

⚠️ 단, `latest.pth` 파일이 `/opt/ml/code/trained_models/` 경로 아래에 있어야 하고, 실제로는 `/opt/ml/level2_dataannotation_cv-level2-cv-17/src/trained_models/` 경로 아래에 있어야 한다. 그러므로 `train.py`를 어디서 돌리든 상관없이 저 위치에 저장될 수 있도록 **절대경로**로 명시하자.
