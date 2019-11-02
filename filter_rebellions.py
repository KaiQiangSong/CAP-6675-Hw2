#!/usr/bin/env python3

import sys
import csv

HEADER_FRAG = 'x,y,color,pen down?'

WAITFOR_CSV_HEADER_STATE = 0
WAITFOR_AGENT_COUNT_STATE = 1
WAITFOR_REBELLION_START_STATE = 2
WAITFOR_REBELLION_END_STATE = 3

def calc_int_pct(frac, total):
  return (frac * 100) / total

def in_rebellion(active, total):
  return calc_int_pct(active, total) >= 10

if __name__ == '__main__':
  filter_results = []
  reader_state = WAITFOR_CSV_HEADER_STATE
  raw_reader = csv.reader(sys.stdin, delimiter=',', quotechar='"')
  initial_agent_count = 0
  rebellion_start_tick = 0
  rebellion_agent_count = 0
  for row_idx, row in enumerate(raw_reader):
    if len(row) != 12:
      # Bad row?
      continue
    if reader_state == WAITFOR_CSV_HEADER_STATE:
      found_header = (
        (len(row) == 12) and
        (','.join(row[0:4]) == HEADER_FRAG) and
        (','.join(row[4:8]) == HEADER_FRAG) and
        (','.join(row[8:12]) == HEADER_FRAG)
      )
      if found_header:
        reader_state = WAITFOR_AGENT_COUNT_STATE
    elif reader_state == WAITFOR_AGENT_COUNT_STATE:
      initial_agent_count = int(row[1]) + int(row[5]) + int(row[9])
      reader_state = WAITFOR_REBELLION_START_STATE
    elif reader_state == WAITFOR_REBELLION_START_STATE:
      active_agent_count = int(row[9])
      if in_rebellion(active_agent_count, initial_agent_count):
        rebellion_start_tick = int(row[0])
        rebellion_agent_count = active_agent_count
        reader_state = WAITFOR_REBELLION_END_STATE
    elif reader_state == WAITFOR_REBELLION_END_STATE:
      active_agent_count = int(row[9])
      if not in_rebellion(active_agent_count, initial_agent_count):
        rebellion_end_tick = int(row[0])
        rebellion_length = rebellion_end_tick - rebellion_start_tick
        average_rebellion_size = float(rebellion_agent_count) / float(rebellion_length)
        filter_results.append(
          [rebellion_length, average_rebellion_size]
        )
        reader_state = WAITFOR_REBELLION_START_STATE
      else:
        rebellion_agent_count += active_agent_count
  csv.writer(sys.stdout, delimiter=',').writerows(filter_results)
  exit(0)

# vim: set ts=2 sw=2 expandtab:
