# -*- coding: utf-8 -*-
#
# Copyright © 2017 Leandro Regueiro Iglesias.
#
# This code is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This code is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this code.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals

import curses
import locale
import time

from bars import EqualsProgressBar, SawtoothProgressBar, SquaresProgressBar


ITERATIONS = 7  # Iterations to run. If too big then all bars get to 100%.
SLEEP_TIME = 0.2  # Time to wait between steps. In seconds.


if __name__ == "__main__":
    progress_bars = [
        EqualsProgressBar(),
        SawtoothProgressBar(),
        SquaresProgressBar(),
    ]
    last_output = ""
    locale.setlocale(locale.LC_ALL, '')
    encoding = locale.getpreferredencoding()
    window = curses.initscr()
    curses.noecho()
    curses.cbreak()
    try:
        for i in range(ITERATIONS):
            strings = [progress_bars[j].random_update()
                       for j in range(len(progress_bars))]
            for j in range(len(progress_bars)):
                window.addstr(j, 0, strings[j].encode(encoding))
            window.refresh()
            last_output = "\n".join(strings)
            time.sleep(SLEEP_TIME)
    finally:
        curses.echo()
        curses.nocbreak()
        curses.endwin()
    print(last_output)
