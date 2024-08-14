'''
PART 1: ETL
- This code sets up the datasets for Problem Set 4
- NOTE: You will update this code for PART 4: CATEGORICAL PLOTS
'''

import pandas as pd

def extract_transform():
    try:
        # Load the datasets
        pred_universe = pd.read_csv('./data/pred_universe.csv')
        charge_counts = pd.read_csv('./data/charge_counts.csv')
        charge_counts_by_offense = pd.read_csv('./data/charge_counts_by_offense.csv')
        
        # Print DataFrame columns and sample data for debugging
        print("Columns in pred_universe:", pred_universe.columns)
        print("Sample data from pred_universe:")
        print(pred_universe.head())
        
        print("Columns in charge_counts:", charge_counts.columns)
        print("Sample data from charge_counts:")
        print(charge_counts.head())
        
        print("Columns in charge_counts_by_offense:", charge_counts_by_offense.columns)
        print("Sample data from charge_counts_by_offense:")
        print(charge_counts_by_offense.head())

        # Return the DataFrames
        return charge_counts, pred_universe, charge_counts_by_offense

    except FileNotFoundError as e:
        print(f"Error: {e}. Please check the file paths and names.")
        return None, None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None, None

def create_felony_charge():
    try:
        # Assuming the function to create felony charge DataFrame
        # This is an example and should be replaced with actual logic
        felony_charge = pd.DataFrame({
            'arrest_id': [1, 2, 3, 4],
            'felony': [True, False, True, False]
        })
        
        print("Columns in felony_charge:", felony_charge.columns)
        print("Sample data from felony_charge:")
        print(felony_charge.head())
        
        return felony_charge
    except Exception as e:
        print(f"An error occurred in create_felony_charge: {e}")
        return None

def merge_felony_pred_universe(felony_charge, pred_universe):
    try:
        # Merge the felony_charge DataFrame with pred_universe DataFrame
        merged_data = pd.merge(felony_charge, pred_universe, on='arrest_id', how='inner')
        
        print("Columns in merged_data:", merged_data.columns)
        print("Sample data from merged_data:")
        print(merged_data.head())
        
        return merged_data
    except Exception as e:
        print(f"An error occurred in merge_felony_pred_universe: {e}")
        return None

def main():
    # Load and print data
    charge_counts, pred_universe, charge_counts_by_offense = extract_transform()
    # Create felony charge DataFrame
    felony_charge = create_felony_charge()
    # Merge dataframes
    merged_data = merge_felony_pred_universe(felony_charge, pred_universe)

if __name__ == "__main__":
    main()





