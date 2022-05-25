# -*- coding: utf-8 -*-
"""
===================================================================================
Copyright (c) 2022, Deutsches HörZentrum Hannover, Medizinische Hochschule Hannover
Author: Tom Gajecki (gajecki.tomas@mh-hannover.de)
All rights reserved.
===================================================================================
"""

import os
import sys

sys.dont_write_bytecode = True
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from models import Model
from utils import setup

def test(args):
    model = Model(args).call()
    model.summary()

def main() -> None:
    args = setup()
    test(args)
 
if __name__ == '__main__':
    main()
