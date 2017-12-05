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

"""Classes for drawing animated progress bars."""

from __future__ import unicode_literals

import random

DEFAULT_TOTAL = 105  # Random total. The bigger, the more steps are calculated.
MIN_STEP_COUNT = 10  # Minimum number of steps used for random update.
PROGRESS_BAR_INNER_LENGTH = 73  # By default consoles are 80 characters wide.


class BaseProgressBar(object):
    """Class providing common code and behavior for progress bars."""

    def __init__(self, total=None):
        """Initialize the progress bar.

        :param int total: Number of total items to be processed.
        """
        self.total = float(DEFAULT_TOTAL if total is None else total)
        self.progress = 0
        self.percentage = 0

    @property
    def style(self):
        """Style used to indicate the progress."""
        raise NotImplementedError

    @property
    def is_incomplete(self):
        """Tells whether the progress bar hasn't yet reached 100%."""
        return self.progress != self.total

    def get_bar(self):
        """Returns the string for the progress bar at current progress.

        The string takes in account the length of the style used.

        :return: Returns the progress bar representation.
        :rtype: str
        """
        i = int(self.percentage * PROGRESS_BAR_INNER_LENGTH / len(self.style))
        int_percent = int(self.percentage * 100)
        return "[%s ] %d%%" % (self.style * i, int_percent)

    def random_update(self):
        """Generates a random increment and then updates the progress bar.

        :return: Returns the progress bar representation after updating.
        :rtype: str
        """
        max_step = int(min(self.total / MIN_STEP_COUNT,
                           self.total - self.progress))
        return self.update(random.randint(0, max_step))

    def update(self, count):
        """Update the progress bar based on the specified progress increase.

        The bar is only updated if progress is not yet completed.

        :param int count: Number of items to increment.
        :return: Returns the progress bar representation after updating.
        :rtype: str
        """
        if self.is_incomplete:
            self.progress += count
            self.percentage = self.progress / self.total
        return self.get_bar()


class EqualsProgressBar(BaseProgressBar):
    """Class rendering a progress bar using equals characters."""

    @property
    def style(self):
        """Style used to indicate the progress."""
        return "="


class SawtoothProgressBar(BaseProgressBar):
    """Class rendering a progress bar in a sawtooth-like fashion."""

    @property
    def style(self):
        """Style used to indicate the progress."""
        return "/\\"


class SquaresProgressBar(BaseProgressBar):
    """Class rendering a progress bar using square characters."""

    @property
    def style(self):
        """Style used to indicate the progress."""
        return "■"
