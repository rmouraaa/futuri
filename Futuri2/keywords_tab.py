
import dash_html_components as html

def render_keywords_tab(selected_company, selected_competitor):
    # TODO: Add specific content for the Keywords tab here.
    # For now, we are returning a placeholder message.
    
    return html.Div([
        html.H3('Conteúdo da aba Keywords para {} e {}'.format(selected_company, selected_competitor))
    ])
