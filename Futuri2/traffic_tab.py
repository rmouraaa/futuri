
from dash import dcc
from dash import html
from plotting_utils import plot_organic_traffic, plot_time_series_decomposition
from data_utils import read_files_for_company

def render_traffic_tab(selected_company, selected_competitor):
    # Read dataframes for selected company and competitor
    company_df, _, _ = read_files_for_company(selected_company)
    competitor_df, _, _ = read_files_for_company(selected_competitor)
    
    # Generate the traffic plot
    traffic_fig = plot_organic_traffic(company_df, competitor_df, selected_company, selected_competitor)
    
    # Generate the decomposition plots for selected company and competitor
    company_decomposition_fig = plot_time_series_decomposition(company_df, selected_company)
    competitor_decomposition_fig = plot_time_series_decomposition(competitor_df, selected_competitor)
    
    return html.Div([
        dcc.Graph(figure=traffic_fig),
        html.H4('Decomposição de Tráfego de {}'.format(selected_company)),
        dcc.Graph(figure=company_decomposition_fig),
        html.H4('Decomposição de Tráfego de {}'.format(selected_competitor)),
        dcc.Graph(figure=competitor_decomposition_fig)
    ])
