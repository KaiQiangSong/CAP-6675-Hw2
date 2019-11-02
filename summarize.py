#!/usr/bin/env python3

import sys
import csv

def produce_summary(filtered_csv_input):
  total_rebellions = 0
  total_rebellion_durations = 0
  total_rebellion_sizes = 0.
  filtered_reader = csv.reader(filtered_csv_input, delimiter=',')
  for a_row in filtered_reader:
    total_rebellions += 1
    total_rebellion_durations += int(a_row[0])
    total_rebellion_sizes += float(a_row[1])
  if total_rebellions > 0:
    avg_rebellion_duration = float(total_rebellion_durations) / float(total_rebellions)
    avg_rebellion_size = total_rebellion_sizes / float(total_rebellions)
    return '{},{},{}'.format(total_rebellions, avg_rebellion_duration, avg_rebellion_size)

if __name__ == '__main__':
  print(produce_summary(sys.stdin))
  exit(0)

# vim: set ts=2 sw=2 expandtab:
