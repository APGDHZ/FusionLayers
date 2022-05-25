# -*- coding: utf-8 -*-
"""
===================================================================================
Copyright (c) 2022, Deutsches HörZentrum Hannover, Medizinische Hochschule Hannover
Author: Tom Gajecki (gajecki.tomas@mh-hannover.de)
All rights reserved.
===================================================================================
"""

import argparse

def setup():
    parser = argparse.ArgumentParser(description='Main configuration')

    parser.add_argument('-top', '--topology', type=str, default="Double_fusion")

    parser.add_argument('-gpu', '--GPU', type=bool, default=False)

    parser.add_argument('-oa', '--output_activation', type=str, default='tanh')
    parser.add_argument('-m', '--metric', type=str, default='SNR')
    parser.add_argument('-sr', '--sample_rate', type=int, default=16000)
    parser.add_argument('-c', '--causal', type=bool, default=True)
    parser.add_argument('-k', '--skip', type=bool, default=True)
    parser.add_argument('-d', '--duration', type=int, default=4)

    parser.add_argument('-e', '--encoding', type=str, default="deep")

    parser.add_argument('-N', '-N', type=int, default=512)
    parser.add_argument('-L', '-L', type=int, default=64)
    parser.add_argument('-B', '-B', type=int, default=64)
    parser.add_argument('-H', '-H', type=int, default=256)
    parser.add_argument('-S', '-S', type=int, default=64)
    parser.add_argument('-P', '-P', type=int, default=256)
    parser.add_argument('-X', '-X', type=int, default=2)
    parser.add_argument('-R', '-R', type=int, default=2)

    args = parser.parse_args()

    return args