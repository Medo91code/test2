import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id='input-box', type='text'),
    html.Button('Submit', id='button'),
    html.P(id='output-box')

])


@app.callback(
    Output('output-box', 'children'),
    [Input('button', 'n_clicks')],
    [State('input-box', 'value')])
def update_output(n_clicks, value):
    if value == '1234':
        print('ok')
    else:
        print('wrong')
    return value


if __name__ == '__main__':
    app.run_server()