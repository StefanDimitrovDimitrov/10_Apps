import justpy as jp


def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Cource Reviews",classes='text-h3 text-center q-pa-md')
    p1 = jp.QDiv(a=wp, text="These graphs represents course review analysis")

    return wp


jp.justpy(app)
