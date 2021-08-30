import justpy as jp
import pandas
from charts.charts_types import chart_month_course_stream
from datetime import datetime
from pytz import utc

def get_data():
    data = pandas.read_csv('reviews.csv', parse_dates=['Timestamp'])
    data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
    month_average_crs = data.groupby(['Month','Course Name'])['Rating'].count().unstack()
    return month_average_crs


def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes='text-h3 text-center q-pa-md')
    p1 = jp.QDiv(a=wp, text="These graphs represents course review analysis", classes="text-h5 q-pl-md")
    hc = jp.HighCharts(a=wp, options=chart_month_course_stream)
    hc.options.title.text = "Average Rating by Month per Course"


    hc.options.xAxis.categories = list(get_data().index)
    hc_data = [{'name': v1, 'data': [v2 for v2 in get_data()[v1]]} for v1 in get_data().columns]

    hc.options.series = hc_data

    return wp

jp.justpy(app)