# conda 환경
​
conda 환경을 하나라도 생성하면, 서버 제출시 아래와 같이 디스크 사용량을 15GB 이하로 만들어달라는 에러가 발생한다.

<img width="250" alt="image" src="https://user-images.githubusercontent.com/9074297/206820814-b7c93415-86fe-4d1c-beca-bdaca603baba.png">

<br>

🤔 "AI Stages Inference 경진대회 참여 가이드"를 보면 아래와 같이 /opt/ml/input/data 경로 하위의 파일들은 모두 제외된다고 하는데, 그럼 이 아래에 conda 환경을 만들면 되지 않나?

<img width="619" alt="Screenshot 2022-12-09 at 12 45 32 PM" src="https://user-images.githubusercontent.com/9074297/206820993-cb9277bd-ea6a-4b1a-b6de-2cf1b02876b8.png">

<br>

👉 아래 명령어를 통해 `/opt/ml/input/data/conda` 경로로 conda 환경을 생성해서 제출한 결과, 역시 동일한 에러가 발생했다.
```shell
conda env create --prefix /opt/ml/input/data/conda -f environment.yml
```

<br>

💡 결론 : conda 환경을 하나라도 생성하면 서버 제출시 용량 제한 에러가 발생하므로, 제출할 때에는 무조건 conda 환경을 삭제해야 한다.

<br>

### conda 환경 생성

```shell
conda create env -f environment.yml
```

### conda 환경 삭제

```shell
conda env remove -n boostcamp
```

### conda 용량 정리하기
```bash
conda clean --yes --all
```
