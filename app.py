# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

collatz = pd.read_csv('data/collatz.csv', index_col=0)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css', 'styles.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
  style={
    'textAlign': 'center',
    'paddingLeft': '1em',
    'paddingRight': '1em',
    'paddingTop': '0.5em',
  },
  children=[
  html.Div(
    style={
      'display': 'flex',
      'flex-direction': 'column',
      'alignItems': 'center',
    },
    children=[
      html.H1(children='Collatz Conjecture Traces'),
      html.Div(
        children=[
          'The path of a number to 1 following the ',
          html.A(
            href='https://en.wikipedia.org/wiki/Collatz_conjecture',
            target='_blank',
            children='Collatz algorithm',
          ), 
          ' is called its Collatz Trace. ',
          'The Collatz Conjecture is a famous unsolved problem in Algorithm Analysis.',
        ],
      ),
      html.Div(
        style={
          'width': '90%',
          'paddingTop': '1em',
          'paddingBottom': '2em',
        },
        children=[
          dcc.Slider(
            id='start-num-slider',
            min=2,
            max=1000,
            marks={
              i if i != 0 else 2: str(i) if i != 0 else '2' for i in range(0, 1001, 100) # messy
            },
            value=500,
          ),
        ],
      ),
      html.Div(children='Adjust the slider above to analyse each number\'s trace'),
    ],
  ),
  
  html.Div(
    style={
      'display': 'flex',
      'padding': '2em',
      'flexWrap': 'wrap',
    },
    children=[
      html.Div(
        style={
          'flex': 1,
          'minWidth': '90px',
        },
        children=[
          html.Div(className='metric-title', children=[
            'Start Number ',
          ]),
          html.Div(id='metric-start-num', className='metric-value metric-start-num'),
          html.Div(className='metric-block', children=[
            html.Div(className='metric-title', children='Steps'),
            html.Div(id='metric-steps', className='metric-value'),
          ]),
          html.Div(className='metric-block', children=[
            html.Div(className='metric-title', children='Largest Number'),
            html.Div(id='metric-largest-num', className='metric-value'),
          ]),
          html.Div(className='metric-block', children=[
            html.Div(className='metric-title', children='Even Steps'),
            html.Div(id='metric-even-steps', className='metric-value'),
          ]),
          html.Div(className='metric-block', children=[
            html.Div(className='metric-title', children='Odd Steps'),
            html.Div(id='metric-odd-steps', className='metric-value'),
          ]),
        ],
      ),
      dcc.Graph(
        id='collatz-trace-graph',
        style={'flex': 6},
      ),
    ],
  ),

  html.Div(
    style={'paddingTop': '4em'},
    children=[
      html.Div(children='''
        The beauty of the Collatz conjecture problem is that it can 
        be expressed as a simple recursive function yet it has
        been unsolved for 80 years.
      '''),
      html.Div(children='''
        The problem has remained essentially unscathed by any attempts
        at proof since its introduction in 1937.
      '''),
    ],
  ),
  html.Div(
    style={'paddingTop': '2em'},
    children=[
      html.Div(children='''
        It is believed that a proof of the conjecture could reveal
        insights into relationships between the prime factorizations of
        numbers.
      '''),
      html.Div(children='''
        Many mathematicians however concede that a proof could be well
        outside of the reach of current mathematics.
      '''),
    ],
  ),
  html.Div(
    children=[
      dcc.Graph(
        id='steps-vs-start',
        style={'height': '600px'},
        figure={
          'data': [
            go.Scatter(
              x=collatz[::2].index,
              y=collatz.iloc[::2]['steps'],
              mode='markers',
              marker={'color': 'red'},
              opacity=0.7,
              name='Even Start Number',
            ),
            go.Scatter(
              x=collatz.index[1::2],
              y=collatz.iloc[1::2]['steps'],
              mode='markers',
              marker={'color': '#629FCA'},
              opacity=0.7,
              name='Odd Start Number',
            ),
          ],
          'layout': {
            'yaxis': {'title':'Steps'},
            'xaxis': {'title':'Start Number'},
            'hovermode': False,
          }
        },
      ),
    ],
  ),

  html.Div(
    style={'paddingTop': '4em'},
    children=[
      html.Div(children='''
        The above graph of the number of steps vs start number shows
        my favourite characteristic of the Collatz algorithm:
      '''),
      html.Div(children='''
        The recognizable order of the data points, arising from the
        tree-structure of the traces.
      '''),
    ],
  ),
  html.Div(
    style={'paddingTop': '2em'},
    children=[
      html.Div(children='''
        We can see and understand the pattern that is formed by the 
        algorithm, without even a grasp of the problem's true complexity.
      '''),
      html.Div(children='''
        Moreover, perhaps revisiting the structure of similar 
        visualizations, once the problem is better understood, will fill
        them with previously unseen meaning.
      '''),
    ],
  ),

  html.Div(
    children=[
      dcc.Graph(
        id='largest-vs-start',
        style={'height':'800px'},
        figure={
          'data': [
            go.Scatter(
              x=collatz.index,
              y=collatz.loc[collatz['largest'] < 50000, 'largest'],
              mode='markers',
              opacity=0.7,
            ),
          ],
          'layout': {
            'yaxis': {'title':'Largest Number in Trace'},
            'xaxis': {'title':'Start Number'},
            'hovermode': False,
          }
        },
      ),
    ],
  ),

  html.Div(
    style={'paddingTop': '4em'},
    children=[
      html.Div(children='''
        These visualizations can aid our initial understanding of the 
        algorithm and intrigue us with the idea that there might be
        deeper, underlying meaning to them.
      '''),
      html.Div(children='''
        The simple appearance of the Collatz algorithm contrasted with
        the enormous complexity of the conjecture leads me to believe
        that there is something we are missing or currently incapable
        of percieving.
      '''),
    ],
  ),
  html.Div(
    style={'paddingTop': '2em', 'paddingBottom': '4em'},
    children=[
      html.Div(children='''
        I wonder if we will see new relationships in the data that  
        are as obvious as the currently understood features, once the
        conjecture is understood.
      '''),
    ],
  ),
])

