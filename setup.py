import sys, os
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = r'C:\\Python37-32\\tcl\\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\\Python37-32\\tcl\\tk8.6'
includes      = []
include_files = [r"C:\\Python37-32\\DLLs\\tcl86t.dll",
                 r"C:\\Python37-32\\DLLs\\tk86t.dll"]

setup(
    name = "Cryptage",
    version = "1.0",
    options = {"build_exe": {"includes": includes, "include_files": include_files}},
    executables = [Executable("interface.py", base="Win32GUI")]
)