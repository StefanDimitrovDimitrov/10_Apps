import justpy as jp
import pandas

from charts.charts_types import chart_days


def get_data():
    data = pandas.read_csv('reviews.csv', parse_dates=['Timestamp'])
    data['Day'] = data['Timestamp'].dt.date
    day_average = data.groupby(['Day']).mean()
    return day_average


def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes='text-h3 text-center q-pa-md')
    p1 = jp.QDiv(a=wp, text="These graphs represents course review analysis", classes="text-h5 q-pl-md")
    hc = jp.HighCharts(a=wp, options=chart_days)
    hc.options.title.text = "Average Rating by Day"

    hc.options.xAxis.categories = list(get_data().index)
    hc.options.series[0].data = list(get_data()['Rating'])
    print(get_data())

    return wp


jp.justpy(app)
