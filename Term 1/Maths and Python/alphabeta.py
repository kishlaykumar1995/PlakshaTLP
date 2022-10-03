import numpy as np
def calc_error(actual, predicted):
    error = 0.0
    for i,j in list(zip(actual, predicted)):
        error+=(i-j)**2
    return np.sqrt(error)

def find_alpha_beta(mat, values, thresh=0.0):
    preds = [0,0]
    a_f,b_f = 0,0
    min_error = 100000
    for i in np.linspace(0,1,101):
        alpha = i
        beta = 1-i
        preds[0] = mat[0][0]*alpha + mat[0][1]*beta
        preds[1] = mat[1][0]*alpha + mat[1][1]*beta
        error = calc_error(values, preds)
        if error < min_error:
            a_f, b_f, min_error = alpha, beta, error
    print(a_f, b_f, min_error)

mat = [[23,84],[82,78]]
values = [70,39]
find_alpha_beta(mat,values)