import winreg
import distutils.msvccompiler


def get_visual_studio_installed_version():
    key = r"SOFTWARE\Microsoft\VisualStudio\%s"

    possible_versions = ["9.0", "10.0", "11.0", "12.0", "14.0", "15.0", "16.0"]
    installed_versions = []

    for v in possible_versions:
        try:
            winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key %
                           v, 0, winreg.KEY_READ)
            installed_versions.append(v)
        except Exception:
            pass
    return installed_versions


def get_build_version_major():
    tmp = distutils.msvccompiler.get_build_version()
    tmp = str(float(int(tmp)))
    return tmp


def right_msvc_version_installed():
    return get_build_version_major() in get_visual_studio_installed_version()


if __name__ == '__main__':
    print(get_visual_studio_installed_version())
    print(get_build_version_major())
    print(right_msvc_version_installed())
