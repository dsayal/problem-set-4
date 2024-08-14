'''
PART 1: ETL
- This code sets up the datasets for Problem Set 4
- NOTE: You will update this code for PART 4: CATEGORICAL PLOTS
'''

import pandas as pd

def extract_transform():
    """
    Extracts and loads data from CSV files for analysis.

    This function reads three datasets: `pred_universe`, `charge_counts`, and `charge_counts_by_offense`
    from CSV files located in the `./data/` directory. It prints the columns and sample data from each
    DataFrame for debugging purposes.

    Returns:
        tuple: A tuple containing three DataFrames:
            - charge_counts (DataFrame): DataFrame with charge counts aggregated by charge degree.
            - pred_universe (DataFrame): DataFrame with predictions for felony and non-felony rearrests.
            - charge_counts_by_offense (DataFrame): DataFrame with charge counts aggregated by offense category.
            """
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
    """
    Creates a DataFrame indicating whether each arrest involved a felony charge.

    This function generates a DataFrame with sample data indicating felony charges. 
    In practice, this function should be replaced with the actual logic to create 
    the `felony_charge` DataFrame based on real data.

    Returns:
        DataFrame: A DataFrame with columns `arrest_id` and `felony` where `felony` 
        indicates whether the arrest involved a felony charge.
    """
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
    """
    This function combines the `felony_charge` DataFrame, which contains information on whether 
    an arrest involved a felony charge, with the `pred_universe` DataFrame, which contains 
    prediction data for rearrests. The merge is performed on the `arrest_id` column using an 
    inner join.

    Args:
        felony_charge (pd.DataFrame): DataFrame containing `arrest_id` and a boolean `felony` 
                                      indicating whether each arrest involved a felony charge.
        pred_universe (pd.DataFrame): DataFrame containing `arrest_id`, `prediction_felony`, 
                                      and `prediction_nonfelony` for each arrest.

    Returns:
        pd.DataFrame: A DataFrame resulting from the merge of `felony_charge` and `pred_universe`, 
                      including columns from both DataFrames.
    """
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





