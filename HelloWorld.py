import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
def grid():
    xgrid = [1,1,1,0,3,2,2,2,2,0,3]
    ygrid = [3,0,1,1,1,1,3,0,2,2,2]
    arr = np.random.normal(1, 1, size=100)
    fig, ax = plt.subplots()
    ax.plot(xgrid,ygrid)
    return fig
def cross(x,y):
    xcross = [x-0.45,x+0.45,x,x+0.45,x-0.45]
    ycross = [y+0.45,y-0.45,y,y+0.45,y-0.45]
    arr = np.random.normal(1, 1, size=100)
    fig, ax = plt.subplots()
    ax.plot(xcross,ycross)
    return fig
figg = grid()
figc = cross(1.5,1.5)
st.pyplot(figg)
st.pyplot(figc)


