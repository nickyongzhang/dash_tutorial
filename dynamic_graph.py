# -*- encoding: utf-8 -*-
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas_datareader.data as web
import datetime
import quandl

api_key = open('quandl_apikey.csv','r').read()

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
	end = datetime.datetime.now()
	#google finance is not working
	# df = web.DataReader(input_data,'google',start,end,authtoken=auth_tok)
	#use quandl as data source, but it needs an api_key
	stock = 'WIKI/'+input_data.upper()
	df = quandl.get(stock,api_key=api_key,start_date=start,end_date=end)

	return dcc.Graph(
		id='example-graph',
        figure={
            'data': [
                {'x': df.index, 'y': df.Close, 'type': 'line', 'name': input_data},
            ],
            'layout': {
                'title': input_data
            }
        }
		)


if __name__ == '__main__':
	app.run_server(debug=True)


