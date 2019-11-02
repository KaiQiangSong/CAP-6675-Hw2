#!/usr/bin/env python3

import sys
import csv

HEADER_FRAG = 'x,y,color,pen down?'

def gnuplot_prep(raw_csv_input, prepped_csv_output):
  header_found = False
  raw_reader = csv.reader(raw_csv_input, delimiter=',', quotechar='"')
  prepped_writer = csv.writer(prepped_csv_output, delimiter=',')
  for row in raw_reader:
    if len(row) != 12:
      # Bad row?
      continue
    if not header_found:
      header_found = (
        (len(row) == 12) and
        (','.join(row[0:4]) == HEADER_FRAG) and
        (','.join(row[4:8]) == HEADER_FRAG) and
        (','.join(row[8:12]) == HEADER_FRAG)
      )
    else:
      prepped_writer.writerow(
        [row[0], row[1], row[5], row[9],]
      )

if __name__ == '__main__':
  gnuplot_prep(sys.stdin, sys.stdout)
  exit(0)

# vim: set ts=2 sw=2 expandtab:
