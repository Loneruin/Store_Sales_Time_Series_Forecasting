# import adfuller
from statsmodels.tsa.stattools import adfuller
# Create a function 'ADF_Stationarity_Test with the input parameters 'timeseries' and 'significance_level':
def ADF_Stationarity_Test(timeseries, significance_level=0.05):
    # run ADF test
    adf_test = adfuller(timeseries, autolag='AIC')

    # print results
    print('ADF Statistic: %f' % adf_test[0])
    print('p-value: %f' % adf_test[1])
    print('Critical Values:')
    for key, value in adf_test[4].items():
        print('\t%s: %.3f' % (key, value))
    
    # check if p-value is less than significance level
    if adf_test[1] <= significance_level:
        print("The time series is likely stationary.", significance_level)
    else:
        print("The time series is likely non-stationary.", significance_level)