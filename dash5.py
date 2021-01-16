## Plotly Dash Tutorial ## set zoom 80%
# -*- coding: utf-8 -*-
import dash
from dash.dependencies import  Event
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas_datareader import data as web

import base64
import random
import StringIO
from cassandra.cluster import Cluster
import datetime
import csv

from collections import deque

app_colors = {
    'background': '#DCDCDC',
    'text': '#000000',
    'sentiment-plot':'#41EAD4',
    'volume-bar':'#FBFC74',
    'someothercolor':'#FF206E',
}

app = dash.Dash()

image_filename = 'bg.jpg' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())
image_filename1 = 'Picture3.png' # replace with your own image
encoded_image1 = base64.b64encode(open(image_filename1, 'rb').read())

all_options = {
    'Machine1': [ 'Temperature1',u'Pressure1','Humidity1','Performance1','PartCount1','Toollife1'],
    'Machine2': ['Temperature2',u'Pressure2','Humidity2','Performance2','PartCount2','Toollife2' ]
    
 }

app.title = 'Dashboard'

# Boostrap CSS.
app.css.append_css({'external_url': 'https://codepen.io/amyoshino/pen/jzXypZ.css'})

app.layout = html.Div(
    html.Div([
        html.Div([            
            html.Img(
                src='data:image/png;base64,{}'.format(encoded_image),
                className='three columns',
                style={
                    'height': '100%',
                    'width': '100%',
                    'float': 'left',
                    'position': 'relative',
                    'margin-top': '-10',
                    'margin-left':'-10',
                  
                     
                },
            ),
            
        ], className = "twelve columns"
                 ),

        html.Div([
            html.H1(children='Auring Technologies',
                    className = "nine columns",style={'margin-top': -1100,'margin-left':400,'margin-right':'auto','position': 'relative','color': app_colors['background']}),
            html.Img(
                src='data:image/png;base64,{}'.format(encoded_image1),
                className='three columns',
                style={
                    'height': '10%',
                    'width': '10%',
                    'float': 'left',
                    'position': 'relative',
                    'margin-top': -1100,
                    'margin-right': 10
                },
            ),
            
        ], className = "banner"
                 ),

        html.Div(
            [
                html.Div(
                    [
                        html.P('Choose Machine:'),
                        dcc.RadioItems(
                                id = 'Machine',
                                options=[{'label': k, 'value': k} for k in all_options.keys()],
                                value='Machine1',
                                labelStyle={'display': 'inline-block'}
                        ),
                    ],
                    className='four columns',
                    style={'margin-left':'10','margin-top': '-1000','position': 'relative','color': app_colors['text']}
                ),
                html.Div(
                    [   html.P('Choose Parameter:'),
                        dcc.Dropdown(
                                id = 'Parameters',
                                value='',
                                multi=True
                                
                        
                        ),
                    ],
                    className='five columns',
                    style={'margin-left':'400','margin-top': '-1000','position': 'relative','color': app_colors['text']}
                )
            ], className="banner"
        ),

       
html.Div([
            html.Div([
            dcc.Graph(
                id='example-graph-4', animate= False
            ),dcc.Interval(
            id='example-graph-4-update',
            interval=5*1000),
            
        ],style={'padding': '2px 2px 2px 2px',"border": "thin black solid",'margin-top':'-800',"border": "thin grey solid",
          'marginLeft': '620px', 'marginRight': 'auto', "width": "600px"
            }
       )
      ],className = 'four columns'
    ),
      

       html.Div([
            html.Div([
                dcc.Graph(
                 id='example-graph', animate= False
                ),
               dcc.Interval(
               id='example-graph-update',
               interval=5*1000),
            ],style={'padding': '2px 2px 2px 2px','margin-top':'-800',
          'marginLeft': '2px', 'marginRight': 'auto', "width": "600px","border": "thin grey solid"
          }
       )
     ], className = 'four columns'
      ),

        html.Div([
            html.Div([
            dcc.Graph(
                id='example-graph-2', animate= False
            ),
            dcc.Interval(
            id='example-graph-2-update',
            interval=5*1000),
        ],style={'padding': '2px 2px 2px 2px',"border": "thin black solid",
          'marginLeft': '2px', 'marginRight': 'auto', "width": "600px", 'margin-top':'-530',"border": "thin grey solid"
          }
       )
     ], className = 'four columns'
      ),
         html.Div([
            html.Div([
            dcc.Graph(
                id='example-graph-3', animate= False
            ),
            dcc.Interval(
            id='example-graph-3-update',
            interval=5*1000),
        ],style={'padding': '2px 2px 2px 2px',"border": "thin black solid",'margin-top':'-260',
          'marginLeft': '2px', 'marginRight': 'auto', "width": "600px"
            }
       )
      ],className = 'four columns'
    ),
         html.Div([
            html.Div([
            dcc.Graph(
                id='example-graph-5', animate= False
            ),
            dcc.Interval(
            id='example-graph-5-update',
            interval=5*1000),
        ],style={'padding': '2px 2px 2px 2px',"border": "thin black solid",'margin-top':'-530',
          'marginLeft': '620px', 'marginRight': 'auto', "width": "600px","border": "thin grey solid"
            }
       )
      ],className = 'four columns'
    ),
         html.Div([
            html.Div([
            dcc.Graph(
                id='example-graph-6', animate= False
            ),
            dcc.Interval(
            id='example-graph-6-update',
            interval=5*1000),
        ],style={'padding': '2px 2px 2px 2px',"border": "thin black solid",'margin-top':'-260',
          'marginLeft': '620px', 'marginRight': 'auto', "width": "600px","border": "thin grey solid"
            }
       )
      ],className = 'four columns'
    ),

        
    
    ], 
  )
)

