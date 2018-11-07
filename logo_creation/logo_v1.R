rm(list = ls())

VERSION <- 'logo_v1'

add_branch <- function(r, x0, y0, theta0=0) {
  theta <- c(3*pi/4, pi/2, pi/4) + theta0
  y <- y0 + r*sin(theta)
  x <- x0 + r*cos(theta)  
  points(x, y, pch=16)
  for (i in 1:length(x)) {
    lines(c(x0, x[i]), c(y0, y[i]))
  }
}

png(sprintf('figures/%s.png', VERSION))
par(pty='s')
plot(c(0, 0), c(0, 3), type='l')
points(rep(0, 4), 0:3, pch=16)

add_branch(1, 0, 1, 0)
add_branch(1, 0, 2, 0)
dev.off()
