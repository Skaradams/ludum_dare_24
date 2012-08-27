import settings
import os
import sys
from distutils.core import setup
import py2exe
from bloodyhell.packager import Packager

DIST_DIR = os.path.join(settings.EXEC_DIR, 'dist')
TARGET_RES_DIR = os.path.join(DIST_DIR, 'res')

origIsSystemDLL = py2exe.build_exe.isSystemDLL


def isSystemDLL(pathname):
    if os.path.basename(pathname).lower() in ["sdl_ttf.dll"]:
        return 0
    return origIsSystemDLL(pathname)

py2exe.build_exe.isSystemDLL = isSystemDLL


def build_all(argv):
    setup(console=['PimpMyRat.py'])
    packager = Packager(settings.RESOURCES_DIR, TARGET_RES_DIR)
    packager.save_all()


if __name__ == '__main__':
    build_all(sys.argv)



