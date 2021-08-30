import justpy as jp
import pandas
from charts.charts_types import chart_month
from datetime import datetime
from pytz import utc

def get_data():
    data = pandas.read_csv('reviews.csv', parse_dates=['Timestamp'])
    data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
    month_average = data.groupby(['Month']).mean()
    return month_average


def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes='text-h3 text-center q-pa-md')
    p1 = jp.QDiv(a=wp, text="These graphs represents course review analysis", classes="text-h5 q-pl-md")
    hc = jp.HighCharts(a=wp, options=chart_month)
    hc.options.title.text = "Average Rating by Month"

    hc.options.xAxis.categories = list(get_data().index)
    hc.options.series[0].data = list(get_data()['Rating'])

    return wp

jp.justpy(app)