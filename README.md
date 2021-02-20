# 시놀로지 파일 이름 필터(Synology File Name Filter)
파일 이름에서 원하지 않는 키워드를 제거하는 스크립트입니다.  
<br><br>
## 기능 예시
파일 이름이 `filename_toolong.txt`일 때 `_toolong`을 필터링 키워드로 지정해두면 자동으로 `filename.txt`로 변경됩니다.  
<br><br>
## 실행 방법
1. 시놀로지에 파이썬 설치
2. `제어판 > 작업 스케줄러`에 스케줄 등록
```
sh /volume1/homes/jihunx/filter/filter.sh
```
* `사용자 정의 스크립트`에 위와 같이 등록
* `/volome1/homes/jihunx/filter/filter.sh` 부분에는 `filter.sh` 파일의 절대 경로를 입력합니다.
  <br><br>
## 환경 설정
### 필터링할 키워드 설정
`filterlist.txt` 파일에 키워드를 입력합니다(대소문자를 구분합니다).
* 한줄씩 입력합니다.

### 대상 폴더 설정
`filter.py`에서 설정합니다.
* `target_dir`: 대상 폴더 설정. 끝에 슬래시(/)를 붙이지 않습니다.
* `filter_list`: `filterlist.txt` 파일의 절대 경로 입력

### 쉘 스크립트 설정
`filter.sh`에 `filter.py`의 절대 경로를 입력합니다.