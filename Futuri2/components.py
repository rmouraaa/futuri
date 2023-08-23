from dash import dcc, html
from constants import COMPANIES

def create_company_dropdown():
    return dcc.Dropdown(
        id='company-dropdown',
        options=[{'label': company, 'value': company} for company in COMPANIES.keys()],
        value='AGC'
    )

def create_competitor_dropdown():
    return dcc.Dropdown(
        id='competitor-dropdown',
        value='Vivix'  # valor inicial
    )

def create_tabs():
    return dcc.Tabs([
        dcc.Tab(label='Tráfego', value='tab-traffic', children=[
            html.Div([
                html.H3('Conteúdo da aba Tráfego')
            ])
        ]),
        dcc.Tab(label='Keywords', value='tab-keywords', children=[
            html.Div([
                html.H3('Conteúdo da aba Keywords')
            ])
        ]),
        dcc.Tab(label='Notícias', value='tab-news', children=[
            html.Div([
                html.H3('Conteúdo da aba Notícias')
            ])
        ]),
    ])
