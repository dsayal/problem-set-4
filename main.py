'''
- You will run Problem Set 4 from this .py, so make sure to set things up to return outputs accordingly
- Go through each PART and write code / make updates as necessary to produce all required outputs
- Run main.py before you start
'''

import os
import pandas as pd
import src.part1_etl as part1
import src.part2_plot_examples as part2
import src.part3_bar_hist as part3
import src.part4_catplot as part4
import src.part5_scatter as part5
from src.part2_plot_examples import barplots, cat_plots, histograms, scatterplot

def main():
    # Load data
    charge_counts = pd.read_csv('data/charge_counts.csv')
    charge_counts_by_offense = pd.read_csv('data/charge_counts_by_offense.csv')
    pred_universe = pd.read_csv('data/pred_universe.csv')

    # Print column names to debug
    print("Columns in pred_universe:", pred_universe.columns)

    # Apply seaborn settings
    part2.seaborn_settings()

    # Generate plots
    part2.barplots(charge_counts, charge_counts_by_offense)
    part2.cat_plots(charge_counts, pred_universe)
    part2.histograms(pred_universe)
    part2.scatterplot(pred_universe)

if __name__ == "__main__":
    main()








