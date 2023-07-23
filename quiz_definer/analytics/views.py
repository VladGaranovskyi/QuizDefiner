from django.shortcuts import render
from .db_connect import get_analytics_dataframes
from .charts import Chart
from .apps import AppConfig

# setting palette
PALETTE = ['#465b65', '#184c9c', '#d33035', '#ffc107', '#28a745', '#6f7f8c', '#6610f2', '#6e9fa5', '#fd7e14', '#e83e8c',
           '#17a2b8', '#6f42c1']


def quiz_analytics(request, caption):

    # getting data frame
    df = get_analytics_dataframes(caption, 3)

    # creating chart instance
    chart = Chart("bar", chart_id="count_of_results", palette=PALETTE)

    # setting data through df
    chart.from_df(df, values="count", labels=["result"])

    return render(request, "quiz/quiz_analytics.html", {"js_code": chart.get_js(),
                                                        "html_code": chart.get_html()})
