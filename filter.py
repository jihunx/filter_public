import os

# 필터링할 대상 디렉터리를 입력합니다.
target_dir = r"/volume2/mac"

# 필터링 키워드가 입력돼 있는 파일 경로를 입력합니다.
filter_list = r"/volume1/homes/jihunx/filter/filterlist.txt"


# 필터링 키워드 파일을 리스트로 만든다.
def get_string(file):
    global strlist
    with open(file, "r", encoding="utf-8-sig") as f:
        strlist = [i.rstrip() for i in f.readlines() if len(i) > 1]


filelist = []


# 필터링할 대상 디렉터리의 하위 디렉터리까지 모든 파일 리스트를 만든다.
def listing(path):
    global filelist
    filenames = os.listdir(path)
    for item in filenames:
        if os.path.isdir(os.path.join(path, item)):
            listing(path + "/" + item)
        else:
            filelist.append(os.path.join(path, item))


def filtering():
    # 파일 리스트 중 하나를 꺼낸다.
    for item in filelist:
        # 파일을 경로와 이름으로 나눈다.
        path, file = os.path.split(item)
        # 필터링할 키워드가 파일 이름에 포함된 경우 제거하는 동작을 반복한다.
        for str in strlist:
            if str in file:
                file = file.replace(str, "")
            continue
        # 기존 경로와 변경된 이름을 새로운 변수에 저장한다.
        new_name = os.path.join(path, file)
        # 원래 파일 이름과 변경된 이름이 같지 않을 경우 파일명을 변경한다.
        if item != new_name:
            os.rename(r"%s" % item, r"%s" % new_name)
            print("[File renamed] {} ===> {}".format(item, new_name))
        continue


get_string(filter_list)
listing(target_dir)
filtering()
