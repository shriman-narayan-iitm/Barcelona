import pandas as pd
import numpy as np

def analyze_repo_features(csv_file):
    
    df = pd.read_csv(csv_file)
    
    if df['has_projects'].dtype == 'object':
        df['has_projects'] = df['has_projects'].map({'true': True, 'false': False})
    if df['has_wiki'].dtype == 'object':
        df['has_wiki'] = df['has_wiki'].map({'true': True, 'false': False})
    
    correlation = df['has_projects'].corr(df['has_wiki'])
    
    stats = {
        'total_repos': len(df),
        'projects_enabled': df['has_projects'].sum(),
        'wiki_enabled': df['has_wiki'].sum(),
        'both_enabled': ((df['has_projects']) & (df['has_wiki'])).sum(),
        'neither_enabled': ((~df['has_projects']) & (~df['has_wiki'])).sum()
    }
    
    return round(correlation, 3), stats

correlation, stats = analyze_repo_features('repositories.csv')
print(f"Correlation coefficient: {correlation}")
print("\nAdditional Statistics:")
for key, value in stats.items():
    print(f"{key}: {value}")