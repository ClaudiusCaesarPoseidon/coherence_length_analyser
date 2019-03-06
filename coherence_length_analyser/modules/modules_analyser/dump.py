





                        cap = cv2.VideoCapture(path)
                        ret, frame = cap.read()
                        c = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    dft = functions.dft(c)
                    fft = functions.fft_cv2(dft)
                    fft = functions.fft_shift_py(
                        fft.astype(np.float64)).astype(np.uint8)
                    row, col = fft.shape
                    h_fft, w_fft = fft.shape
                    row, col = int(row / 2), int(col / 2)
                    tmp_value = int(
                        int(self.parent.Section_Size_Text.text()) / 2)
                    section = fft[row - tmp_value:row +
                                  tmp_value, col - tmp_value:col + tmp_value]
                    h_sec, w_sec = section.shape
                    for glubber in range(11, 2, -2):  # 11 - 3

                        # find maxima in FFT
                        points = functions.maxi(
                            section, max_count, glubber, 0)
                        if len(points) > 0:
                            points = tuple(map(tuple, points))
                            indexes.append(points)
                            frame_number = i
                            break
                    i += 1

            else:
                self.ind = (self.parent.Spin_Row.value(),
                            self.parent.Spin_Col.value())
                print("Skipping Peak Detectcion. Using provided Peak Location.")
            print("The second run is to determine the theshold value.")
            print("Please wait.")
            cap = cv2.VideoCapture(path)
            data = []
            x = []
            i = 0
            if video is True and self.parent.ends is False:

                # save the intensity values of the FFT at the location
                # of the peak and the relative motor position in lists
                while True:
                    if self.parent.ends is True:
                        break
                    ret, frame = cap.read()
                    if ret is False:
                        break
                    else:
                        c = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                        dft = functions.dft(c)
                        fft = functions.fft_cv2(dft)
                        fft = functions.fft_shift_py(
                            fft.astype(np.float64)).astype(np.uint8)
                        row, col = fft.shape
                        h_fft, w_fft = fft.shape
                        row, col = int(row / 2), int(col / 2)
                        tmp_value = int(
                            int(self.parent.Section_Size_Text.text()) / 2)
                        section = fft[row - tmp_value:row + tmp_value,
                                      col - tmp_value:col + tmp_value]
                        h_sec, w_sec = section.shape
                        data.append(section[self.ind])
                        x.append(step_width * i)
                        i += 1

            # calculates threshold value
            if video is True and self.parent.ends is False:
                data_a = np.array(data)
                tmp_for_filter = self.parent.Filter_Switch.currentIndex()
                data_a = choose_filter(data_a, tmp_for_filter, x)
                threshold, maxi, mini = functions.threshold(
                    data_a, 7.5)
                data_threshold = [threshold] * len(data)
                data_maxi = [maxi] * len(data)
                data_mini = [mini] * len(data)
                array_max = np.argmax(data_a)

                cap.set(cv2.CAP_PROP_POS_FRAMES, array_max)
                ret, frame = cap.read()
                c = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                dft = functions.dft(c)
                fft = functions.fft_cv2(dft)
                fft = functions.fft_shift_py(
                    fft.astype(np.float64)).astype(np.uint8)
                row, col = fft.shape
                h_fft, w_fft = fft.shape
                row, col = int(row / 2), int(col / 2)
                tmp_value = int(
                    int(self.parent.Section_Size_Text.text()) / 2)
                section = fft[row - tmp_value:row + tmp_value,
                              col - tmp_value:col + tmp_value]
                h_sec, w_sec = section.shape
                section = cv2.cvtColor(
                    section, cv2.COLOR_GRAY2BGR)
                section[self.ind] = [0, 0, 255]

                # save FFT and image at maximum intensity
                if self.parent.demo is False:
                    cv2.imwrite(os.path.join(
                        file_direc, file_name + "_alignment2.png"), c)
                    cv2.imwrite(
                        os.path.join(
                            file_direc,
                            file_name +
                            "_alignment_%d.png" %
                            tmp_value),
                        section)

                # display FFT and image at maximum intensity
                section = functions.resize(
                    section, h_fft / h_sec, w_fft / w_sec)
                c = cv2.cvtColor(
                    c, cv2.COLOR_GRAY2BGR)
                fft = cv2.cvtColor(
                    fft, cv2.COLOR_GRAY2BGR)
                res = np.concatenate(
                    (c, fft, section), axis=1)
                convertToQtFormat = qimage2ndarray.array2qimage(
                    res).rgbSwapped()
                p_cv2 = convertToQtFormat.scaled(
                    self.parent.cv2_width,
                    self.parent.cv2_height,
                    QtCore.Qt.KeepAspectRatio)
                self.changePixmap.emit(p_cv2)
                print("The third run is to determine the coherence length.")
                print("Please wait.")

            if video is True and self.parent.ends is False:
                # set matplotlib image dpi
                self.parent.canvas.figure.set_dpi(h_dpi)
                self.parent.canvas.figure.set_size_inches(
                    self.parent.pyplot_width / h_dpi, self.parent.pyplot_height / h_dpi)
                self.ax.clear()
                if x[-1] >= 50:
                    self.ax.xaxis.set_major_locator(
                        ticker.MultipleLocator(10))
                self.ax.margins(x=0)

                # plot graph
                self.ax.plot(x, data_a, color="black")
                self.ax.plot(x, data_threshold, color="red")
                self.ax.plot(x, data_maxi, color="cyan")
                self.ax.plot(x, data_mini, color="magenta")

                # calculate coherence length by
                # finding the position of the first value above the treshold
                # and the position of the first value under the treshold and
                # after the maximum and calculating the distance between
                # theese points
                if self.parent.Calculate.isChecked() is True:
                    s = -1
                    e = 0
                    for i, item in zip(x, data_a):
                        if self.parent.ends is True:
                            break
                        j = i / step_width
                        if item > threshold and s == -1:
                            s = j
                        elif item < threshold and s != -1 and e == 0 and j > array_max:
                            e = j
                    print(
                        "The Coherence Length is:",
                        (e - s) * step_width)

                    # add the parameters to the plot
                    self.ax.axvline(s * step_width, color="green")
                    self.ax.axvline(e * step_width, color="green")
                    self.parent.canvas.figure.text(
                        0.0, 0.97, "Results:", fontsize=8, zorder=10)
                    self.parent.canvas.figure.text(
                        0, 0.94, "First Occurence:", fontsize=8, zorder=10)
                    self.parent.canvas.figure.text(
                        0, 0.91, "%0.2f" %
                        (s * step_width), fontsize=8, zorder=10)
                    self.parent.canvas.figure.text(
                        0, 0.89, "Last Occurence:", fontsize=8, zorder=10)
                    self.parent.canvas.figure.text(
                        0, 0.86, "%0.2f" %
                        (e * step_width), fontsize=8, zorder=10)
                    self.parent.canvas.figure.text(
                        0, 0.83, "Coherence Length:", fontsize=8, zorder=10)
                    self.parent.canvas.figure.text(0, 0.81, "%0.2f" % (
                        (e - s) * step_width), fontsize=8, zorder=10)
                    self.parent.canvas.figure.text(
                        0, 0.78, "Maximum Value:", fontsize=8, zorder=10)
                    self.parent.canvas.figure.text(
                        0, 0.75, "%0.2f" % maxi, fontsize=8, zorder=10)
                    self.parent.canvas.figure.text(
                        0, 0.72, "Minumum Value:", fontsize=8, zorder=10)
                    self.parent.canvas.figure.text(
                        0, 0.69, "%0.2f" % mini, fontsize=8, zorder=10)
                    self.parent.canvas.figure.text(
                        0, 0.66, "Threshold Value:", fontsize=8, zorder=10)
                    self.parent.canvas.figure.text(
                        0, 0.63, "%0.2f" %
                        threshold, fontsize=8, zorder=10)
                    current = float(os.path.splitext(
                        os.path.basename(path))[0].split("_")[-2])
                    temperature = float(os.path.splitext(
                        os.path.basename(path))[0].split("_")[-3])
                    max_width = float(os.path.splitext(
                        os.path.basename(path))[0].split("_")[-4])
                    temp = os.path.splitext(os.path.basename(path))[
                        0].split("_")[0][-1]
                    if temp == "f":
                        mode = "forward"
                    elif temp == "b":
                        mode = "backward"
                    else:
                        mode = "No mode specified"
                    self.parent.canvas.figure.text(
                        0, 0.50, "Parameters:", fontsize=8, zorder=10)
                    self.parent.canvas.figure.text(
                        0, 0.47, "Temperature:", fontsize=8, zorder=10)
                    self.parent.canvas.figure.text(
                        0, 0.44, "%0.2f" %
                        temperature, fontsize=8, zorder=10)
                    self.parent.canvas.figure.text(
                        0, 0.41, "Current:", fontsize=8, zorder=10)
                    self.parent.canvas.figure.text(
                        0, 0.38, "%0.2f" %
                        current, fontsize=8, zorder=10)
                    self.parent.canvas.figure.text(
                        0, 0.35, "Step_Width:", fontsize=8, zorder=10)
                    self.parent.canvas.figure.text(
                        0, 0.32, "%0.2f" %
                        step_width, fontsize=8, zorder=10)
                    self.parent.canvas.figure.text(
                        0, 0.29, "Total Length:", fontsize=8, zorder=10)
                    self.parent.canvas.figure.text(
                        0, 0.26, "%0.2f" %
                        max_width, fontsize=8, zorder=10)
                    self.parent.canvas.figure.text(
                        0, 0.23, "Mode:" + mode, fontsize=8, zorder=10)
                    self.parent.canvas.figure.text(
                        0, 0.20, "filter used:", fontsize=8, zorder=10)
                    if tmp_for_filter == 0:
                        filter_string = "None\n"
                        filter_name = "wo"
                    elif tmp_for_filter == 1:
                        filter_string = "Moving Average\n"
                        filter_name = "m-a"
                    elif tmp_for_filter == 2:
                        filter_string = "Savitzky–Golay\n"
                        filter_name = "s-g"
                    elif tmp_for_filter == 3:
                        filter_string = "first moving Average\nthen Savitzky–Golay"
                        filter_name = "m-a_s-g"
                    elif tmp_for_filter == 4:
                        filter_string = "Median\n"
                        filter_name = "me"
                    elif tmp_for_filter == 5:
                        filter_string = "First Median\nthen Savitzky–Golay"
                        filter_name = "me_s-g"
                    elif tmp_for_filter == 6:
                        filter_string = "FFT\n"
                        filter_name = "fft"
                    elif tmp_for_filter == 7:
                        filter_string = "First FFT\nthen Savitzky–Golay"
                        filter_name = "fft_s-g"

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
