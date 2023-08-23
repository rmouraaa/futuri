
import statsmodels.api as sm
import plotly.subplots as sp
import plotly.graph_objects as go


def plot_organic_traffic(df_company, df_competitor, company_name, competitor_name):
    """
    Create a line plot comparing Organic Traffic of a company and its competitor.
    This updated version includes translations to Portuguese and enhanced tooltips.
    
    Parameters:
    - df_company: DataFrame containing traffic data for the selected company.
    - df_competitor: DataFrame containing traffic data for the competitor.
    - company_name: Name of the selected company.
    - competitor_name: Name of the competitor.
    
    Returns:
    - fig: A plotly graph object for the line plot.
    """
    
    # Extracting Organic Traffic data for the company and its competitor
    company_traffic = df_company[df_company['Metric'] == 'Organic Traffic'].iloc[0, 5:]
    competitor_traffic = df_competitor[df_competitor['Metric'] == 'Organic Traffic'].iloc[0, 5:]
    
    # Creating the line plot
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=company_traffic.index, y=company_traffic.values,
                             mode='lines+markers', name=company_name,
                             text=company_traffic.values, hoverinfo='x+text+name'))
    
    fig.add_trace(go.Scatter(x=competitor_traffic.index, y=competitor_traffic.values,
                             mode='lines+markers', name=competitor_name,
                             text=competitor_traffic.values, hoverinfo='x+text+name'))
    
    fig.update_layout(title='Comparação de Tráfego Orgânico entre {} e {}'.format(company_name, competitor_name),
                      xaxis_title='Mês',
                      yaxis_title='Tráfego Orgânico',
                      xaxis=dict(showline=True, showgrid=False),
                      yaxis=dict(showgrid=True, gridcolor='rgba(230,230,230,0.8)'),
                      plot_bgcolor='rgba(255,255,255,1)')
    
    return fig

def plot_time_series_decomposition(df, company_name):
    """
    Decompose the time series data into trend, seasonal, and residual components and plot them.
    This version uses the updated seasonal_decompose function.
    
    Parameters:
    - df: DataFrame containing time series data.
    - company_name: Name of the company for the title.
    
    Returns:
    - fig: A plotly graph object with the three subplots.
    """
    
    # Extracting Organic Traffic data
    traffic_data = df[df['Metric'] == 'Organic Traffic'].iloc[0, 5:]
    
    # Decomposing the time series
    decomposition = sm.tsa.seasonal_decompose(traffic_data, model='additive', extrapolate_trend='freq', period=12)
    
    # Creating subplots
    fig = sp.make_subplots(rows=3, cols=1, 
                           subplot_titles=('Tendência', 'Sazonalidade', 'Residual'),
                           shared_xaxes=True)
    
    # Plotting trend
    fig.add_trace(go.Scatter(x=traffic_data.index, y=decomposition.trend, mode='lines'), row=1, col=1)
    
    # Plotting seasonal
    fig.add_trace(go.Scatter(x=traffic_data.index, y=decomposition.seasonal, mode='lines'), row=2, col=1)
    
    # Plotting residual
    fig.add_trace(go.Scatter(x=traffic_data.index, y=decomposition.resid, mode='lines'), row=3, col=1)
    
    fig.update_layout(title='Decomposição de Tráfego Orgânico de {}'.format(company_name))
    
    return fig