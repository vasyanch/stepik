# имитация игрального кубика
dice_roll <- function(n){
  return (floor(runif(n, min=0, max=6)) + 1) 
}
