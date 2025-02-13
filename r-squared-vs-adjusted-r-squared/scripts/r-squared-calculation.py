"""
===============================================
Objective: R-squared Vs Adjusted R-squared comparision
Sub Objective: Calculating R-squared
Author: Saimadhu.Polamuri
Blog: https://dataaspirant.com
Date: 2020-10-14
===============================================
"""

## Requried Python Packages
import pandas as pd
import numpy as np


## Paths
data_path = "../data/sales_data.csv"

## UDF's Functions

## Residual sum of squares
def rss_value(actuals, forecasted):

    residuals = actuals - forecasted
    ## Squared each residual
    squared_residuals = [np.power(residual, 2) for residual in residuals]
    return sum(squared_residuals)


## Total sum of square
def tss_value(actuals):

    ## Calcuate mean
    actual_mean = actuals.mean()
    ## Squared mean difference value
    mean_difference_squared = [np.power(
    (actual - actual_mean), 2) for actual in actuals]
    return sum(mean_difference_squared)


## R-squared value
def get_r_squared_value(actuals, forecasted):

    rss = rss_value(actuals, forecasted)
    tss = tss_value(actuals)
    ## Calculating R-squared value
    r_squared_value = 1 - (rss/float(tss))
    return round(r_squared_value, 2)


def main():

    ## Load dataset
    data = pd.read_csv(data_path)
    # print(data.head())

    ## Calculating residual squared value
    rss = rss_value(data["sales"], data["dummy_forecasted_sales"])
    print("Calculated residual sum of squares :: {}".format(rss))

    ## Calculating total squared value
    tss = tss_value(data["sales"])
    print("Calculated total sum of squares value :: {}".format(tss))

    ## Calculating R-Squared value
    r_squared_value = get_r_squared_value(data["sales"],
    data["dummy_forecasted_sales"])
    print("Calculated R Squared Value :: {}".format(r_squared_value))


if __name__ == "__main__":
    main()

## Output
"""
Calculated residual sum of squares :: 189
Calculated total sum of squares value :: 1704.4
Calculated R Squared Value :: 0.89
"""

## dataaspirant-r-squared-calculation.py
