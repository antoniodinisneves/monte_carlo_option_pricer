import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Pool, cpu_count

# --- Parameters for the simulation ---
drift = 0.07                  # Expected annual return of the stock
volatility = 0.01549          # Daily volatility of returns
time_increment = 1 / 252      # Time step (1 trading day out of 252 per year)
trading_days = 252            # Number of trading days to simulate
num_simulations = 1_000       # Number of Monte Carlo simulations to run
initial_price = 100           # Starting stock price

# --- Function to simulate a single price path ---
def simulate_path(initial_price):
    """
    Simulates a single stock price path using Geometric Brownian Motion (GBM).

    Parameters:
        initial_price (float): The starting stock price.
    Returns:
        list: Simulated daily stock prices over the specified period.
    """

    share_price = [initial_price] # Start with the initial stock price
    for i in range(trading_days):
        rand_num = np.random.normal(0,1) # Generate a random shock from a standard normal distribution
        exponent = (drift-0.5*volatility**2)*time_increment + volatility*((time_increment)**0.5)*rand_num

        # Update the price for this day
        new_price = share_price[-1]*np.exp(exponent)
        share_price.append(new_price)

    return share_price

# --- Main program ---
if __name__ == '__main__':
    # Use all CPU cores to run multiple simulations in parallel
    with Pool(cpu_count()) as pool:
        results = pool.map(simulate_path, [initial_price] * num_simulations)

    # Plot all simulated price paths
    for path in results:
        plt.plot(path)
    
    plt.title("Monte Carlo Simulated Stock Price Paths")
    plt.xlabel("Days")
    plt.ylabel("Price")
    plt.show()

    # Collect only the final prices from each simulation
    final_prices = [path[-1] for path in results]

    # Plot histogram of final prices to see the probability distribution
    plt.hist(final_prices, bins=100, density=True)
    plt.xlabel('Final Stock Price')
    plt.ylabel('Probability Density')
    plt.title('Distribution of Final Simulated Prices')
    plt.show()


