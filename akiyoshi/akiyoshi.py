#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import lib.exceptions

__version__ = "0.1.0"
__release__ = "1"
__app__ = "akiyoshi"

options = None # @see bootstrap.start
config = None # @see bootstrap.start
log = None # @see bootstrap.start
plugins = {} # @see plugin.load


dirname=os.path.dirname(__file__)


