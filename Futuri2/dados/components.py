from dash import dcc, html

def get_marca_dropdown():
    return dcc.Dropdown(
        id='marca-dropdown',
        options=[{'label': marca, 'value': marca} for marca in CONCORRENTES.keys()],
        value=None,
        placeholder='Selecione uma marca'
    )

def get_concorrente_dropdown():
    return dcc.Dropdown(
        id='concorrente-dropdown',
        options=[],
        value=None,
        placeholder='Selecione um concorrente'
    )

def get_dashboard_tabs():
    return html.Div(id='dashboard-content', children=[
        dcc.Tabs(id='tabs', value='tab-1', children=[
            dcc.Tab(label='Tráfego', value='tab-1'),
            dcc.Tab(label='Keywords', value='tab-2'),
            dcc.Tab(label='Notícias', value='tab-3')
        ]),
        html.Div(id='tabs-content')
    ])
