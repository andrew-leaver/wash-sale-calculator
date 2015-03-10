# Copyright Google

# BSD License

import copy
import wash

# from http://stackoverflow.com/questions/8924173/how-do-i-print-bold-text-in-python
class color:
  PURPLE = '\033[95m'
  CYAN = '\033[96m'
  DARKCYAN = '\033[36m'
  BLUE = '\033[94m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
  END = '\033[0m'

def print_progress(lots, text, bold_lots):
  lots = copy.copy(lots)  # so I can re-sort non-destructively
  print text
  lots.sort(cmp=wash.cmp_by_buy_date)
  bold_ids = [id(lot) for lot in bold_lots]
  for lot in lots:
    header = ''
    footer = ''
    if id(lot) in bold_ids:
      header = color.BOLD
      footer = color.END
    print header + str(lot) + footer
  raw_input('hit enter>')
    