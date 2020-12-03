# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 16:24:35 2020

@author: Märten Mikk
"""
import numpy as np
import numpy.linalg 
import scipy

def matrix():
    """
    Parameters
    ----------
    MatA : Matrix A
    ----------
    Returns Matrix A. Cannot input as fraction. Eg, insert 3/5 as 0.6. 
    I might some day add the fraction thing. Couldn't be bothered righ now. 
    Might get a little bit inaccuracy if operating with fractions. Most functions round to 
    5 decimal places.
    To define a matrix write into the console the following Matrix_Name = matrix()
    and follow the questions.
    """
    r = int(input("no of rows?  "))
    c = int(input("no of colums?  "))
    MatA = np.zeros((r,c))
    for i in range(r):
        for y in range(c):
            MatA[i][y]= float(input("insert elemnt in row {} and column {}   ".format(i+1,y+1)))
    return MatA
             
def transpose(MatA):
    """
    Parameters
    ----------
    MatA : Matrix A
    ----------
    Returns transpose of Matrix A. Define the matrix first usinf function matrix()
    """
    return MatA.transpose()

def inverse(MatA):
    """
    Parameters
    ----------
    MatA : Matrix A
    ----------
    Returns inverse of Matrix A. Define the matrix first usinf function matrix()
    """
    return (np.linalg.inv(MatA)).round(5)

def det(MatA):
    """
    Parameters
    ----------
    MatA : Matrix A
    ----------
    Returns determinant of Matrix A. Define the matrix first usinf function matrix()
    """
    return np.linalg.det((MatA)).round(5)

def minor_of_element(A,i,j):
    """
    Parameters
    ----------
    MatA : Matrix A
    ----------
    Returns minor of matrix A in given posistion. Only works if rows, columns = 3. 
    Will fix this later!
    Last 2 dimensions of the array must be square
    """
    sub_A = np.delete(A,i-1,0)     
    M_ij = np.linalg.det(sub_A)    
    return np.around(M_ij,decimals=5)

def cofactor(A):
    """
    Parameters
    ----------
    MatA : Matrix A
    ----------
    Returns cofactor matrix for matrix A
    Only works if rows, columns = 3. 
    Will fix this later!
    """
    m = np.shape(A)[0]   
    C_A = np.zeros([m,m])   
    for i in range(1,m+1):
        for j in range(1,m+1):
            C_A[i-1,j-1] = pow(-1,i+j) * minor_of_element(A,i,j)
    return C_A

def multiply(MatA,MatB):
    """
    Parameters
    ----------
    MatA : Matrix A
    MatB : Matrix B
    ----------
    Returns Matrix AB
    """
    return (MatA.dot(MatB))

def add(MatA, MatB):
    """
    Parameters
    ----------
    MatA : Matrix A
    MatB : Matrix B
    ----------
    Returns Matrix A + B
    """
    return (MatA + MatB).round(6)

def solve(MatA, b):
    """
    Parameters
    ----------
    MatA : Matrix A (coefficents of linear equation system)
    MatB : b 
    ----------
    Returns solutions to linear equation system in the form MatA * X = b, using matrixes
    """
    return scipy.linalg.solve(MatA, b)

