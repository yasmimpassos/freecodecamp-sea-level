import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    years_extended = pd.Series([*range(df['Year'].min(), 2051)])
    
    sea_levels_predicted = intercept + slope * years_extended

    plt.plot(years_extended, sea_levels_predicted, 'r')

    # Create second line of best fit

    df_second = df[df['Year'] >= 2000]
    slope_2000, intercept_2000, r_value, p_value, std_err = linregress(df_second['Year'], df_second['CSIRO Adjusted Sea Level'])

    years_2000_extended = pd.Series([*range(2000, 2051)])

    sea_levels_predicted_2000 = intercept_2000 + slope_2000 * years_2000_extended
    plt.plot(years_2000_extended, sea_levels_predicted_2000, 'g')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()