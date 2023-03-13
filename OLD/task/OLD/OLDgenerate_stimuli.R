# I want to generate 400 unique stimuli. Each stimulus is a cluster of 100 red and green balls, evenly spaced over a circular space.
# The 100 balls should be 54-46 in favor of either red or green.

rm(list=ls())
library(ggplot2)
set.seed(1337)

# number of dots
N <- 100

# distance between dots
sep <- .01

# sample a dot
make_dot <- function() {
  r <- runif(1,0,1)
  theta <- 2*pi*runif(1,0,1)
  newdot <- data.frame(
    x = r*cos(theta),
    y = r*sin(theta)
  )
  return(newdot)
}

# check if dot is far away enough
bad_dot <- function(dots, newdot) {
  any_bad <- F
  for (i in c(1:length(dots$x))) {
    if ( abs(dots$x[i]-newdot[1])<sep | abs(dots$y[i]-newdot[2])<sep ) {any_bad <- T}
  }
  return(any_bad)
}

# sample the first dot
dots <- data.frame()
dots[1,c('x','y')] <- make_dot()

# sample the rest of the dots
for (n in c(2:N)) {
  newdot <- make_dot()
  break_counter <- 0
  while (bad_dot(dots, newdot)) {
    newdot <- make_dot()
    break_counter <- break_counter + 1
    if (break_counter > 1000) {
      stop("Need a smaller distance between dots.")
    }
  }
  dots[n,c('x','y')] <- newdot
}

# plot
stimulus <- 
  
  ggplot(data=dots, aes(x=x, y=y)) +
  
  geom_circle(
    aes(x0=0, y0=0, r=1.06), 
    inherit.aes=F,
    size=1.5,
    color='lightgrey'
  ) +
  
  geom_point(
    size = 1
  ) +
  
  coord_fixed() +
  theme_classic() 
  # theme(
  #   axis.line = element_blank(),
  #   axis.title = element_blank(),
  #   axis.ticks = element_blank(),
  #   axis.text = element_blank()
  # )

plot(stimulus)