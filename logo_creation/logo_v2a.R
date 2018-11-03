rm(list = ls())

VERSION <- 'logo_v2a'

add_branch <- function(r, x0, y0, theta0=0) {
  theta <- c(3*pi/4, pi/2, pi/4) + theta0
  y <- y0 + r*sin(theta)
  x <- x0 + r*cos(theta)
  for (i in 1:length(x)) {
    lines(c(x0, x[i]), c(y0, y[i]))
  }
}

png(sprintf('figures/%s.png', VERSION), 150, 150)
par(pty='s', bg=NA, lwd=10, cex=2.5, col=rgb(34/255,250/255,34/255), mar=rep(0.25, 4))
plot(c(0, 0), c(0, 3), type='l', #axes=F,
     xlab="", ylab="", xaxt='n', yaxt='n',
     xlim=c(-sqrt(2),sqrt(2)), ylim=c(-0.5,3.5))

add_branch(1, 0, 1, 0)
add_branch(1, 0, 2, 0)
dev.off()
