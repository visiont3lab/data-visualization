# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from pyngrok import ngrok
import webbrowser


# Design
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
colors = {
    'background': 'rgb(255,255,255)',
    'text': 'rgb(0,0,0)'
}

# Introduction
introduction_md = '''
## Introduzione
L'obbiettivo di questa dashboard é l'analisi dell'andamento del Corona Virus in italia.
Per crearla ci inspireremo alla [dashboard della protezione civile italiana](http://opendatadpc.maps.arcgis.com/apps/opsdashboard/index.html#/b0c68bce2cce478eaac82fe38d4138b1).
Quest'ultima utilizza il [seguente dataset pubblico](https://github.com/pcm-dpc/COVID-19/tree/master/dati-regioni).
La sottostante dashboard é realizzata usando la libreria [Dash plotly](https://dash-gallery.plotly.host/Portal/)
'''

description_md = '''
## Descrizione del dataset

L'obbiettivo di questa dashboard é l'analisi dell'andamento del Corona Virus in italia.
Per crearla ci inspireremo alla [dashboard della protezione civile italiana](http://opendatadpc.maps.arcgis.com/apps/opsdashboard/index.html#/b0c68bce2cce478eaac82fe38d4138b1).
Quest'ultima utilizza il [seguente dataset pubblico](https://github.com/pcm-dpc/COVID-19/tree/master/dati-regioni).
La sottostante dashboard é realizzata usando la libreria [Dash plotly](https://dash-gallery.plotly.host/Portal/)
'''

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, sharing=True)
app.config.update({
    #'url_base_pathname': '/showtemperature1/',
    # as the proxy server will remove the prefix
    'routes_pathname_prefix': '/', 

    # the front-end will prefix this string to the requests
    # that are made to the proxy server
    'requests_pathname_prefix': '/proxy/'
})

app.layout = html.Div(
    style={'backgroundColor': colors['background']},
    children=[

        html.H1(
            children='COVID-19 Analysiss',
            style={
                'textAlign': 'center',
                'color': colors['text']
                }
            ),
        
         html.Div(
            dcc.Markdown(
                children=introduction_md,
                style={
                    'color': colors['text']
                }
            )
        ),

        html.Div(
            children='Corona Virus Analisi',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }),

        dcc.Graph(
            id='example-graph',
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                ],
                'layout': {
                    'title': 'Dash Data Visualization',
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': {
                        'color': colors['text']
                    }
                }
            }
        )
])

if __name__ == '__main__':
    # debug true allows hot reloading
    app.run_server(debug=False,host='0.0.0.0', port=8050)

    
