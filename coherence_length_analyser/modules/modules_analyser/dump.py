

                    elif tmp_for_filter == 2:
                        filter_string = "Savitzky–Golay\n"
                        filter_name = "s-g"

                    elif tmp_for_filter == 3:
                        filter_string = "first moving Average\nthen Savitzky–Golay"
                        filter_name = "m-a_s-g"

                    elif tmp_for_filter == 5:
                        filter_string = "First Median\nthen Savitzky–Golay"
                        filter_name = "me_s-g"

                    elif tmp_for_filter == 7:
                        filter_string = "First FFT\nthen Savitzky–Golay"
                        filter_name = "fft_s-g"
