'''
PART 1: ETL
- This code sets up the datasets for Problem Set 4
- NOTE: You will update this code for PART 4: CATEGORICAL PLOTS
'''

import pandas as pd

def load_data():
    # Load the datasets
    pred_universe = pd.read_csv('./data/pred_universe.csv')
    charge_counts = pd.read_csv('./data/charge_counts.csv')
    charge_counts_by_offense = pd.read_csv('./data/charge_counts_by_offense.csv')
    
    # Print DataFrame columns and sample data
    print("Columns in pred_universe:", pred_universe.columns)
    print("Sample data from pred_universe:")
    print(pred_universe.head())
    
    print("Columns in charge_counts:", charge_counts.columns)
    print("Sample data from charge_counts:")
    print(charge_counts.head())
    
    print("Columns in charge_counts_by_offense:", charge_counts_by_offense.columns)
    print("Sample data from charge_counts_by_offense:")
    print(charge_counts_by_offense.head())
    
    return pred_universe, charge_counts, charge_counts_by_offense

def process_data(pred_universe, charge_counts, charge_counts_by_offense):
    # Example processing: Check the columns to ensure data is as expected
    if 'arrest_id' not in pred_universe.columns:
        raise ValueError("The 'arrest_id' column is missing in pred_universe.")
    
    # Since charge_counts and charge_counts_by_offense do not have 'arrest_id',
    # you cannot merge them with pred_universe. You might need different processing.
    
    # If merging is necessary and you have a common column, adjust accordingly.
    # For demonstration, we'll just return the DataFrames for now.
    
    return charge_counts, charge_counts_by_offense

def save_data(charge_counts, charge_counts_by_offense):
    # Save processed DataFrames if needed
    charge_counts.to_csv('./data/processed/charge_counts_processed.csv', index=False)
    charge_counts_by_offense.to_csv('./data/processed/charge_counts_by_offense_processed.csv', index=False)

def main():
    # Load the data
    pred_universe, charge_counts, charge_counts_by_offense = load_data()
    
    # Process the data
    charge_counts, charge_counts_by_offense = process_data(pred_universe, charge_counts, charge_counts_by_offense)
    
    # Save the processed data
    save_data(charge_counts, charge_counts_by_offense)
    
    print("Data processing complete. Check the 'processed' directory for output files.")

if __name__ == "__main__":
    main()



