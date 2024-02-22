from django.test import TestCase
from .charts import Chart, generate_chart_id, get_colors, get_random_colors

class TestChart(TestCase):
    def test_generate_chart_id(self):
        # Test if generate_chart_id generates a string of length 8
        chart_id = generate_chart_id()
        self.assertEqual(len(chart_id), 8)

    def test_get_colors(self):
        # Test if get_colors returns a list of colors
        colors = get_colors()
        self.assertIsInstance(colors, list)
        self.assertTrue(colors)

    def test_get_random_colors(self):
        # Test if get_random_colors returns a list of random colors
        colors = get_random_colors(6)
        self.assertIsInstance(colors, list)
        self.assertEqual(len(colors), 6)

    def test_from_lists(self):
        # Test if from_lists generates datasets and labels correctly
        chart = Chart(chart_type='bar')
        values = [[1, 2, 3], [4, 5, 6]]
        labels = ['A', 'B', 'C']
        stacks = ['X', 'Y']
        chart.from_lists(values, labels, stacks)
        self.assertEqual(len(chart.datasets), 2)
        self.assertEqual(len(chart.labels), 3)

    def test_from_df(self):
        # Test if from_df generates datasets and labels correctly from DataFrame
        import pandas as pd
        chart = Chart(chart_type='bar')
        df = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6]
        })
        values = ['A', 'B']
        labels = ['X', 'Y', 'Z']
        stacks = None
        chart.from_df(df, values, labels, stacks)
        self.assertEqual(len(chart.datasets), 2)
        self.assertEqual(len(chart.labels), 3)

    def test_get_elements(self):
        # Test if get_elements returns correct elements for chart.js
        chart = Chart(chart_type='bar')
        chart.from_lists([[1, 2, 3]], ['A', 'B', 'C'], ['X'])
        elements = chart.get_elements()
        self.assertIn('data', elements)
        self.assertIn('type', elements)
        self.assertIn('options', elements)

    def test_get_html(self):
        # Test if get_html generates correct HTML code
        chart = Chart(chart_type='bar')
        chart_id = 'test_chart_id'
        chart.chart_id = chart_id
        html_code = chart.get_html()
        self.assertIn(f'<canvas id="{chart_id}"></canvas>', html_code)

    def test_get_js(self):
        # Test if get_js generates correct JavaScript code
        chart = Chart(chart_type='bar')
        chart_id = 'test_chart_id'
        chart.chart_id = chart_id
        js_code = chart.get_js()
        self.assertIn(f'var chartElement = document.getElementById(\'{chart_id}\').getContext(\'2d\');', js_code)
        self.assertIn(f'var {chart_id}Chart = new Chart(chartElement, {chart.get_elements()})', js_code)
