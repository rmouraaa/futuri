
from dash import html

def render_news_tab(selected_company, selected_competitor):
    # TODO: Add specific content for the News tab here.
    # For now, we are returning a placeholder message.
    
    return html.Div([
        html.H3('Conteúdo da aba Notícias para {} e {}'.format(selected_company, selected_competitor))
    ])
