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
    ## PART 1: ETL 
    # ETL the datasets into dataframes
    pred_universe, arrest_events, charge_counts, charge_counts_by_offense = part1.extract_transform()
    
    # Print the columns and first few rows of the DataFrames to check their structure
    print("pred_universe columns and sample data:")
    print(pred_universe.head())
    print(pred_universe.columns)
    
    print("charge_counts columns and sample data:")
    print(charge_counts.head())
    print(charge_counts.columns)
    
    print("charge_counts_by_offense columns and sample data:")
    print(charge_counts_by_offense.head())
    print(charge_counts_by_offense.columns)

    ## PART 2: PLOT EXAMPLES ##
    # Apply plot theme
    part2.seaborn_settings()

    # Generate plots
    part2.barplots(charge_counts, charge_counts_by_offense)
    part2.cat_plots(charge_counts, pred_universe)
    part2.histograms(pred_universe)
    part2.scatterplot(pred_universe)

    ## PART 3: BAR PLOTS AND HISTOGRAMS ##
    part3.part3_bar_plots(pred_universe)
    part3.part3_histograms(pred_universe)

    ## PART 4: CATEGORICAL PLOTS ##
    part4.part4_catplot(pred_universe, charge_counts)

    ## PART 5: SCATTERPLOTS ##
    part5.part5_scatter(pred_universe)

if __name__ == "__main__":
    main()




