import numpy as np
import matplotlib.pyplot as plt

def step_plot(data, n, xlabel='Sample', ylabel='Amplitude', title='Graph of Combinated Signal'):
    # Step plot
    x_values = np.arange(len(data) + 1) / n
    y_values = np.repeat(data, 2)
    x_step = np.repeat(x_values, 2)[1:-1]

    fig, ax = plt.subplots(figsize=(18, 3))
    ax.step(x_step, y_values, where='post', linewidth=2)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.grid(True)

    plt.close(fig)

    return fig


def binary_plot(data, xlabel='Sample', ylabel='Amplitude', title='Graph of Binary Signal'):
    # Step plot
    x_values = np.arange(len(data) + 1)
    y_values = np.repeat(data, 2)
    x_step = np.repeat(x_values, 2)[1:-1]

    fig, ax = plt.subplots(figsize=(18, 3))
    ax.step(x_step, y_values, where='post', linewidth=2)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    
    ax.set_ylim(-0.1, 1.1) 
    ax.set_yticks([0, 1])   
    ax.grid(True)

    plt.close(fig)

    return fig
