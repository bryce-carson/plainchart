"""Additional style functions for PlainChart."""
import statistics


def mean_html(chart, value, y):
    """Style a y value to produce a bar chart in an HTML document."""
    mean = statistics.mean(chart.values)
    mean_y = chart.y(mean)
    value_y = chart.y(value)

    if value_y <= mean_y and y <= value_y:
        return '<span style="color:green">▌</span>'

    elif y <= mean_y:
        return '<span style="color:green">▌</span>'

    elif y <= value_y:
        return '<span style="color:red">▌</span>'

    return '<span style="color:white">▌</span>'