@app.callback(
  dash.dependencies.Output('collatz-trace-graph', 'figure'),
  [dash.dependencies.Input('start-num-slider', 'value')])
def update_collatz_trace(start_num):
  trace = pd.eval(collatz.loc[start_num, 'trace'])
  return {
    'data': [
      {'x': len(trace), 'y': trace, 'type': 'line'},
    ],
    'layout': {
      'yaxis': {'title':'Value'},
      'xaxis': {'title':'Step'},
      'margin': {'t':30, 'b':30},
    }
  }

# Callback to update metrics
@app.callback(
  dash.dependencies.Output('metric-start-num', 'children'),
  [dash.dependencies.Input('start-num-slider', 'value')])
def update_start_number(start_num):
  return start_num

@app.callback(
  dash.dependencies.Output('metric-steps', 'children'),
  [dash.dependencies.Input('start-num-slider', 'value')])
def update_steps(start_num):
  return collatz.loc[start_num, 'steps']

@app.callback(
  dash.dependencies.Output('metric-largest-num', 'children'),
  [dash.dependencies.Input('start-num-slider', 'value')])
def update_largest_number(start_num):
  return collatz.loc[start_num, 'largest']

@app.callback(
  dash.dependencies.Output('metric-even-steps', 'children'),
  [dash.dependencies.Input('start-num-slider', 'value')])
def update_odd_steps(start_num):
  return collatz.loc[start_num, 'evens']

@app.callback(
  dash.dependencies.Output('metric-odd-steps', 'children'),
  [dash.dependencies.Input('start-num-slider', 'value')])
def update_even_steps(start_num):
  return collatz.loc[start_num, 'odds']
# end callback to update metrics

if __name__ == '__main__':
  app.run_server(debug=True)
