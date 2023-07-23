import pandas as pd
from dataclasses import dataclass, field
from palettable.lightbartlein.diverging import BlueOrangeRed_10 as palette
import random
import numpy as np
import string


# options for chart.js
def get_options():
    return {
                'xAxes': [
                    {'stacked': 'true'}
                ],
                'yAxes': [
                    {'stacked': 'true'}
                ]
           }


# if id is not set
def generate_chart_id():
    return ''.join(random.choice(string.ascii_letters) for i in range(8))


# if palette is not set
def get_colors():
    try:
        return palette.hex_colors
    except:
        return get_random_colors(6)


def get_random_colors(num, colors=[]):
    while len(colors) < num:
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))

        if color not in colors:
            colors.append(color)

    return colors


@dataclass
class Chart:
    # chart type in chart.js
    chart_type: str
    # data from df
    datasets: list = field(default_factory=list)
    # labels from df
    labels: list = field(default_factory=list)
    # id in html and js
    chart_id: str = field(default_factory=generate_chart_id)
    # colors
    palette: list = field(default_factory=get_colors)
    # options for chart.js
    options: dict = field(default_factory=get_options)

    def from_lists(self, values, labels, stacks):

        # initializing datasets
        self.datasets = []

        # adding colors if colors in palette are not enough for values
        if len(self.palette) < len(values):
            get_random_colors(num=len(values), colors=self.palette)

        # converting data for chart.js
        for i in range(len(stacks)):
            self.datasets.append(
                {
                    'label': stacks[i],
                    'backgroundColor': self.palette[i],
                    'data': values[i],
                }
            )

        if len(values) == 1:
            self.datasets[0]['backgroundColor'] = self.palette

        self.labels = labels

    def from_df(self, df, values, labels, stacks=None, aggfunc=np.sum, round_values=0):

        # making pivot table
        pivot = pd.pivot_table(
            df,
            values=values,
            index=stacks,
            columns=labels,
            aggfunc=aggfunc,
            fill_value=0
        )

        # round
        pivot = pivot.round(round_values)

        # setting vars to send them to another method
        values = pivot.values.tolist()
        labels = pivot.columns.tolist()
        stacks = pivot.index.tolist()

        self.from_lists(values, labels, stacks)

    def get_elements(self):

        # setting elements for chart.js, there is a possibility to add another elements
        elements = {
            'data': {
                'labels': self.labels,
                'datasets': self.datasets
            },
            'type': "bar",
            'options': self.options
        }

        return elements

    def get_html(self):
        code = f'<canvas id="{self.chart_id}"></canvas>'
        return code

    def get_js(self):
        code = f"""
            var chartElement = document.getElementById('{self.chart_id}').getContext('2d');
            var {self.chart_id}Chart = new Chart(chartElement, {self.get_elements()})
        """
        return code
