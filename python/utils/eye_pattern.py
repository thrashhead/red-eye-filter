#!/usr/bin/env python3

from typing import Tuple
import numpy as np
EyePattern = Tuple[str, str, str, str, str]

EYE_PATTERN_1: EyePattern = (
  "/---\\",
  "|   |",
  "|-o-|",
  "|   |",
  "\\---/"
)

EYE_PATTERN_2: EyePattern = (
  "/---\\",
  "| | |",
  "| 0 |",
  "| | |",
  "\\---/"
)

EYE_PATTERN_3: EyePattern = (
  "/---\\",
  "| | |",
  "|-q-|",
  "| | |",
  "\\---/"
)

EYE_PATTERN_4: EyePattern = (
  "/---\\",
  "|\\ /|",
  "| w |",
  "|/ \\|",
  "\\---/"
)

def flat(pattern):
  return "".join(pattern)

def straight(pattern):
  res = []
  for col in range(5):
    for row in range(5):
      res.append(pattern[row][col])

  return res

ALL_EYE_PATTERNS = [flat(EYE_PATTERN_4), flat(EYE_PATTERN_3), flat(EYE_PATTERN_2), flat(EYE_PATTERN_1)]

