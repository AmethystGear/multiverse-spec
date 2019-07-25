#!/usr/bin/env python3

import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn import linear_model

if __name__ == '__main__':
    # read data file
    df = pd.read_csv('data.csv')

    # discard rows outside multiples of std
    df = df[np.abs(df.y - df.y.mean()) <= (2.5 * df.y.std())]

    x = sm.add_constant(df.x)
    lm = sm.OLS(df.y, x).fit()

    # display results
    print('Fitted using statsmodels')
    print('y = {:.2f} + {:.2f} * x'.format(lm.params.const, lm.params.x))
    print('R squared: {:.2f}'.format(lm.rsquared))
