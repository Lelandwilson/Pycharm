from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import pearsonr
from scipy.stats import spearmanr
from scipy.optimize import fsolve

# turn off annoying warning
import warnings
from sklearn.exceptions import DataConversionWarning
warnings.filterwarnings(action='ignore', category=FutureWarning)


if __name__ == '__main__':
    print("<Init>")
    # ------------------ Method 2 ---------------#
    force = [11.4, 18.7, 11.7, 12.3, 14.7, 18.8, 19.6]
    time = [0.56, 0.35, 0.55, 0.52, 0.43, 0.34, 0.31]

    sumX = sum(force)
    sumY = sum(time)
    sumXsq = sum(np.square(force))
    sumYsq = sum(np.square(time))
    sumXY = sum(np.array(force) * np.array(time))

    print(sumX)
    print(sumY)
    print(sumXsq)
    print(sumYsq)
    print(sumXY)



    def myfunc(a):
        return [len(force)*a[0] + sumX*a[1] - sumY, sumX*a[0] + sumXsq*a[1] - sumXY]

    z = fsolve(myfunc, [1,1])
    print("Answer: " + str(z))
    print("Coefficient = %.3f, intercept = %.4f" % (z[0], z[1]))
    print("Hence the eq. of the regression line of Y on X is: Y = a0 + a1X = %.3f - %.4fX" % (z[0], z[1]))

    plt.plot(force, time, 'ro')
    plt.xlabel('force')
    plt.ylabel('time')
    plt.show()

    x_reg = []
    y_reg = []

    for i in np.linspace(10,20, 10000):
        x_reg.append(i)
        y_reg.append(z[1]* i + z[0])

    plt.plot(x_reg, y_reg)
    plt.scatter(force,time, c='r')
    plt.show()

    #------------------ Method 1 ---------------#

    # Below is method 1 for Problem 6, tutorial 10
    #
    # force = [11.4, 18.7, 11.7, 12.3, 14.7, 18.6, 19.6] # force values from question
    # time = [0.56, 0.35, 0.55, 0.52, 0.43, 0.34, 0.31] # time values from question
    #
    # # Create a zipped lisyt of tuples from above list
    # zippedList = list(zip(force, time))
    # print(zippedList)
    #
    # # Crete a dataFrame from zipped list
    # df = pd.DataFrame(zippedList, columns=['force', 'time'])
    # print(df)
    #
    # X=df['force'].values.reshape(-1,1)
    # print(X)
    #
    # # Calc Pearson's correlation: used to summarize the strength of the linear relationship
    # # b/w the two samples
    # corr, _ = pearsonr(df['force'], df['time'])
    # print('Pearsons correlation: %.3f. This determines if the data does indeed have a linear correlation' % corr)
    #
    # y=df['time'] #.values.reshape(-1,1) ?? if not in matirx?
    # reg = LinearRegression().fit(X,y)
    # # print('Coefficient = %.4f' % reg.coef_[0])
    # # print('Intercept = %.4f' % reg.intercept_)
    #
    # print("\n")
    # print("Liner Regression score = " + str(reg.score(X, y)))
    #
    # print("Answer: [%.4f, %.4f]" % (reg.coef_[0], reg.intercept_))
    # print("Coefficient = %.4f, intercept = %.4f" % (reg.coef_[0], reg.intercept_))
    # print("Hence the eq. of the regression line of Y on X is: Y = a0 + a1X = %.4f - %.4fX" % (reg.coef_[0], reg.intercept_))
    #
    #
    #
    #
    # test=np.array([14.1])
    # test = test.reshape(-1, 1)
    # ## print(reg.predict(test))
    #
    # x_reg = []
    # y_reg = []
    #
    # for i in np.linspace(10,20,10000):
    #     x_reg.append(i)
    #     y_reg.append(reg.coef_[0] * i + reg.intercept_)
    #
    # plt.plot(x_reg, y_reg)
    # plt.scatter(X,y, c='r')
    # plt.show()
    #
    #


# --------- \/ not required \/ -------------#
    # MULTI LINEAR REGRESSION EXAMPLE #
    ## boston = load_boston()
    ## x = boston.data
    ## y = boston.target
    ## reg = LinearRegression().fit(x, y)
    ##
    ## print(reg.coef_)
    ## print(reg.intercept_)
    ## print("Liner Regression score = " + str(reg.score(x, y)))
    ##
    ## print(reg.predict([[0.03, 0, 3, 0, 0.5, 7, 50, 4, 7, 220, 19, 390, 5]]))
    ##
    ## pd.set_option('max_colwidth', 800) # to see more columns
    ##
    ## # create zipped list of tuples from above lists
    ## zippedList_boston = list(zip(x,y))
    ##
    ## #create a dataframe from zipped list
    ## df_boston = pd.DataFrame(zippedList_boston, columns= ['data', 'target'])
    ## df_boston.head()

    # --------- /\ not required /\ -------------#

