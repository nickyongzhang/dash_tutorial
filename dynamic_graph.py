# -*- encoding: utf-8 -*-
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas_datareader.data as web
import datetime

app = dash.Dash()

app.layout = html.Div(children=[
	html.Div(children='symbol to graph:'),

	dcc.Input(id='input', value='', type='text'),
	html.Div(id='output-graph')
	])

@app.callback(
	Output(component_id='output-graph',component_property='children'),
	[Input(component_id='input',component_property='value')]
	)
def update_value(input_data):
	start = datetime.datetime(2015,1,1)
	end = datetime.datetime(2018,2,8)
	df = web.DataReader(input_data,'morningstar',start,end)

	return dcc.Graph(
		id='example-graph',
        figure={
            'data': [
                {'x': df.index.get_level_values(1), 'y': df.Close, 'type': 'line', 'name': input_data},
            ],
            'layout': {
                'title': input_data
            }
        }
		)


if __name__ == '__main__':
	app.run_server(debug=True)