@app.callback(
    dash.dependencies.Output('Parameters','options'),
        [dash.dependencies.Input('Machine','value')]
)
def set_Parameters_options(selected_Machine):    

     return [{'label': i, 'value': i} for i in all_options[selected_Machine]]

@app.callback(
    dash.dependencies.Output('example-graph', 'figure'),
     
    [dash.dependencies.Input('Parameters', 'value')],
    events=[Event('example-graph-update', 'interval')] )
def update_graph_src(selector):
    cluster= Cluster()
    keyspace= 'temperaturekey'
    connection = cluster.connect(keyspace)
    with open ('mytemp1.csv','w') as f:
         thewriter=csv.writer(f)
         first_order = connection.execute('SELECT * FROM temperaturetable1 WHERE machine=1')
         for order in  first_order:
          thewriter.writerow([order.date1.strftime("%M:%S") , order.temperature, order.humidity, order.pressure, order.machine, order.performance,order.part,order.toollife])
    df1 = pd.read_csv('mytemp1.csv')
    df1=df1.tail()
    with open ('mytemp2.csv','w') as f:
         thewriter=csv.writer(f)
         first_order = connection.execute('SELECT * FROM temperaturetable1 WHERE machine=2')
         for order in  first_order:
          thewriter.writerow([order.date1.strftime("%M:%S") , order.temperature, order.humidity, order.pressure, order.machine, order.performance,order.part,order.toollife])
    df2 = pd.read_csv('mytemp2.csv')
    df2=df2.tail()
    
     

    Param = {
        
         
        'Temperature1': {'x': df1.iloc[:,0], 'y': df1.iloc[:,1]},
        'Pressure1': {'x': 0, 'y': 0},
        'Humidity1': {'x': 0, 'y': 0},
        'Performance1': {'x': 0, 'y': 0},
        'PartCount1': {'x': 0, 'y': 0},
        'Toollife1': {'x': 0, 'y': 0},
         
        'Temperature2': {'x': df2.iloc[:,0], 'y': df2.iloc[:,1]},
        'Pressure2': {'x': 0, 'y': 0},
        'Humidity2': {'x': 0, 'y': 0},
        'Performance2': {'x': 0, 'y': 0},
        'PartCount2': {'x': 0, 'y': 0},
        'Toollife2': {'x': 0, 'y': 0}
        
    }

    data = []
    for city in selector:
        data.append({'x': Param[city]['x'], 'y': Param[city]['y'],
                    'type': 'line', 'name': city})
    figure = {
        'data': data,
        'layout': {
            'height':250,
            'title': 'Temperature',
            'xaxis' : dict(
                title='Time',
                titlefont=dict(
                family='Courier New, monospace',
                size=20,
                color='#7f7f7f'
            )),
            'yaxis' : dict(
                title='y Axis',
                titlefont=dict(
                family='Helvetica, monospace',
                size=20,
                color='#7f7f7f'
            ))
        }
    }
    return figure

@app.callback(
    dash.dependencies.Output('example-graph-2', 'figure' ),
   
    [dash.dependencies.Input('Parameters', 'value')],
 events=[Event('example-graph-2-update', 'interval')])
