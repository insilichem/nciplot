#!/usr/bin/env python
# encoding: utf-8

"""
This is the preferences file for the extension. All default values
should be listed here for reference and easy reuse.
"""

# Get used to importing this in your Py27 projects!
from __future__ import print_function, division
import os
# Chimera
from chimera import preferences


def assert_preferences():
    try:
        binary, dat = get_preferences()
    except KeyError:
        binary, dat = '', ''
        preferences.addCategory('plume_nciplot', preferences.HiddenCategory)
    return binary, dat
    
def set_preferences(binary, dat):
    assert_preferences()
    if os.path.isfile(binary) and os.path.isdir(dat):
        preferences.set('plume_nciplot', 'nciplot_bin', binary)
        preferences.set('plume_nciplot', 'nciplot_dat', dat)
        preferences.save(preferences.preferences._filename)
    else:
        raise ValueError('One or more of the specified paths do not exist.')

def get_preferences():
    return preferences.get('plume_nciplot', 'nciplot_bin'), \
           preferences.get('plume_nciplot', 'nciplot_dat')

def test_preferences():
    binary, dat = get_preferences()
    return os.path.isfile(binary) and os.path.isdir(dat)

preferences.addCategory('plume_nciplot', preferences.HiddenCategory)