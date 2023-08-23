import pandas as pd
from constants import FILE_PATHS
from dash import html

def get_file_paths(company_name):
    return FILE_PATHS.get(company_name, {})

def read_files_for_company(company_name):
    """Read files for the given company name and return dataframes for trafego, keywords, and news."""
    # Get the file paths for the given company name
    paths = get_file_paths(company_name)
    
    # Read the files and create dataframes
    trafego_df = pd.read_excel(paths.get('trafego', ''))
    keywords_df = pd.read_excel(paths.get('keywords', ''))
    news_df = pd.read_json(paths.get('news', ''))
    
    return trafego_df, keywords_df, news_df
    
