import sys
import os
# print(sys.path)

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,base_dir)

# import utils
# from utils import cal

from utils.cal import add
from utils.image import get_image

# add(3,5)
get_image()


