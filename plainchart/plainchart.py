"""A text-based, zero-dependency, open-source charting utility.

The plainchart module contains PlainChart, a simple class which makes
approximate plots of uni-dimensional data. The initialization function receives
this data as the parameter "values". The "height" of a chart is what makes it
approximate. All values are clamped (truncated) to the maximum height if they
go beyond it, but otherwise values are scaled through rounding and
multiplication to an approximation of their magnitude in the number of
characters cells that will be displayed.

The simplest example usage of the library is as follows:
```python
import plainchart


print(plainchart.PlainChart([1,2,3]).render())
```

This example, when plotted, will show the three values in a bar plot like so:

  ▌
  ▌
  ▌
 ▌▌
 ▌▌
 ▌▌
 ▌▌
▌▌▌
▌▌▌
▌▌▌

The values—one, two, and three—are scaled to approximately three characters in
height because the default for that parameter is ten (height = 10). To make
adjustments to the scaling, users should use a more appropriate height argument
than the default to reduce visual bias. However, the library is incredibly
simple, and shouldn't be relied upon for qualitative data analysis. It is only
suitable as an amusement or for a quick view of a simple linear trend.

"""


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
