get_fractions <- function(m, n) {
  f <- seq(0, 1, 1/n)
  s <- seq(0, 1, 1/m)
  w <- c(f, s)
  w <- unique(sort(w, decreasing = TRUE))
  return(w)
}

