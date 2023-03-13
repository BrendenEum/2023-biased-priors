########################################################################
## Preamble

set.seed(4)

########################################################################
## Set magnitude and hyperpriors

x = 2.2
mu = 2
px = 1

########################################################################
## Function to calculate estimates

getEstimate <- function(x, mu, px, pr) {
  
  r = rnorm(1, x, 1/sqrt(pr))
  beta = pr / (px+pr)
  estimate = mu + beta*(r - mu)
  return(estimate)
  
}

########################################################################
## How do estimates vary with signal precision?

signal_precisions = c(0.1, 0.5, 1, 1.5, 2)
df = data.frame(pr = signal_precisions, estimate = signal_precisions)

I = 1
for (pr in signal_precisions) {
  
  df$pr[I] = pr
  df$estimate[I] = getEstimate(x, mu, px, pr)
  
}