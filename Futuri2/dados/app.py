import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from defs import CONCORRENTES
from components import get_marca_dropdown, get_concorrente_dropdown, get_dashboard_tabs



app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    get_marca_dropdown(),
    html.Br(),
    get_concorrente_dropdown(),
    html.Br(),
    dbc.Button('Gerar Dashboard', id='gerar-btn', color='primary'),
    get_dashboard_tabs()
])

@app.callback(
    Output('concorrente-dropdown', 'options'),
    Input('marca-dropdown', 'value')
)
def update_dropdown(marca_selecionada):
    if marca_selecionada:
        return [{'label': concorrente, 'value': concorrente} for concorrente in CONCORRENTES[marca_selecionada]]
    return []

@app.callback(
    Output('tabs-content', 'children'),
    [Input('tabs', 'value'),
     Input('gerar-btn', 'n_clicks')],
    [State('marca-dropdown', 'value'),
     State('concorrente-dropdown', 'value')]
)
def update_tabs_content(tab, btn_click, marca, concorrente):
    if not marca or not concorrente:
        return 'Selecione uma marca e um concorrente primeiro.'
    
    if btn_click:
        if tab == 'tab-1':
            return f'Dados de tráfego para {marca} e {concorrente}'
        elif tab == 'tab-2':
            return f'Dados de keywords para {marca} e {concorrente}'
        elif tab == 'tab-3':
            return f'Notícias relacionadas a {marca} e {concorrente}'
    return ''

if __name__ == '__main__':
    app.run_server(debug=True)
