
# Importando as bibliotecas necessárias
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from data_utils import read_files_for_company
from traffic_tab import render_traffic_tab
from keywords_tab import render_keywords_tab
from news_tab import render_news_tab

# Dicionário de empresas e seus concorrentes
companies = {
    'AGC': ['Vivix', 'Guardian', 'Cebrace'],
    'Visa': ['Mastercard', 'American Express'],
    'Polenghi': ['Tirolez', 'Catupiry']
}

# Inicializando a aplicação Dash
app = dash.Dash(__name__)

# Definindo o layout da aplicação
app.layout = html.Div([
    html.Div([
        html.Label('Empresa:'),
        dcc.Dropdown(
            id='company-dropdown',
            options=[{'label': company, 'value': company} for company in companies.keys()],
            value='AGC'
        ),
        html.Label('Concorrente:'),
        dcc.Dropdown(
            id='competitor-dropdown',
            value='Vivix'  # valor inicial
        ),
        html.Br(),
        html.Button('Gerar Dashboard', id='generate-button', n_clicks=0),
    ]),
    html.Div(id='tabs-content', children=[])
])

# Callback para preencher o dropdown de concorrentes baseado na empresa selecionada
@app.callback(
    Output('competitor-dropdown', 'options'),
    Input('company-dropdown', 'value')
)
def set_competitors_options(selected_company):
    return [{'label': competitor, 'value': competitor} for competitor in companies[selected_company]]

# Callback para gerar as abas após clicar no botão
@app.callback(
    Output('tabs-content', 'children'),
    Input('generate-button', 'n_clicks'),
    Input('company-dropdown', 'value'),
    Input('competitor-dropdown', 'value'),
    prevent_initial_call=True  # Evita que seja chamado no primeiro carregamento
)
def generate_tabs(n_clicks, selected_company, selected_competitor):
    return dcc.Tabs([
        dcc.Tab(label='Tráfego', value='tab-traffic', children=render_traffic_tab(selected_company, selected_competitor)),
        dcc.Tab(label='Keywords', value='tab-keywords', children=render_keywords_tab(selected_company, selected_competitor)),
        dcc.Tab(label='Notícias', value='tab-news', children=render_news_tab(selected_company, selected_competitor))
    ])

# Executando a aplicação
if __name__ == '__main__':
    app.run_server(debug=True)
