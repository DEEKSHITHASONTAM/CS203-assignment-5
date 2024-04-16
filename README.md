# Bayesian Inference with Beta Distribution

This Python code demonstrates Bayesian inference using the Beta distribution. We use Bayesian updating to estimate the probability of getting heads in a coin toss based on prior and observed data.

## Requirements

- Python 3.x
- NumPy
- Matplotlib
- SciPy

## Installation

You can install the required packages using pip:

```bash
pip install numpy matplotlib scipy
```
## Code Explanation

### Observations

- `heads = 6`: Number of observed heads
- `tails = 4`: Number of observed tails

### Prior Parameters

We use different prior parameters for each case:

- **Case 1**: `alpha_prior = 2`, `beta_prior = 5`
- **Case 2**: `alpha_prior = 5`, `beta_prior = 2`
- **Case 3**: `alpha_prior = 1`, `beta_prior = 1`
- **Case 4**: `alpha_prior = 2`, `beta_prior = 2`

### Posterior Parameters

The posterior parameters are calculated using Bayesian updating:

```python
alpha_posterior = alpha_prior + heads
beta_posterior = beta_prior + tails
```
### Maximum Likelihood Estimate (MLE) and Maximum A Posteriori (MAP)

We also calculate MLE and MAP estimates for each case:

- **MLE**: `heads / (heads + tails)`
- **MAP**: `(alpha_posterior - 1) / (alpha_posterior + beta_posterior - 2)`

### Plotting

We plot the posterior distribution along with MLE and MAP estimates for each case using Matplotlib.

## Running the Code

To run the code, simply execute the Python script:

```bash
python bayesian_inference.py
```
## Results 
After running the code, you will see plots displaying the posterior distributions and estimates for each case:
* Case 1:Beta(2,5)
* Case 2:Beta(5,2)
* Case 3:Beta(1,1)
* Case 4:Beta(2,2)
  
  Each PLot includes:
  * Posterior Distribution
  * Maximum Likelihood Estimate (MLE)
  * Maximum A Posteriori (MAP) Estimate

