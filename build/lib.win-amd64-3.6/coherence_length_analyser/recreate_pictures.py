import os
import cv2


def index_containing_substring(the_list, substring):
    for i, s in enumerate(the_list):
        if substring in s:
            return i
    return None


def hasNumber(inputString):
    return any(char.isdigit() for char in inputString)


user_path = os.path.expanduser('~')
direc_path = os.path.join(user_path, "OUT", "coherence_length_analyser")
path = os.path.join(direc_path, "converted_videos")
tmp = [x[0] for x in os.walk(path) if hasNumber(x[0]) is True]
for item in tmp:
    direc_name = os.path.basename(item)
    new_direc = os.path.join(direc_path, direc_name)
    if os.path.exists(new_direc) is True:
        continue
    x = os.listdir(item)
    index = index_containing_substring(x, "Boxcar")
    try:
        file = x[index]
    except TypeError:
        continue
    path = os.path.join(item, file)
    temp = os.path.basename(path)
    temp = os.path.splitext(temp)[0]
    temp = temp.split("_")
    mode = temp[0]
    mode = mode.replace(mode[:3], "")
    if len(mode) > 1:
        mode = mode.replace(mode[-1], "")
    del temp[0]
    del temp[0]
    temp = '_'.join(temp)
    mode = "img" + mode
    i = 0
    cap = cv2.VideoCapture(path)
    os.makedirs(new_direc)
    while True:
        ret, frame = cap.read()
        if ret is False:
            break
        c = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        string = mode + '_%d_' % i + temp + ".png"
        save_path = os.path.join(new_direc, string)
        cv2.imwrite(save_path, c)
        i += 1
    print("finished: ", new_direc)
