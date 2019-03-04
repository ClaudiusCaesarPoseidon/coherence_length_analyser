import numpy as np
from .functions import save_txt


def build_csv(path, out_path):
    """builds a csv file from the values in the file(path)"""
    with open(path, "r") as file:
        # reads the lines from the file and parses it to a dictionary
        tmp = file.read()
        tmp = [x.split("\t") for x in tmp.split("\n")]
        csv_dict = {}
        for item in tmp:
            tempo = item[0].split("_")

            try:
                current = tempo[-1]
                temp = tempo[-2]
                lines = item[1]
                angle = item[2]
                tempo = (item[-1].split(";")[-1]).replace("Kaiser ", "")
                pos1 = tempo.find("(")
                pos2 = tempo.find(")")
                tempo = float(tempo.replace(
                    tempo[pos1:pos2 + 1], "").split()[-1])

                # sets the settings as key for the dictionary
                key = temp + '/' + current + "/" + lines + '/' + angle

                # sets the value as value for the key or appends the the list
                tmp_value = csv_dict.get(key)
                if tmp_value is not None:
                    tmp_value.append(tempo)
                    csv_dict[key] = tmp_value
                else:
                    csv_dict[key] = [tempo]

            except IndexError:
                # ignores line if it does not follow the right format
                continue

        # converts the keys and items to a 1D array
        csv = None
        for item in csv_dict:
            item2 = item.split("/")
            temp = float(item2[0])
            current = float(item2[1])
            lines = float(item2[2])
            angle = float(item2[3])
            array = np.array([current, temp, lines, angle])
            array = np.concatenate((array, csv_dict.get(item)))
            if csv is not None:
                csv = np.concatenate((csv, array), axis=0)
            else:
                csv = array.copy()

        # reshapes the array to 2D
        tmp = int(len(csv_dict.get(item)) + 4)
        temp = int(len(csv) / tmp)
        csv = csv.reshape(temp, tmp)

        # saves to array to file
        save_txt(out_path, csv)

        # reads the file and adds the column heads
        with open(out_path, "r+") as file:
            tmp = file.read()
            temp = tmp.split("\n")[0].split(",")
            length = len(temp) - 4
            first_line = ["Strom", "Temperatur", "Anzahl", "Winkel"]
            second_line = ["[mA]", "[°C]", "[1]", "[°]"]
            if length == 1:
                first_line.append("Kohärenzlänge")
                second_line.append("[µm]")
            else:
                for i in range(1, length + 1):
                    first_line.append("Kohärenzlänge %d" % i)
                    second_line.append("[µm]")
            head = ','.join(first_line) + "\n" + ','.join(second_line) + "\n"
            tmp = head + tmp
            file.seek(0)
            file.write(tmp)


if __name__ == '__main__':
    csvv = build_csv(
        r"C:\Users\Haarmeyer\OUT\coherence_length_analyser\lines.txt")
    print(csvv)