def update_graph_src(selector):
    cluster= Cluster()
    keyspace= 'temperaturekey'
    connection = cluster.connect(keyspace)
    with open ('mytemp1.csv','w') as f:
         thewriter=csv.writer(f)
         first_order = connection.execute('SELECT * FROM temperaturetable1 WHERE machine=1')
         for order in  first_order:
          thewriter.writerow([order.date1.strftime("%M:%S") , order.temperature, order.humidity, order.pressure, order.machine, order.performance,order.part,order.toollife])
    df1 = pd.read_csv('mytemp1.csv')
    df1=df1.tail()
    with open ('mytemp2.csv','w') as f:
         thewriter=csv.writer(f)
         first_order = connection.execute('SELECT * FROM temperaturetable1 WHERE machine=2')
         for order in  first_order:
          thewriter.writerow([order.date1.strftime("%M:%S") , order.temperature, order.humidity, order.pressure, order.machine, order.performance,order.part,order.toollife])
    df2 = pd.read_csv('mytemp2.csv')
    df2=df2.tail()
    Param = {

        'Temperature1': {'x': 0, 'y': 0},
        'Pressure1': {'x': df1.iloc[:,0], 'y': df1.iloc[:,2]},
        'Humidity1': {'x': 0, 'y': 0},
        'Performance1': {'x': 0, 'y': 0},
        'PartCount1': {'x': 0, 'y': 0},
        'Toollife1': {'x': 0, 'y': 0},
         
        'Temperature2': {'x': 0, 'y': 0},
        'Pressure2': {'x': df2.iloc[:,0], 'y': df2.iloc[:,2]},
        'Humidity2': {'x': 0, 'y': 0},
        'Performance2': {'x': 0, 'y': 0},
        'PartCount2': {'x': 0, 'y': 0},
        'Toollife2': {'x': 0, 'y': 0}
        
    }

    data = []
    for city in selector:
        data.append({'x': Param[city]['x'], 'y': Param[city]['y'],
                    'type': 'bar', 'name': city})
    figure = {
        'data': data,
        'layout': {
            'height': 250,
            'margin-left':'2px',
            'title': 'Pressure',
            'xaxis' : dict(
                title='Time',
                titlefont=dict(
                family='Courier New, monospace',
                size=20,
                color='#7f7f7f'
            )),
            'yaxis' : dict(
                title='y Axis',
                titlefont=dict(
                family='Helvetica, monospace',
                size=20,
                color='#7f7f7f'
            ))
        }
    }
    return figure

@app.callback(
    dash.dependencies.Output('example-graph-3', 'figure' ),
   
    [dash.dependencies.Input('Parameters', 'value')],
    events=[Event('example-graph-3-update', 'interval')])
def update_graph_src(selector):
    cluster= Cluster()
    keyspace= 'temperaturekey'
    connection = cluster.connect(keyspace)
    with open ('mytemp1.csv','w') as f:
         thewriter=csv.writer(f)
         first_order = connection.execute('SELECT * FROM temperaturetable1 WHERE machine=1 ')
         for order in  first_order:
          thewriter.writerow([order.date1.strftime("%M:%S") , order.temperature, order.humidity, order.pressure, order.machine, order.performance,order.part,order.toollife])
    df1 = pd.read_csv('mytemp1.csv')
    df1=df1.tail()
    with open ('mytemp2.csv','w') as f:
         thewriter=csv.writer(f)
         first_order = connection.execute('SELECT * FROM temperaturetable1 WHERE machine=2 ')
         for order in  first_order:
          thewriter.writerow([order.date1.strftime("%M:%S") , order.temperature, order.humidity, order.pressure, order.machine, order.performance,order.part,order.toollife])
    df2 = pd.read_csv('mytemp2.csv')
    df2=df2.tail()
    
    Param = {
        
        'Temperature1': {'x': 0, 'y': 0},
        'Pressure1': {'x': 0, 'y': 0},
        'Humidity1': {'x': df1.iloc[:,0], 'y': df1.iloc[:,3]},
        'Performance1': {'x': 0, 'y': 0},
        'PartCount1': {'x': 0, 'y': 0},
        'Toollife1': {'x': 0, 'y': 0},
         
        'Temperature2': {'x': 0, 'y': 0},
        'Pressure2': {'x':0, 'y':0},
        'Humidity2': {'x': df2.iloc[:,0], 'y': df2.iloc[:,3]},
        'Performance2': {'x': 0, 'y': 0},
        'PartCount2': {'x': 0, 'y': 0},
        'Toollife2': {'x': 0, 'y': 0}
    }

    data = []
    for city in selector:
        data.append({'x': Param[city]['x'], 'y': Param[city]['y'],
                    'type': 'line', 'name': city})
    figure = {
        'data': data,
        'layout': {
            'height': 250,
            'margin-left':'2px',
            'title': 'Humidity',
            'xaxis' : dict(
                title='Time',
                titlefont=dict(
                family='Courier New, monospace',
                size=20,
                color='#7f7f7f'
            )),
            'yaxis' : dict(
                title='y Axis',
                titlefont=dict(
                family='Helvetica, monospace',
                size=20,
                color='#7f7f7f'
            ))
        }
    }
    return figure

