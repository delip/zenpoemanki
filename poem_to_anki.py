import os
import sys

# This is the number of lines that will be in one study batch
LINES_PER_GROUP = 8

# This is the number of lines that will be shown to prompt the user to recite the next line
# Of course, if it's the beginning of the poem, fewer will be shown
PREVIOUS_LINES = 2
# This is the number of lines to show after the portion being tested so the user can see it
# in poetic context
AFTER_LINES = 2

# This is the minimum number of lines the user will be prompted to recite given
# a prompt of the previous PREVIOUS_LINES from the poem
MIN_LINES_TO_STUDY = 1

# This is the maximum number of lines the user will be prompted to recite given a prompt.
# A given group's studying will go from all MIN_LINES_TO_STUDY then go to the next value
# until it hits MAX_LINES_TO_STUDY
MAX_LINES_TO_STUDY = 2

# If True, the beginning of each group will include a card which tests the entire poem up
# to that point
CUMULATIVE_TEST = True

def read_poem(poem_file):
  with open(poem_file, 'r') as poem:
    return poem.read().split('\n')

def write_line(output, prompt=None, previous=None, tostudy=None, after=None, tags=None):
  prompt = prompt or ''
  previous = previous or []
  if tostudy is None:
    raise ValueError('value tostudy must be set')
  after = after or []
  tags = tags or []
  output.write('{prompt}\t{tostudy}\t{after}\t{tags}'.format(
    # Slightly janky, but this will give us a unique key for anki
    prompt='<br/>'.join(['({})'.format(prompt)] + previous),
    tostudy='<br/>'.join(tostudy),
    after='<br/>'.join(after),
    tags=' '.join(tags)))
  output.write('\n')

def main(poem_file):
  poem = read_poem(poem_file)
  with open(os.path.basename(poem_file) + '.anki', 'w') as output:
    if CUMULATIVE_TEST:
      # This generates the cumulative test which begins every new group
      cumulative_test_end = LINES_PER_GROUP
      place_test_in_group = 2
      while cumulative_test_end-LINES_PER_GROUP < len(poem):
        if cumulative_test_end > len(poem):
          prompt = 'Please recite the entire poem'
        else:
          prompt = 'Please recite the first {} lines of the poem'.format(cumulative_test_end)
        write_line(output,
          prompt=prompt,
          tostudy=poem[:cumulative_test_end],
          tags=['group{}'.format(place_test_in_group)])
        cumulative_test_end += LINES_PER_GROUP
        place_test_in_group += 1

    for LINES_TO_STUDY in range(MIN_LINES_TO_STUDY, MAX_LINES_TO_STUDY+1):
      for i in range(0, len(poem)-LINES_TO_STUDY+1):
        current_group = (i / LINES_PER_GROUP) + 1
        prev_index = max(0, i - PREVIOUS_LINES)
        if i == 0 and LINES_TO_STUDY == 1:
          prompt = 'Please recite the first line of the poem'
        elif i == 0:
          prompt = 'Please recite the first {} lines of the poem'.format(LINES_TO_STUDY)
        elif LINES_TO_STUDY == 1:
          prompt = 'Please recite the next line of the poem'
        else:
          prompt = 'Please recite the next {} lines of the poem'.format(LINES_TO_STUDY)
        write_line(output,
          prompt=prompt,
          previous=poem[prev_index:i] or ['(Beginning of poem)'],
          tostudy=poem[i:i+LINES_TO_STUDY],
          after=poem[i+LINES_TO_STUDY:i+LINES_TO_STUDY+AFTER_LINES],
          tags=['group{}'.format(current_group)])

if __name__ == '__main__':
  main(sys.argv[1]) # the poem file