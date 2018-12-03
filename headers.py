import matplotlib.pyplot as plt
from skimage import io
import math
import numpy as np
from scipy.ndimage import convolve
import sys
import os
import csv
from skimage.transform import rescale, resize
from skimage.draw import line as s_line