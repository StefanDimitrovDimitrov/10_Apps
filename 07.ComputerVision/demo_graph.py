import pandas
from bokeh.plotting import figure
from bokeh.io import output_file, show
"""
p=figure(plot_width=500,plot_height=400, tools='pan',logo=None)
 
p.title.text="Cool Data"
p.title.text_color="Gray"
p.title.text_font="times"
p.title.text_font_style="bold"
p.xaxis.minor_tick_line_color=None
p.yaxis.minor_tick_line_color=None
p.xaxis.axis_label="Date"
p.yaxis.axis_label="Intensity"    
 
p.line([1,2,3],[4,5,6])
output_file("graph.html")
show(p)

p = figure(plot_width=500, plot_height=400, tools = 'pan, reset')
p.title.text = "Earthquakes"
p.title.text_color = "Orange"
p.title.text_font = "times"
p.title.text_font_style = "italic"
p.yaxis.minor_tick_line_color = "Yellow"
p.xaxis.axis_label = "Times"
p.yaxis.axis_label = "Value"
p.circle([1,2,3,4,5], [5,6,5,5,3], size = [i*2 for i in [8,12,14,15,20]], color="red", alpha=0.5)
output_file("Scatter_plotting.html")

"""
def basic_graph():
    x = [1, 2, 3, 4, 5]
    y = [6, 7, 8, 9, 10]

    output_file("Line.html")

    f = figure()

    # f.line(x, y)
    # f.triangle(x, y)
    f.circle(x, y)

    show(f)

def read_from_csv():

    df = pandas.read_csv('data.csv')
    x = df["x"]
    y = df["y"]

    output_file("Line_from_csv.html")

    f=figure()
    f.circle(x,y)
    show(f)

# read_from_csv()

def women_education():

    df = pandas.read_csv('data_year.csv')
    print(df)

women_education()


def excel_reading():
    df = pandas.read_excel("http://pythonhow.com/data/verlegenhuken.xlsx", sheet_name=0)
    df["Temperature"] = df["Temperature"] / 10
    df["Pressure"] = df["Pressure"] / 10

    p = figure(plot_width=500, plot_height=400, tools='pan')

    p.title.text = "Temperature and Air Pressure"
    p.title.text_color = "Gray"
    p.title.text_font = "arial"
    p.title.text_font_style = "bold"
    p.xaxis.minor_tick_line_color = None
    p.yaxis.minor_tick_line_color = None
    p.xaxis.axis_label = "Temperature (°C)"
    p.yaxis.axis_label = "Pressure (hPa)"

    p.circle(df["Temperature"], df["Pressure"], size=0.5)
    output_file("Weather.html")
    show(p)