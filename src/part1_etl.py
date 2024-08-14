'''
PART 1: ETL
- This code sets up the datasets for Problem Set 4
- NOTE: You will update this code for PART 4: CATEGORICAL PLOTS
'''

import pandas as pd

def extract_transform():
    """
    Extracts and transforms data from CSV files, and merges them into a single DataFrame.
    
    Returns:
    - pred_universe DataFrame
    - charge_counts DataFrame
    - charge_counts_by_offense DataFrame
    """
    # Load datasets
    pred_universe = pd.read_csv('./data/pred_universe.csv')
    charge_counts = pd.read_csv('./data/charge_counts.csv')
    charge_counts_by_offense = pd.read_csv('./data/charge_counts_by_offense.csv')

    # Display columns and sample data for debugging
    print("part1_etl: pred_universe columns and sample data:")
    print(pred_universe.head())
    print(pred_universe.columns)

    print("part1_etl: charge_counts columns and sample data:")
    print(charge_counts.head())
    print(charge_counts.columns)

    print("part1_etl: charge_counts_by_offense columns and sample data:")
    print(charge_counts_by_offense.head())
    print(charge_counts_by_offense.columns)

    # Merge dataframes as needed
    # Example merge (assuming 'charge_degree' is a common column)
    merged_df = pd.merge(pred_universe, charge_counts, on='charge_degree', how='left')
    
    # Save the merged DataFrame for later use
    merged_df.to_csv('./data/merged_data.csv', index=False)

    return pred_universe, charge_counts, charge_counts_by_offense

def create_felony_charge(pred_universe):
    """
    Creates a DataFrame indicating whether each arrest had at least one felony charge.

    Parameters:
    - pred_universe DataFrame

    Returns:
    - felony_charge DataFrame
    """
    felony_charge = pred_universe[pred_universe['charge_degree'] == 'felony']
    return felony_charge

def merge_felony_pred_universe(pred_universe, felony_charge):
    """
    Merges the felony charge data with the prediction universe.

    Parameters:
    - pred_universe DataFrame
    - felony_charge DataFrame

    Returns:
    - merged_felony_pred DataFrame
    """
    merged_felony_pred = pd.merge(pred_universe, felony_charge, on='arrest_id', how='left')
    return merged_felony_pred

