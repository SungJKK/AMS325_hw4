# AMS 325 - Homework 4 
Repository for homework 4, AMS 325 class (SBU).

### Files
`mandelbrot.py`: contains function to compute [Mandelbrot sets](https://en.wikipedia.org/wiki/Mandelbrot_set) that iterates starting from z = 0, and saves the Mandelbrot Fractal graph into `mandelbrot.png` file. Function takes 3 arguments: `n`, `N_max`, and `threshold`.
- `n`: number of (x, y) points to generate
- `N_max = 50`: maximum number of Mandelbrot iterations
- `threshold = 50`: value to determine whether the point is included in the Mandelbrot set

<br/>

`markov_chain.py`: contains function to compute [Markov chains](https://en.wikipedia.org/wiki/Markov_chain), and saves a graph comparing norm and the number of iterations into `markov.png` file. Function takes 2 arguments: `n` and `N`.
- `n = 5`: size of the initial n-vector and n x n matrix
- `N = 50`: number of transition steps to iterate

### How to run 
Pull the repository to an empty folder 
```sh
$ mkdir hw4 && cd hw4
$ git init .
$ git pull https://github.com/SungJKK/AMS325_hw4.git
```

---
They depend on the packages Numpy and Matplotlib.  
Either install them according to your environment
or use poetry.  
```sh
$ poetry install 
```

---
Go into the virtual environment and run each file.
```sh
$ poetry shell
$ python mandelbrot.py
$ python markov_chain.py
```


### Author
Sung Joong Kim




