




















                    # save plot as png
                    self.parent.canvas.figure.text(
                        0, 0.16, filter_string, fontsize=8, zorder=10)
                    self.parent.canvas.canvas.draw()
                    cap.release()
                    if self.parent.demo is False:
                        tmp_array = np.column_stack((x, data_a))
                        self.parent.canvas.figure.savefig(
                            os.path.join(
                                file_direc,
                                file_name +
                                "_" +
                                filter_name +
                                ".png"),
                            format="png",
                            dpi=h_dpi)
                        functions.save_txt(
                            os.path.join(
                                file_direc,
                                file_name +
                                "_" +
                                filter_name +
                                "_" +
                                (
                                    self.parent.Section_Size_Text.text()) +
                                ".csv"),
                            tmp_array)

                        # save the coherence length in a text file
                        window = file_name.split("_")[1]
                        with open(os.path.join(file_direc, "coherence_length.txt"), "a+") as file:
                            file.seek(0)
                            dump = file.read().split("\n")
                        if dump[0] == '':
                            del dump[0]
                        i = 0
                        for line in dump:
                            if window in line and filter_name in line:
                                dump[i] = window + "\t" + filter_name + "\t" + \
                                    "%0.2f" % (
                                        (e - s) * step_width) + str(self.ind)
                            i += 1
                        if substring_in_list(
                                window + "\t" + filter_name, dump) is True:
                            pass
                        else:
                            dump.append(window +
                                        "\t" +
                                        filter_name +
                                        "\t" +
                                        "%0.2f" %
                                        ((e -
                                          s) *
                                         step_width) +
                                        str(self.ind))
                        with open(os.path.join(file_direc, "coherence_length.txt"), "w") as file:
                            file.write("\n".join(dump))
