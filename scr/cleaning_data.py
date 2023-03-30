# function to convert a column to string
def convert_to_string(df, col):
    df[col] = df[col].apply(str)
    return df

# test nomality of the distribution
from scipy.stats import shapiro
def test_normality(data):
    stat, p = shapiro(data)
    print('Statistics=%.3f, p=%.3f' % (stat, p))
    if p > 0.05:
        print('Sample looks normally distributed (fail to reject H0)')
    else:
        print('Sample does not look normally distributed (reject H0)')