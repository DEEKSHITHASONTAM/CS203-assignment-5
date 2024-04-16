import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

# Observations
heads = 6
tails = 4

# Prior parameters
alpha_prior = 2
beta_prior = 5

# Posterior parameters
alpha_posterior = alpha_prior + heads
beta_posterior = beta_prior + tails

# Generate values for x axis
x = np.linspace(0, 1, 1000)

# Calculate the posterior distribution
posterior_distribution = beta.pdf(x, alpha_posterior, beta_posterior) #probability density function

# Calculate Maximum Likelihood Estimate (MLE) and Maximum A Posteriori (MAP) estimates
mle = heads / (heads + tails)
map_estimate = (alpha_posterior - 1) / (alpha_posterior + beta_posterior - 2)

# Plot the posterior distribution
plt.figure(figsize=(10, 6))
plt.plot(x, posterior_distribution, label='Posterior Distribution')

# Plot the MLE and MAP estimates
plt.axvline(x=mle, color='r', linestyle='--', label='MLE')
plt.axvline(x=map_estimate, color='g', linestyle='--', label='MAP')

plt.title('Posterior Distribution for Case 1: Beta(2,5)')
plt.xlabel('Probability of Heads')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()

# Prior parameters for Case 2
alpha_prior = 5
beta_prior = 2

# Posterior parameters for Case 2
alpha_posterior_case2 = alpha_prior + heads
beta_posterior_case2 = beta_prior + tails

# Calculate the posterior distribution for Case 2
posterior_distribution_case2 = beta.pdf(x, alpha_posterior_case2, beta_posterior_case2)

# Calculate Maximum Likelihood Estimate (MLE) and Maximum A Posteriori (MAP) estimates for Case 2
mle_case2 = heads / (heads + tails)
map_estimate_case2 = (alpha_posterior_case2 - 1) / (alpha_posterior_case2 + beta_posterior_case2 - 2)

# Plot the posterior distribution for Case 2
plt.figure(figsize=(10, 6))
plt.plot(x, posterior_distribution_case2, label='Posterior Distribution')

# Plot the MLE and MAP estimates for Case 2
plt.axvline(x=mle_case2, color='r', linestyle='--', label='MLE')
plt.axvline(x=map_estimate_case2, color='g', linestyle='--', label='MAP')

plt.title('Posterior Distribution for Case 2: Beta(5,2)')
plt.xlabel('Probability of Heads')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()


# Prior parameters for Case 3
alpha_prior = 1
beta_prior = 1

# Posterior parameters for Case 3
alpha_posterior_case3 = alpha_prior + heads
beta_posterior_case3 = beta_prior + tails

# Calculate the posterior distribution for Case 3
posterior_distribution_case3 = beta.pdf(x, alpha_posterior_case3, beta_posterior_case3)

# Calculate Maximum Likelihood Estimate (MLE) and Maximum A Posteriori (MAP) estimates for Case 3
mle_case3 = heads / (heads + tails)
map_estimate_case3 = (alpha_posterior_case3 - 1) / (alpha_posterior_case3 + beta_posterior_case3 - 2)

# Plot the posterior distribution for Case 3
plt.figure(figsize=(10, 6))
plt.plot(x, posterior_distribution_case3, label='Posterior Distribution')

# Plot the MLE and MAP estimates for Case 3
plt.axvline(x=mle_case3, color='r', linestyle='--', label='MLE')
plt.axvline(x=map_estimate_case3, color='g', linestyle='--', label='MAP')

plt.title('Posterior Distribution for Case 3: Beta(1,1)')
plt.xlabel('Probability of Heads')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()


# Prior parameters for Case 4
alpha_prior = 2
beta_prior = 2

# Posterior parameters for Case 4
alpha_posterior_case4 = alpha_prior + heads
beta_posterior_case4 = beta_prior + tails

# Calculate the posterior distribution for Case 4
posterior_distribution_case4 = beta.pdf(x, alpha_posterior_case4, beta_posterior_case4)

# Calculate Maximum Likelihood Estimate (MLE) and Maximum A Posteriori (MAP) estimates for Case 4
mle_case4 = heads / (heads + tails)
map_estimate_case4 = (alpha_posterior_case4 - 1) / (alpha_posterior_case4 + beta_posterior_case4 - 2)

# Plot the posterior distribution for Case 4
plt.figure(figsize=(10, 6))
plt.plot(x, posterior_distribution_case4, label='Posterior Distribution')

# Plot the MLE and MAP estimates for Case 4
plt.axvline(x=mle_case4, color='r', linestyle='--', label='MLE')
plt.axvline(x=map_estimate_case4, color='g', linestyle='--', label='MAP')

plt.title('Posterior Distribution for Case 4: Beta(2,2)')
plt.xlabel('Probability of Heads')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
