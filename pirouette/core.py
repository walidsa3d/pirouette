#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
import sys
import time
import os
import itertools
from termcolor import colored
import sys

frames = {
    'tetris': ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'],
    'stick': ['-', '/', '\\'],
    #'pointer': ['>', '>>', '>>>'],
    'circle': ['.', 'o', 'O', '°', 'O', 'o', '.'],
    'hourglass': ['⏳', '⌛'],
    'moon': ['◐', '◓', '◑', '◒'],
    'stack': ['▁', '▃', '▄', '▅', '▆', '▇', '█', '▇', '▆', '▅', '▄', '▃', '▁'],
    'clock': ['🕛', '🕐', '🕑', '🕒', '🕓', '🕔', '🕕', '🕖', '🕗', '🕘', '🕙', '🕚'],
    'box': ['■', '□', '▪', '▫'],
    'arrow': ['←', '↖', '↑', '↗', '→', '↘', '↓', '↙'],
    #'dot': ['.', '..', '...', '....'],
    'bullet': ['◎ ◎ ◎', '◉ ◎ ◎', '◉ ◉ ◎', '◉ ◉ ◉']
}


class Spinner:

    def __init__(self):
        pass

    def cursor_on(self):
        '''turn the cursor on'''
        os.system('setterm -cursor on')

    def cursor_off(self):
        '''turn the cursor off'''
        os.system('setterm -cursor off')

    def spin(self, duration=5, color='cyan', shape='tetris'):
        shape = frames[shape]
        frame_gen = itertools.cycle(shape)
        self.cursor_off()
        try:
            for _ in xrange(duration*10):
                frame = next(frame_gen)
                frame = colored(frame, color)
                l = len(frame)
                sys.stdout.write(frame)
                sys.stdout.flush()
                time.sleep(0.1)
                sys.stdout.write('\b'*l)
        except KeyboardInterrupt:
            self.cursor_on()
            sys.exit(0)
        self.cursor_on()
