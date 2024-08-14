import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def part3_bar_plots(pred_universe):
    '''
    Creates bar plots for the 'fta' column in pred_universe and hues by sex
    
    Parameters:
    - pred_universe dataframe
    '''
    # Create a bar plot for the 'fta' column
    sns.barplot(data=pred_universe, 
                x='fta', 
                y='count')  # Adjust if 'count' is not in pred_universe
    plt.title('Bar Plot of FTA Counts')
    plt.savefig('./data/part3_plots/barplot_fta.png', bbox_inches='tight')
    plt.close()

    # Create a bar plot for the 'fta' column, with hue by sex
    sns.barplot(data=pred_universe, 
                x='fta', 
                y='count', 
                hue='sex')  # Adjust if 'count' is not in pred_universe
    plt.title('Bar Plot of FTA Counts by Sex')
    plt.savefig('./data/part3_plots/barplot_fta_by_sex.png', bbox_inches='tight')
    plt.close()

def part3_histograms(pred_universe):
    '''
    Creates histograms for the 'age_at_arrest' column in pred_universe
    
    Parameters:
    - pred_universe dataframe
    '''
    # Plot histogram of age_at_arrest
    sns.histplot(data=pred_universe, 
                 x='age_at_arrest')
    plt.title('Histogram of Age at Arrest')
    plt.savefig('./data/part3_plots/histogram_age_at_arrest.png', bbox_inches='tight')
    plt.close()

    # Create bins for age groups
    bins = [18, 21, 30, 40, 100]
    labels = ['18-21', '21-30', '30-40', '40+']
    pred_universe['age_group'] = pd.cut(pred_universe['age_at_arrest'], bins=bins, labels=labels, right=False)

    # Plot histogram with age groups
    sns.histplot(data=pred_universe, 
                 x='age_at_arrest',
                 hue='age_group',
                 multiple='stack')
    plt.title('Histogram of Age at Arrest by Age Groups')
    plt.savefig('./data/part3_plots/histogram_age_at_arrest_by_groups.png', bbox_inches='tight')
    plt.close()

