import numpy as np
from .functions import save_txt


def build_csv(path, out_path):
    with open(path, "r") as file:
        tmp = file.read()
        tmp = [x.split("\t") for x in tmp.split("\n")]
        csv_dict = {}
        for item in tmp:
            tempo = item[0].split("_")
            print(item)
#            glubber = item[1]
            try:
                current = tempo[-1]
                temp = tempo[-2]
                tempo = (item[-1].split(";")[-1]).replace("Kaiser ", "")
                pos1 = tempo.find("(")
                pos2 = tempo.find(")")
                tempo = float(tempo.replace(tempo[pos1:pos2+1], "").split()[-1])
                key = temp + '/' + current + "/"# + glubber
                tmp_value = csv_dict.get(key)
                if tmp_value is not None:
                    tmp_value.append(tempo)
                    csv_dict[key] = tmp_value
                else:
                    csv_dict[key] = [tempo]
            except IndexError:
                continue
#        csv = None
#        for item in csv_dict:
#            item2 = item.split("/")
#            temp = float(item2[0])
#            current = float(item2[1])
#            lines = float(item2[2])
#            array = np.array([current, temp, lines])
#            array = np.concatenate((array, csv_dict.get(item)))
#            try:
#                csv = np.concatenate((csv, array), axis=0)
#            except UnboundLocalError:
#                csv = array.copy()
#        tmp = int(len(csv_dict.get(item)) + 2)
#        temp = int(len(csv)/tmp)
#        csv = csv.reshape(temp, tmp)
#        save_txt(out_path, csv)


if __name__ == '__main__':
    csvv = build_csv(r"C:\Users\Haarmeyer\OUT\coherence_length_analyser\lines.txt")
    print(csvv)