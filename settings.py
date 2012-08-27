import os
import sys

if not hasattr(sys, 'frozen'):
    EXEC_DIR = os.path.dirname(__file__)
    BLOODYHELL_DIR = os.path.join(EXEC_DIR, 'bloodyhell')
    sys.path.insert(0, BLOODYHELL_DIR)
else:
    EXEC_DIR = os.path.dirname(os.path.abspath(sys.executable))

RESOURCES_DIR = os.path.join(EXEC_DIR, 'res')
INTERFACES_DIR = os.path.join(RESOURCES_DIR, 'interfaces')
RESOLUTION = (800, 600)
FPS = 25
PACKAGES = {
    'static': '  Cleaning pills  ',
    'rat': '  Rendering beards  ',
    'tinyrat': '  Generating peaches ',
    'lumi': '  Feeding developers  ',
    'grasshopper': '  Stealing your coins  ',
    'svg_json': '  Buying plants  ',
    'pill_grasshopper': '  Eating pills  ',
    'pill_tinyrat': '  Duh ! Winning !  ',
    'pill_lumi': '  Stalking your mom  ',
    'music': ' Sacrificing rats '
}
