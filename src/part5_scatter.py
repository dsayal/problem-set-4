'''
PART 5: SCATTER PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part5_plots`
'''

import seaborn as sns
import matplotlib.pyplot as plt

def scatterplot_felony_vs_nonfelony(merged_df):
    '''
    Creates a scatter plot where the x-axis is prediction for felony and the y-axis is prediction for nonfelony.
    The plot is hue by whether the current charge is a felony.
    
    Parameters:
    - merged_df dataframe (merged pred_universe and felony_charge)
    '''
    sns.lmplot(data=merged_df,
               x='prediction_felony',
               y='prediction_nonfelony',
               hue='has_felony_charge',
               fit_reg=False)
    plt.title('Prediction for Felony vs. Non-Felony Rearrest')
    plt.savefig('./data/part5_plots/scatterplot_felony_vs_nonfelony.png', bbox_inches='tight')
    plt.close()

    # Print statement to address the right-side dots
    print("The group of dots on the right side of the plot represents individuals with high predictions for both felony and nonfelony rearrest. This group might include those who are considered high-risk by the model regardless of the type of charge.")

def scatterplot_felony_prediction_vs_actual_rearrest(merged_df):
    '''
    Creates a scatter plot where the x-axis is prediction for felony rearrest and the y-axis is whether someone was actually rearrested.
    
    Parameters:
    - merged_df dataframe (merged pred_universe and felony_charge)
    '''
    sns.scatterplot(data=merged_df,
                    x='prediction_felony',
                    y='actual_rearrest_felony')  # Replace 'actual_rearrest_felony' with the actual column name if different
    plt.title('Prediction for Felony Rearrest vs. Actual Felony Rearrest')
    plt.savefig('./data/part5_plots/scatterplot_felony_prediction_vs_actual_rearrest.png', bbox_inches='tight')
    plt.close()

    # Print statement to address model calibration
    print("Based on this plot, if there is a clear separation between high prediction values and actual rearrest occurrences, the model might be well-calibrated. If there is no clear pattern or significant overlap, the model may need adjustment to improve calibration.")

# Example usage:
# merged_df = merge_felony_charge(pred_universe, felony_charge)  # Ensure this is called before creating plots
# scatterplot_felony_vs_nonfelony(merged_df)
# scatterplot_felony_prediction_vs_actual_rearrest(merged_df)
