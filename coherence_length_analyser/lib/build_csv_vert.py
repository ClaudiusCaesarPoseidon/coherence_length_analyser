import os


path = r"C:\Users\Haarmeyer\OUT\coherence_length_analyser\converted_videos"
def build_csv_vert(path, out_path):
    tmp = [z for x, y, z in os.walk(path)]
    tmp = [os.path.abspath(val) for sublist in [[os.path.join(i[0], j) for j in i[2]]
                                                for i in os.walk(path)] for val in sublist if val.endswith(".txt")]

    lst = [[],[]]
    i = 1
    for item in tmp:
        name = os.path.dirname(item)
        with open(item, "r") as file:
            tmp = file.read()
        tmp = tmp.split("\t")[-1]

        pos1 = tmp.find("(")
        pos2 = tmp.find(")")
        tmp = tmp.replace(
            tmp[pos1:pos2 + 1], "").split()[-1]
        lst[0].append(str(i))
        lst[1].append(tmp)
        i+=1
    #print(lst)
    lst = list(map(list, zip(*lst)))
    string = '\n'.join([','.join(x) for x in lst])
#    print(string)
    with open(out_path, "w") as file:
        file.write(string)

if __name__ == '__main__':
    path = r"C:\Users\Haarmeyer\OUT\coherence_length_analyser\converted_videos"
    path2 = r"C:\Users\Haarmeyer\OUT\coherence_length_analyser\csv_vert.csv"
    build_csv_vert(path, path2)