library(dplyr)
library(ggplot2)
library(ggforce)
library(beepr)

###########################################################################################################
## Things you can control.

setwd("D:/OneDrive - California Institute of Technology/PhD/Rangel Lab/2022-biased-priors/task") # set wd
seed <- 1337 # set the seed so you can generate the same stimuli every time
num_red <- 46 # the number of red balls (which also sets blue to 100 minus this number). see (*).
jitter_amt <- .03 # the amount to jitter the balls from their original sunflower layout
ball_size <- 1.4 # how big do you like your balls?
pixels <- 450 # how large do you want the picture to be?

# (*) Experiment has 400 trials, split into 4 blocks of 100 trials. We will repeat the same stimuli in 
# each block. There are 10 sanity check trials, 5 with 80-20 Blue-Red, and 5 with 20-80. There are 45
# 54-46 trials and 45 46-54 trials. These numbers can change, depending on the value of num_red you set.

###########################################################################################################

# make sure you generate the same stimuli every time you run this.

set.seed(seed)


# function that plot points in sunflower formation, making an even distribution of points in a circle
# (https://stackoverflow.com/questions/28567166/uniformly-distribute-x-points-inside-a-circle)

sunflower <- function(n, alpha = 2, geometry = c('planar','geodesic'), num_red = 46) {
  
  b <- round(alpha*sqrt(n))  # number of boundary points
  phi <- (sqrt(5)+1)/2  # golden ratio
  
  r <- radius(1:n,n,b)
  theta <- 1:n * ifelse(geometry[1] == 'geodesic', 360*phi, 2*pi/phi^2)
  
  data <- 
    data.frame(
    x = r*cos(theta),
    y = r*sin(theta)
  )
  
  data$red <- factor(
    sample(
      c(
        rep(0,100-num_red), 
        rep(1,num_red) 
      )
    )
  )
  
  return(data)
  
}


# function to get vector of radii

radius <- function(k,n,b) {
  ifelse(
    k > n-b,
    1,
    sqrt(k-1/2)/sqrt(n-(b+1)/2)
  )
}


# function that generates points, plots, and saves in stimulus folder

make_stimuli <- function(num_red = 46, name = 'name_me') {
  
  pdata <- sunflower(100, 2, 'planar', num_red=num_red)
    
  p.stimulus <- 
    ggplot(data=pdata, aes(x=x, y=y, color=red)) +
    
    geom_circle(
      aes(x0=0, y0=0, r=1.11), 
      inherit.aes=F,
      size=1,
      color='grey94'
    ) +
    
    geom_jitter(
      width=jitter_amt, 
      height=jitter_amt,
      size=ball_size
    ) +
    scale_color_manual(
      #breaks=c("0", "1"),
      values=c("0"="#00BFC4", "1"="#F8766D") #blue,red
    ) +
    
    coord_fixed() +
    theme_classic() +
    theme(
      legend.position = 'none',
      axis.line = element_blank(),
      axis.title = element_blank(),
      axis.ticks = element_blank(),
      axis.text = element_blank()
    )
  
  ggsave(
    filename=name, 
    plot=p.stimulus,
    width=pixels,
    height=pixels,
    units="px"
  )
  
}


# Use the functions above to make stimuli based on the conditions.

## 54-46 Blue-Red
stim_num <- 1
for (i in c(1:45)) {
  name <- paste0("img/blue", toString(stim_num), ".png")
  make_stimuli(num_red=num_red, name=name)
  stim_num <- stim_num + 1
}

## 46-54 Blue-Red
num_red <- 100-num_red
stim_num <- 1
for (i in c(1:45)) {
  name <- paste0("img/red", toString(stim_num), ".png")
  make_stimuli(num_red=num_red, name=name)
  stim_num <- stim_num + 1
}

## 80-20 Blue-Red
num_red <- 20
stim_num <- 1
for (i in c(1:5)) {
  name <- paste0("img/sanityblue", toString(stim_num), ".png")
  make_stimuli(num_red=num_red, name=name)
  stim_num <- stim_num + 1
}

## 20-80 Blue-Red
num_red <- 80
stim_num <- 1
for (i in c(1:5)) {
  name <- paste0("img/sanityred", toString(stim_num), ".png")
  make_stimuli(num_red=num_red, name=name)
  stim_num <- stim_num + 1
}

# Make a visual mask
pdata <- sunflower(100, 1, 'planar', num_red=num_red)

p.stimulus <- 
  ggplot(data=pdata, aes(x=x, y=y)) +
  
  geom_circle(
    aes(x0=0, y0=0, r=1.11), 
    inherit.aes=F,
    size=1,
    color='grey94'
  ) +
  
  geom_jitter(
    width=0, 
    height=0,
    size=ball_size+.1
  ) +
  
  coord_fixed() +
  theme_classic() +
  theme(
    legend.position = 'none',
    axis.line = element_blank(),
    axis.title = element_blank(),
    axis.ticks = element_blank(),
    axis.text = element_blank()
  )

ggsave(
  filename="img/mask.png", 
  plot=p.stimulus,
  width=pixels,
  height=pixels,
  units="px"
)

# Make red and blue balls for response screen
pdata <- data.frame(x=0, y=0)

p.stimulus <- 
  ggplot(data=pdata, aes(x=x, y=y)) +
  
  geom_point(
    size=20,
    color="#00BFC4"
  ) +
  
  coord_fixed() +
  theme_classic() +
  theme(
    legend.position = 'none',
    axis.line = element_blank(),
    axis.title = element_blank(),
    axis.ticks = element_blank(),
    axis.text = element_blank()
  )

ggsave(
  filename="img/blueResponse.png", 
  plot=p.stimulus,
  width=pixels,
  height=pixels,
  units="px"
)

p.stimulus <- 
  ggplot(data=pdata, aes(x=x, y=y)) +
  
  geom_point(
    size=20,
    color="#F8766D"
  ) +
  
  coord_fixed() +
  theme_classic() +
  theme(
    legend.position = 'none',
    axis.line = element_blank(),
    axis.title = element_blank(),
    axis.ticks = element_blank(),
    axis.text = element_blank()
  )

ggsave(
  filename="img/redResponse.png", 
  plot=p.stimulus,
  width=pixels,
  height=pixels,
  units="px"
)

# ping when done
beep()
