import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def create_felony_charge(arrest_events):
    '''
    Creates a dataframe indicating whether each arrest had at least one felony charge
    
    Parameters:
    - arrest_events dataframe
    
    Returns:
    - felony_charge dataframe
    '''
    felony_charge = arrest_events.groupby('arrest_id').apply(
        lambda x: pd.Series({'has_felony_charge': (x['charge_degree'] == 'felony').any()})
    ).reset_index()
    
    print("Felony Charge DataFrame:")
    print(felony_charge.head())
    
    return felony_charge

def merge_felony_charge(pred_universe, felony_charge):
    '''
    Merges the felony_charge dataframe with pred_universe
    
    Parameters:
    - pred_universe dataframe
    - felony_charge dataframe
    
    Returns:
    - merged dataframe
    '''
    merged_df = pd.merge(pred_universe, felony_charge, on='arrest_id')
    
    print("Merged DataFrame:")
    print(merged_df.head())
    
    return merged_df

def cat_plots(charge_counts, pred_universe):
    '''
    Produces different types of categorical plots using the given datasets

    Parameters:
    - charge_counts dataframe
    - pred_universe dataframe

    Returns:
    - Categorical bar plot for charge degree counts
    - Categorical bar plot for prediction_nonfelony by charge degree
    '''
    # Bar plot for charge degree counts
    sns.catplot(data=charge_counts,
                x='charge_degree',
                y='count', 
                kind='bar')
    plt.savefig('./data/part2_plots/catplot1.png', bbox_inches='tight')

    # Bar plot for prediction_nonfelony by charge degree
    sns.catplot(data=pred_universe, 
                x='charge_degree',
                y='prediction_nonfelony', 
                kind='bar')
    plt.savefig('./data/part2_plots/catplot2.png', bbox_inches='tight')






