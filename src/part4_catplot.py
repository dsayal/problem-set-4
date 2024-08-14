'''
PART 4: CATEGORICAL PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part4_plots`
'''
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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
    return merged_df

def part4_catplot(pred_universe, arrest_events):
    '''
    Creates categorical plots
    
    Parameters:
    - pred_universe dataframe
    - arrest_events dataframe
    '''
    # Create felony charge dataframe
    felony_charge = create_felony_charge(arrest_events)
    
    # Merge with pred_universe
    merged_df = merge_felony_charge(pred_universe, felony_charge)
    
    # Ensure output directory exists
    output_dir = './data/part4_plots'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 1. Catplot for prediction of felony rearrest by charge type
    sns.catplot(data=merged_df,
                x='charge_degree',
                y='prediction_felony',
                kind='bar')
    plt.title('Prediction for Felony Rearrest by Charge Degree')
    plt.savefig(f'{output_dir}/catplot_felony_rearrest.png', bbox_inches='tight')
    plt.close()

    # 2. Catplot for prediction of non-felony rearrest by charge type
    sns.catplot(data=merged_df,
                x='charge_degree',
                y='prediction_nonfelony',
                kind='bar')
    plt.title('Prediction for Non-Felony Rearrest by Charge Degree')
    plt.savefig(f'{output_dir}/catplot_nonfelony_rearrest.png', bbox_inches='tight')
    plt.close()
    
    # Print statement to address the difference
    print("Differences between felony and non-felony rearrest predictions might be explained by the inherent characteristics of felony versus non-felony offenses. Felonies may have different underlying patterns or risk factors that influence rearrest predictions.")

    # 3. Catplot for prediction of felony rearrest by charge type with hue for actual rearrest
    sns.catplot(data=merged_df,
                x='charge_degree',
                y='prediction_felony',
                hue='has_felony_charge',
                kind='bar')
    plt.title('Prediction for Felony Rearrest by Charge Degree with Hue for Actual Felony Charge')
    plt.savefig(f'{output_dir}/catplot_felony_rearrest_with_hue.png', bbox_inches='tight')
    plt.close()
    
    # Print statement to address the hue difference
    print("If predictions for arrestees with current felony charges but who did not get rearrested for a felony are higher than those with a current misdemeanor but who did get rearrested for a felony, it suggests that the model might be overestimating the risk for certain groups or not fully capturing the complexity of rearrest behavior.")

