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
