import justpy as jp
import pandas
from charts.charts_types import chart_pie


def get_data():
    data = pandas.read_csv('reviews.csv', parse_dates=['Timestamp'])
    share = data.groupby(['Course Name'])['Rating'].count()
    return share


def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes='text-h3 text-center q-pa-md')
    p1 = jp.QDiv(a=wp, text="These graphs represents course review analysis", classes="text-h5 q-pl-md")
    hc = jp.HighCharts(a=wp, options=chart_pie)
    hc.options.title.text = "Average Rating by Month per Course"


    hc.options.xAxis.categories = list(get_data().index)
    hc_data = [{'name': v1, 'y': v2} for v1, v2 in zip(get_data().index, get_data())]

    hc.options.series[0]['data'] = hc_data

    return wp

jp.justpy(app)