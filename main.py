'''
- You will run Problem Set 4 from this .py, so make sure to set things up to return outputs accordingly
- Go through each PART and write code / make updates as necessary to produce all required outputs
- Run main.py before you start
'''

import src.part1_etl as part1
import src.part2_plot_examples as part2
import src.part3_bar_hist as part3
import src.part4_catplot as part4
import src.part5_scatter as part5
import importlib

# Reloading modules
importlib.reload(part1)
importlib.reload(part2)
importlib.reload(part3)
importlib.reload(part4)
importlib.reload(part5)

def main():
    """The main function to execute the data processing and visualization tasks.
    """

        # Load and process the data
    charge_counts, pred_universe, charge_counts_by_offense = part1.extract_transform()
    print("Data loaded successfully.")

        # Merging data
    felony_charge = part1.create_felony_charge()
    merged_data = part1.merge_felony_pred_universe(felony_charge, pred_universe)
    merged_df = part4.merge_felony_charge(pred_universe, felony_charge)
        
        # Print DataFrames to verify
    print("Columns in pred_universe:", pred_universe.columns)
    print("Sample data from pred_universe:")
    print(pred_universe.head())

    print("Columns in charge_counts:", charge_counts.columns)
    print("Sample data from charge_counts:")
    print(charge_counts.head())

    print("Columns in charge_counts_by_offense:", charge_counts_by_offense.columns)
    print("Sample data from charge_counts_by_offense:")
    print(charge_counts_by_offense.head())

    print("Columns in felony_charge:", felony_charge.columns)
    print("Sample data from felony_charge:")
    print(felony_charge.head())

    print("Columns in merged_data:", merged_data.columns)
    print("Sample data from merged_data:")
    print(merged_data.head())

        # Part 2: Generate categorical plots
    part2.cat_plots(charge_counts, pred_universe)
        
        # Part 3: Generate bar and histogram plots
    part3.part3_bar_plots(pred_universe)  # Updated function name
    part3.part3_histograms(pred_universe)  # Updated function name

        # Part 4: Generate additional categorical plots
    part4.cat_plots(charge_counts, pred_universe)

        # Part 5: Generate scatter plots
    part5.scatterplot_felony_vs_nonfelony(merged_df)
    part5.scatterplot_felony_prediction_vs_actual_rearrest(merged_df)

if __name__ == "__main__":
    main()















