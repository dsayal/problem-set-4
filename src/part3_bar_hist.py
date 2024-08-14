import seaborn as sns
import matplotlib.pyplot as plt

def part3_bar_plots(pred_universe):
    """
    Creates bar plots from the pred_universe DataFrame.

    Args:
        pred_universe (pd.DataFrame): The DataFrame containing prediction-related data for individuals.
    """
    # Example of creating a bar plot with available columns
    # Assuming you want to plot counts of felony and non-felony predictions
    if 'prediction_felony' in pred_universe.columns and 'prediction_nonfelony' in pred_universe.columns:
        felony_counts = pred_universe['prediction_felony'].value_counts().reset_index()
        felony_counts.columns = ['prediction_felony', 'count']
        
        plt.figure(figsize=(10, 6))
        sns.barplot(data=felony_counts, x='prediction_felony', y='count')
        plt.title('Counts of Felony Predictions')
        plt.xlabel('Prediction of Felony')
        plt.ylabel('Count')
        plt.savefig('./data/part3_plots/felony_predictions.png', bbox_inches='tight')
        plt.close()
    else:
        raise ValueError("Required columns are not present in the DataFrame")

def part3_histograms(pred_universe):
    """
    Create histograms for Part 3 of the project.
    
    Arguments:
    - pred_universe: DataFrame containing the prediction-related data
    """
    print("part3_histograms: pred_universe columns and sample data:")
    print(pred_universe.head())
    print(pred_universe.columns)
    
    # Plot histogram of 'age_at_arrest'
    plt.figure(figsize=(10, 6))
    sns.histplot(pred_universe['age_at_arrest'])
    plt.title('Histogram of Age at Arrest')
    plt.savefig('./data/part3_plots/histogram_age_at_arrest.png', bbox_inches='tight')
    plt.close()


