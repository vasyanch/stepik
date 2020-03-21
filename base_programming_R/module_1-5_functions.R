y <- vector(mode="character", length = 100)
y <- character(100)
for (i in 1:100) {
  if (i %% 15 == 0) {
    y[i] <- "fizz buzz"
  } else if (i %% 3 == 0) {
    y[i] <- "fizz"
  } else if (i %% 5 == 0) {
    y[i] <- "buzz"
  } else {
    y[i] <- i
  }
}
y

# fizz-buzz, vector-oriented stale
x <- 1:100
z <- 1:100

x %% 5 == 0
z[x %% 5 == 0] <- "buzz"
z[x %% 3 == 0] <- "fizz"
z[x %% 15 ==0] <- "fizz buzz"
all(y == z)


#Geometric progression
f <- 2 ^(0:10)
f
log2(f)
set.seed(42)
x <- sample(1:100, 50)

#Neigbors with greatest dff
x
x[-1]
x[-length(x)]
x[-1] - x[-length(x)]
k <- which.max(abs(x[-1] -x[-length(x)]))
x[c(k, k + 1)]

# Multiple min/max
x <- sample(1:100, 50, replace = TRUE)
x
min(x)
which.min(x)
which(x == min(x))
max(x)
which(x == max(x))

#Packing into a function
maxdiff <- function(x) {
  y <- abs(x[-1] - x[-length(x)])
  k <- which(y == max(y))
  print("first neighbor(s):")
  print(x[k])
  print("second neighbor(s):")
  print(x[k + 1])
  print("maximum absolute diff is:")
  print(max(y))
}

xx <- sample(1:100, 1e4, replace = TRUE)
maxdiff(xx)