@app.callback(
    dash.dependencies.Output('example-graph-4', 'figure' ),
   
    [dash.dependencies.Input('Parameters', 'value')],
    events=[Event('example-graph-4-update', 'interval')])

def update_graph_src(selector):
    cluster= Cluster()
    keyspace= 'temperaturekey'
    connection = cluster.connect(keyspace)
    with open ('mytemp1.csv','w') as f:
         thewriter=csv.writer(f)
         first_order = connection.execute('SELECT * FROM temperaturetable1 WHERE machine=1 ')
         for order in  first_order:
          thewriter.writerow([order.date1.strftime("%M:%S") , order.temperature, order.humidity, order.pressure, order.machine, order.performance,order.part,order.toollife])
    df1 = pd.read_csv('mytemp1.csv')
    df1=df1.tail()
    with open ('mytemp2.csv','w') as f:
         thewriter=csv.writer(f)
         first_order = connection.execute('SELECT * FROM temperaturetable1 WHERE machine=2 ')
         for order in  first_order:
          thewriter.writerow([order.date1.strftime("%M:%S") , order.temperature, order.humidity, order.pressure, order.machine, order.performance,order.part,order.toollife])
    df2 = pd.read_csv('mytemp2.csv')
    df2=df2.tail()
    Param = {
                 
        'Temperature1': {'x': 0, 'y': 0},
        'Pressure1': {'x': 0, 'y': 0},
        'Humidity1': {'x': 0, 'y': 0},
        'Performance1': {'x': df1.iloc[:,0], 'y': df1.iloc[:,5]},
        'PartCount1': {'x': 0, 'y': 0},
        'Toollife1': {'x': 0, 'y': 0},
         
        'Temperature2': {'x': 0, 'y': 0},
        'Pressure2': {'x':0, 'y':0},
        'Humidity2': {'x': 0, 'y': 0},
        'Performance2': {'x': df2.iloc[:,0], 'y': df2.iloc[:,5]},
        'PartCount2': {'x': 0, 'y': 0},
        'Toollife2': {'x': 0, 'y': 0}
    }
     
    data = []
    for city in selector:
        data.append({'x': Param[city]['x'], 'y': Param[city]['y'],
                     'name': city})
    figure = {
        'data': data,
        'mode': 'markers',
        'marker': {'size': 12},
        'layout': {            
            'height': 250,
            'margin-left':'2px',
            'title': 'Performance over Time',
            'xaxis' : dict(
                title='Time',
                titlefont=dict(
                family='Courier New, monospace',
                size=20,
                color='#7f7f7f'

            )),
            'yaxis' : dict(
                title='Performance %',
                titlefont=dict(
                family='Helvetica, monospace',
                size=20,
                color='#7f7f7f'
            ))
        }
    }
    return figure

@app.callback(
    dash.dependencies.Output('example-graph-5', 'figure' ),
   
    [dash.dependencies.Input('Parameters', 'value')],
    events=[Event('example-graph-5-update', 'interval')])

