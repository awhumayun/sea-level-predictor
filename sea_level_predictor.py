import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], label='Data')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    years_ext = pd.Series([i for i in range(1880, 2051)])
    sea_level_pred = intercept + slope * years_ext
    plt.plot(years_ext, sea_level_pred, 'r', label='Best fit line (1880-2050)')

    # Create second line of best fit
    data_2000 = data[data['Year'] >= 2000]
    slope_2000, intercept_2000, r_value_2000, p_value_2000, std_err_2000 = linregress(data_2000['Year'], data_2000['CSIRO Adjusted Sea Level'])
    years_2000_ext = pd.Series([i for i in range(2000, 2051)])
    sea_level_2000_pred = intercept_2000 + slope_2000 * years_2000_ext
    plt.plot(years_2000_ext, sea_level_2000_pred, 'g', label='Best fit line (2000-2050)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()