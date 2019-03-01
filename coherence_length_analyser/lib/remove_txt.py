import os


def remove_txt(path):
    tmp = [z for x, y, z in os.walk(path)]
    tmp = [os.path.abspath(val) for sublist in [[os.path.join(i[0], j) for j in i[2]]
                                                for i in os.walk(path)] for val in sublist if val.endswith(".txt")]
    for file in tmp:
        os.remove(file)


if __name__ == '__main__':
    remove_txt(
        r"C:\Users\Haarmeyer\OUT\coherence_length_analyser\converted_videos")
