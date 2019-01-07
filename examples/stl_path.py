import os
import sys

cur_dir = os.path.dirname(__file__)

# Run from TREX_STL_LIB directory
sys.path.insert(0, "../")
STL_PROFILES_PATH = cur_dir + '/profiles/stl/'
