import sys
from cx_Freeze import setup, Executable

try:
    from cx_Freeze.hooks import get_qt_plugins_paths
except ImportError:
    include_files = [""]
else:
    # Inclusion of extra plugins (new in cx_Freeze 6.8b2)
    # cx_Freeze imports automatically the following plugins depending of the
    # use of some modules:
    # imageformats - QtGui
    # platforms - QtGui
    # mediaservice - QtMultimedia
    # printsupport - QtPrintSupport
    #
    # So, "platforms" is used here for demonstration purposes.
    include_files = get_qt_plugins_paths("PyQt5", "platforms")

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

build_exe_options = {
    "excludes": ["tkinter"],
    "include_files": include_files,
    "path": sys.path + ["src"],
}

bdist_mac_options = {
    "bundle_name": "Test",
}

bdist_dmg_options = {
    "volume_label": "TEST",
}

executables = [Executable("src/main.py", base=base, target_name="spotify-stats")]

setup(
    name="spotify-stats",
    version="0.1",
    description="Sample cx_Freeze PyQt5 script",
    options={
        "build_exe": build_exe_options,
        "bdist_mac": bdist_mac_options,
        "bdist_dmg": bdist_dmg_options,
    },
    executables=executables,
)