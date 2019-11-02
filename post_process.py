#!/usr/bin/env python3

import os
import re
import sys
from gnuplot_prep import gnuplot_prep
from filter_rebellions import filter_raw_netlogo

def process_directory(dir_path):
  if len(dir_path) == 0:
    raise ValueError('Empty path passed to process_directory()')
  if not os.path.exists(dir_path):
    raise RuntimeError('Could not find path {}'.format(dir_path))
  config_name = os.path.basename(dir_path)
  filtered_path = '{}/{}-filtered.csv'.format(dir_path, config_name)
  with open(filtered_path, 'w', newline='') as filtered_file:
    for a_raw_idx in range(1, 11):
      raw_path = '{}/{}-raw-{}.csv'.format(dir_path, config_name, a_raw_idx)
      if not os.path.exists(raw_path):
        print('WARNING: Could not find NetLogo raw file {}'.format(raw_path))
      gnuplot_path = '{}/{}-gnuplot-{}.csv'.format(dir_path, config_name, a_raw_idx)
      with open(raw_path, newline='') as raw_input:
        gnuplot_prep(raw_input, open(gnuplot_path, 'w'))
        raw_input.seek(0)
        filter_raw_netlogo(raw_input, filtered_file)

if __name__ == '__main__':
  if len(sys.argv) < 2:
    print('Usage: {} <results_dir>'.format(sys.argv[0]))
    exit(1)
  process_directory(sys.argv[1])
  exit(0)

# vim: set ts=2 sw=2 expandtab:
