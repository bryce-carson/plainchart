"""A text-based, zero-dependency, open-source charting utility."""


class PlainChart(object):
    """Chart objects which can be `render'ed for `print'ing."""

    def __init__(self, values, height: int = 10, style=None):
        """Create the matrix of characters according to style.

        When style is None the default of PlainChart.bar is used.

        The height parameter must be a positive integer
        """
        if not isinstance(height, int) or height <= 0:
            raise PlainChartException('height must be a postive integer.')

        self.values = values
        self.height = height
        self.max = max(values)

        columns = []  # For every column,
        for value in self.values:

            cells = []  # create the cells thereof.
            for y in range(1, self.height + 1):

                if style:
                    cell = style(self, value, y)

                else:
                    cell = PlainChart.bar(self, value, y)

                cells.append(cell)

            columns.append(cells)

        # transpose and flip
        self.rows = list(reversed(list(map(list, zip(*columns)))))

    def y(self, value):
        """Return y values scaled to rough proportions of the chart height."""
        _y = round(value * self.height / self.max) if self.max != 0 else 0
        return _y if _y <= self.height else self.height

    @staticmethod
    def bar(chart, value, y):
        """Style a y value to produce bar charts."""
        return '▌' if y <= chart.y(value) else ' '

    @staticmethod
    def scatter(chart, value, y):
        """Style a y value to produce scatter plots (charts)."""
        return '×' if y == chart.y(value) else ' '

    def render(self, new_line='\n'):
        """Linearize (stringify) the chart's character cell matrix."""
        return new_line.join([''.join(row) for row in self.rows])


class PlainChartException(Exception):
    """Simple exceptions for the PlainChart class."""

    def __init__(self, message):
        """Set the message for the exception."""
        self.message = message
