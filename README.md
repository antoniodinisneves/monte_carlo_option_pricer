-Monte Carlo stock price simulation

This project simulates possible future stock price paths using Monte Carlo methods and Geometric Brownian Motion (GBM). It leverages Python multiprocessing to efficiently generate thousands of simulations in parallel, making the process significantly faster on multi-core machines.

-Overview
Stock prices are often modeled as a stochastic process due to their inherent randomness. One of the most widely used models is GBM, which assumes that stock prices evolve continuously with a drift (expected return) and a volatility (random fluctuation).

The stochastic differential equation (SDE) for GBM is:

𝑑
𝑆
𝑡
=
𝜇
𝑆
𝑡
 
𝑑
𝑡
+
𝜎
𝑆
𝑡
 
𝑑
𝑊
𝑡
dS 
t
​
 =μS 
t
​
 dt+σS 
t
​
 dW 
t
​
 
Where:

𝑆
𝑡
S 
t
​
  = Stock price at time 
𝑡
t

𝜇
μ = Expected return (drift)

𝜎
σ = Volatility

𝑑
𝑊
𝑡
dW 
t
​
  = Wiener process (Brownian motion) increment

The discretized solution used in this simulation is:

𝑆
𝑡
+
Δ
𝑡
=
𝑆
𝑡
⋅
exp
⁡
(
(
𝜇
−
1
2
𝜎
2
)
Δ
𝑡
+
𝜎
Δ
𝑡
 
𝑍
)
S 
t+Δt
​
 =S 
t
​
 ⋅exp((μ− 
2
1
​
 σ 
2
 )Δt+σ 
Δt
​
 Z)
Where 
𝑍
∼
𝑁
(
0
,
1
)
Z∼N(0,1) is a standard normal random variable.

-Efficiency via Multiprocessing
Running thousands of independent price path simulations can be computationally expensive. This project uses Python’s multiprocessing.Pool to distribute the workload across all available CPU cores, drastically reducing runtime.

-Features
Simulates multiple price paths using GBM dynamics

Produces both:

A line plot of simulated price trajectories

A histogram showing the distribution of final simulated prices

Parallelized computation for faster execution on multi-core processors

Well-documented code for readability and educational use
