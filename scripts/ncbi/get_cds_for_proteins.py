#!/usr/bin/env python
__author__ = 'Sergei F. Kliver'
import os
import argparse

from Pantera.Routines import NCBIRoutines


parser = argparse.ArgumentParser()

parser.add_argument("-i", "--input", action="store", dest="input", required=True,
                    help="Input file with ids of ncbi peptides")
parser.add_argument("-o", "--output_prefix", action="store", dest="output_prefix", required=True,
                    help="Prefix of output files")

args = parser.parse_args()

NCBIRoutines.get_cds_for_proteins_from_id_file(args.input, args.output_prefix)
