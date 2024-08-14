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

import pandas as pd
import os

# Create directories if they don't exist
directories = [
    './data/part2_plots',
    './data/part3_plots',
    './data/part4_plots',
    './data/part5_plots'
]

for directory in directories:
    if not os.path.exists(directory):
        os.makedirs(directory)

def main():
    ##  PART 1: ETL  ##
    # ETL the datasets into dataframes
    pred_universe, arrest_events, charge_counts, charge_counts_by_offense = part1.extract_transform()

    ##  PART 2: PLOT EXAMPLES  ##
    # Apply plot theme
    part2.seaborn_settings()

    # Generate plots
    part2.barplots(charge_counts, charge_counts_by_offense)
    part2.cat_plots(charge_counts, pred_universe)
    part2.histograms(pred_universe)
    part2.scatterplot(pred_universe)

    ##  PART 3: BAR PLOTS AND HISTOGRAMS  ##
    # Create bar plots and histograms
    part3.part3_bar_plots(pred_universe)
    part3.part3_histograms(pred_universe)

    ##  PART 4: CATEGORICAL PLOTS  ##
    # 1. Create felony_charge dataframe
    felony_charge = arrest_events.groupby('arrest_id').apply(lambda x: pd.Series({
        'has_felony_charge': (x['charge_degree'] == 'Felony').any()
    })).reset_index()
    
    # 2. Merge felony_charge with pred_universe
    merged_df = pd.merge(pred_universe, felony_charge, on='arrest_id', how='left')

    # 3. Generate categorical plots
    part4.catplot_felony_prediction(merged_df)
    part4.catplot_nonfelony_prediction(merged_df)
    part4.catplot_felony_prediction_hue(merged_df)

    ##  PART 5: SCATTERPLOTS  ##
    # Generate scatter plots
    part5.scatterplot_felony_vs_nonfelony(merged_df)
    part5.scatterplot_felony_prediction_vs_actual_rearrest(merged_df)

if __name__ == "__main__":
    main()

