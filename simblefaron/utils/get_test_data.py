"""A set of helper functions to download, import, etc... testing data"""

from __future__ import print_function
from __future__ import division
import urllib

def Get_test_data():
    """A helper function to download the testing data.

    .. todo::
        implement testing
    """
    testfile = urllib.URLopener()
    testfile.retrieve("http://img.medscapestatic.com/pi/meds/ckb/97/30797tn.jpg", "file.jpg")