def update_graph_src(selector):
    cluster= Cluster()
    keyspace= 'temperaturekey'
    connection = cluster.connect(keyspace)
    with open ('mytemp1.csv','w') as f:
         thewriter=csv.writer(f)
         first_order = connection.execute('SELECT * FROM temperaturetable1 WHERE machine=1')
         for order in  first_order:
          thewriter.writerow([order.date1.strftime("%M:%S") , order.temperature, order.humidity, order.pressure, order.machine,   order.performance,order.part,order.toollife])
    df1 = pd.read_csv('mytemp1.csv')
    df1=df1.tail()
    with open ('mytemp2.csv','w') as f:
         thewriter=csv.writer(f)
         first_order = connection.execute('SELECT * FROM temperaturetable1 WHERE machine=2 ')
         for order in  first_order:
          thewriter.writerow([order.date1.strftime("%M:%S") , order.temperature, order.humidity, order.pressure, order.machine, order.performance,order.part,order.toollife])
    df2 = pd.read_csv('mytemp2.csv')
    df2=df2.tail()
    Param = {
                 
        'Temperature1': {'x': 0, 'y': 0},
        'Pressure1': {'x': 0, 'y': 0},
        'Humidity1': {'x': 0, 'y': 0},
        'Performance1': {'x': 0, 'y': 0},
        'PartCount1': {'x': df1.iloc[:,0], 'y': df1.iloc[:,6]},
        'Toollife1': {'x': 0, 'y': 0},   
         
        'Temperature2': {'x': 0, 'y': 0},
        'Pressure2': {'x':0, 'y':0},
        'Humidity2': {'x': 0, 'y': 0},
        'Performance2': {'x': 0, 'y': 0},
        'PartCount2': {'x': df2.iloc[:,0], 'y': df2.iloc[:,6]},
        'Toollife2': {'x': 0, 'y': 0},
    }
     
    data = []
    for city in selector:
        data.append({'x': Param[city]['x'], 'y': Param[city]['y'],
                     'name': city})
    figure = {
        'data': data,
        'mode': 'markers',
        'marker': {'size': 12},
        'layout': {            
            'height': 250,
            'margin-left':'2px',
            'title': 'Part Count over Time',
            'xaxis' : dict(
                title='Time',
                titlefont=dict(
                family='Courier New, monospace',
                size=20,
                color='#7f7f7f'

            )),
            'yaxis' : dict(
                title='Part Count',
                titlefont=dict(
                family='Helvetica, monospace',
                size=20,
                color='#7f7f7f'
            ))
        }
    }
    return figure

@app.callback(
    dash.dependencies.Output('example-graph-6', 'figure' ),
   
    [dash.dependencies.Input('Parameters', 'value')],
    events=[Event('example-graph-6-update', 'interval')])

def update_graph_src(selector):
    cluster= Cluster()
    keyspace= 'temperaturekey'
    connection = cluster.connect(keyspace)
    with open ('mytemp1.csv','w') as f:
         thewriter=csv.writer(f)
         first_order = connection.execute('SELECT * FROM temperaturetable1 WHERE machine=1')
         for order in  first_order:
          thewriter.writerow([order.date1.strftime("%M:%S") , order.temperature, order.humidity, order.pressure, order.machine,   order.performance,order.part,order.toollife])
    df1 = pd.read_csv('mytemp1.csv')
    df1=df1.tail()
    with open ('mytemp2.csv','w') as f:
         thewriter=csv.writer(f)
         first_order = connection.execute('SELECT * FROM temperaturetable1 WHERE machine=2')
         for order in  first_order:
          thewriter.writerow([order.date1.strftime("%M:%S") , order.temperature, order.humidity, order.pressure, order.machine, order.performance,order.part,order.toollife])
    df2 = pd.read_csv('mytemp2.csv')
    df2=df2.tail()
    Param = {
                 
        'Temperature1': {'x': 0, 'y': 0},
        'Pressure1': {'x': 0, 'y': 0},
        'Humidity1': {'x': 0, 'y': 0},
        'Performance1': {'x': 0, 'y': 0},
        'PartCount1': {'x': 0, 'y': 0},
        'Toollife1': {'x': df1.iloc[:,0], 'y': df1.iloc[:,7]},   
         
        'Temperature2': {'x': 0, 'y': 0},
        'Pressure2': {'x':0, 'y':0},
        'Humidity2': {'x': 0, 'y': 0},
        'Performance2': {'x': 0, 'y': 0},
        'PartCount2': {'x': 0, 'y': 0},
        'Toollife2': {'x': df2.iloc[:,0], 'y': df2.iloc[:,7]}
    }
     
    data = []
    for city in selector:
        data.append({'x': Param[city]['x'], 'y': Param[city]['y'],
                     'name': city})
    figure = {
        'data': data,
        'mode': 'markers',
        'marker': {'size': 12},
        'layout': {            
            'height': 250,
            'margin-left':'2px',
            'title': 'Tool Life vs Time',
            'xaxis' : dict(
                title='Time',
                titlefont=dict(
                family='Courier New, monospace',
                size=20,
                color='#7f7f7f'

            )),
            'yaxis' : dict(
                title='Tool Life',
                titlefont=dict(
                family='Helvetica, monospace',
                size=20,
                color='#7f7f7f'
            ))
        }
    }
    return figure

if __name__ == '__main__':
    app.run_server(debug=True)

