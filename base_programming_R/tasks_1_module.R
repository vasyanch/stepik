is_monotone <- function(x) {
  k <- x[-1] - x[-length(x)]
  return(all(k >= 0) | all(k <= 0))
}

combin_count <- function(n, k, with_repetitions=FALSE) {
  if (with_repetitions) {
    return (factorial(n + k - 1) / (factorial(k) * factorial(n - 1)))
  } else {
    return (factorial(n) / (factorial(k) * factorial(n - k)))
  }
}

combin_count <- function(n, k, with_repetitions = FALSE) {
  prod( if( with_repetitions) (k+1):(n+k-1)/1:(n-1) else (k+1):n/1:(n-k))
}