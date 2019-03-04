# pylint: disable=line-too-long
# pylint: disable=C0103
# pylint: disable=C0111
# pylint: disable=C0330
# pylint: disable=C0413
# pylint: disable=C0412
# pylint: disable=C0410
# pylint: disable=C0411
# pylint: disable=C1801
# pylint: disable=R0902
# pylint: disable=R0903
# pylint: disable=R0201
# pylint: disable=R0914
# pylint: disable=R0912
# pylint: disable=R0915
# pylint: disable=R1702
# pylint: disable=R0912
# pylint: disable=W0703
# pylint: disable=W0123
# pylint: disable=W0104
# pylint: disable=W0621
# pylint: disable=W0613
# pylint: disable=W0612
# pylint: disable=W0603
# pylint: disable=W0611
# pylint: disable=E1101

# loads the main class of the modules_analyser submodule
from .modules_analyser.analyser import Analyser
from ..lib import functions
import matplotlib
import warnings
from ..lib.get_qt_module import get_qt_module
warnings.filterwarnings('error', category=UserWarning, module="matplotlib")

# sets MAtplotlib to use the preferred Qt binding for display
if functions.is_pyinstaller() is False:
    tmp = get_qt_module()
    if tmp in ('pyside2', 'pyqt5'):
        try:
            matplotlib.use("Qt5Agg")
        except Exception:
            pass
    else:
        try:
            matplotlib.use("Qt4Agg")
        except Exception:
            pass
else:
    try:
        matplotlib.use("Qt5Agg")
    except Exception:
        pass
