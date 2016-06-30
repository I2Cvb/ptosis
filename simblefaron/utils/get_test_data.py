"""A set of helper functions to download, import, etc... testing data"""

from __future__ import print_function
from __future__ import division

import os

try:
    # Python 2
    from urllib2 import HTTPError
    from urllib2 import urlopen
except ImportError:
    # Python 3+
    from urllib.error import HTTPError
    from urllib.request import urlopen

from shutil import copyfileobj

def Get_test_data():
    """A helper function to download the testing data.

    .. todo::
        implement testing
    """

    urlname = 'http://img.medscapestatic.com/pi/meds/ckb/97/30797tn.jpg'
    filename = 'file.jpg'
    try:
        url_data = urlopen(urlname)
    except HTTPError as e:
        if e.code == 404:
            e.msg = 'URL {} not found.'.format(urlname)
            raise

    # store Matlab file
    try:
        with open(filename, 'w+b') as image:
            copyfileobj(url_data, image)
    except:
        os.remove(filename)
        raise
        url_data.close()
