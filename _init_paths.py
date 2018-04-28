'''
Wrapper to add the library paths to any training/test functions
'''
import os.path as osp
import sys


def add_path(path):
    '''Prepend to system path'''
    if path not in sys.path:
        sys.path.insert(0, path)


THIS_DIR = osp.dirname(__file__)

# Add lib to PYTHONPATH
LIB_PATH = osp.join(THIS_DIR, 'lib')
add_path(LIB_PATH)

COCO_PATH = osp.join(THIS_DIR, 'data', 'coco', 'PythonAPI')
add_path(COCO_PATH)
