import numpy as np
import matplotlib.pyplot as plt

def markov(n:int = 5, N:int = 50):
    # Generate n-vector w/ non-negative entries
    p = np.random.rand(n)

    # Scale so that the sum equals to 1
    # This gives the probability distribution, p
    p = p / p.sum()

    # Generate n x n matrix w/ non-negative entries 
    P = np.random.rand(n, n)

    # Scale so that the sum in each row is 1
    # This gives the transition matrix, P
    for i in range(n):
        P[i,:] = P[i,:] / P[i,:].sum()

    # Compute transition (p <- P^T*p) for N steps
    for i in range(N):
        p = P.T * p

        # Compute largest eigenvalue, and then scale it so that the sum is equal to 1
        eig = np.linalg.eig(P.T)
        pos = np.argmax(eig[0])
        p_stationary = eig[1][:, pos]
        p_stationary = p_stationary / p_stationary.sum()

        # Compute the norm of p - p_stationary 
        norm = np.linalg.norm(p - p_stationary)

        # Plot the point 
        plt.plot(norm, i, color = 'red', marker = 'o')

    # Save the plot into a figure
    plt.xlabel('Norms')
    plt.ylabel('Iterations (i)')
    plt.savefig('./markov.png')


if __name__ == '__main__':
    # markov(1, 100)
    # markov(3, 100)
    markov(5, 50)
    # markov(5, 100)
    # markov(10, 100)



