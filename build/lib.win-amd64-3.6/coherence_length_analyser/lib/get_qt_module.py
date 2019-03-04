# pylint: disable=C0111
# pylint: disable=C1133
import pkg_resources


class PythonQtError(RuntimeError):
    """Error raise if no bindings could be selected."""
    pass


def get_available_modules():
    '''gets a list of all availible modules'''
    package_list = []
    for dist in pkg_resources.working_set:
        package_list.append(dist.project_name.replace('Python', ''))

    package_list = sorted(package_list, key=lambda s: s.casefold())

    return package_list


def get_qt_module():
    """returns the preferred Qt binding"""
    list_of_packages = get_available_modules()
    if 'PySide2' in list_of_packages:
        return 'pyside2'
    if 'PySide' in list_of_packages:
        return 'pyside'
    if 'PyQt5' in list_of_packages:
        return 'pyqt5'
    if 'PyQt4' in list_of_packages:
        return 'pyqt4'
    raise PythonQtError('No Qt bindings could be found')
