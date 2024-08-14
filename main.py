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

def main():
    # Load and transform data
    pred_universe, charge_counts, charge_counts_by_offense = part1.extract_transform()
    
    # Print dataframes to ensure they are loaded correctly
    print("pred_universe columns and sample data:")
    print(pred_universe.head())
    print(pred_universe.columns)
    
    print("\ncharge_counts columns and sample data:")
    print(charge_counts.head())
    print(charge_counts.columns)
    
    print("\ncharge_counts_by_offense columns and sample data:")
    print(charge_counts_by_offense.head())
    print(charge_counts_by_offense.columns)
    
    # Create histograms
    part3.create_histograms(pred_universe)
    
    # Create categorical plots
    part4.cat_plots(pred_universe, charge_counts_by_offense)
    
    # Scatter plots
    part5.scatter_plots(pred_universe)
    
if __name__ == "__main__":
    main()






