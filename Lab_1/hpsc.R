# Load necessary libraries
library(Matrix)

# Function for Dot Product
dot_product <- function(n) {
  a <- runif(n)
  b <- runif(n)
  
  # Dot product with for-loop
  start_time <- Sys.time()
  c <- sum(a * b)
  loop_time <- as.numeric(Sys.time() - start_time)
  cat("Result:", c, "\n")
  cat("Time using for-loop:", loop_time, "seconds\n")
  
  # Dot product with vectorization
  start_time <- Sys.time()
  cc <- sum(a * b)
  vec_time <- as.numeric(Sys.time() - start_time)
  cat("Result (vectorized):", cc, "\n")
  cat("Time using vectorization:", vec_time, "seconds\n")
  
  # Compare results and measure speed-up
  cat("Norm of difference:", norm(c - cc), "\n")
  cat("Speed-up:", loop_time / vec_time, "\n")
}

# Function for Matrix-Vector Product
matrix_vector_product <- function(n) {
  A <- matrix(runif(n^2), ncol = n)
  x <- runif(n)
  
  # Matrix-Vector product with nested loops
  start_time <- Sys.time()
  b <- numeric(n)
  for (i in 1:n) {
    for (j in 1:n) {
      b[i] <- b[i] + A[i, j] * x[j]
    }
  }
  loop_time <- as.numeric(Sys.time() - start_time)
  cat("Result:", b, "\n")
  cat("Time using nested loops:", loop_time, "seconds\n")
  
  # Matrix-Vector product with vectorization
  start_time <- Sys.time()
  bb <- A %*% x
  loop_vec_time <- as.numeric(Sys.time() - start_time)
  cat("Result (vectorized):", bb, "\n")
  cat("Time using vectorization:", loop_vec_time, "seconds\n")
  
  # Matrix-Vector product with full vectorization
  start_time <- Sys.time()
  bbb <- A %*% x
  vec_time <- as.numeric(Sys.time() - start_time)
  cat("Result (fully vectorized):", bbb, "\n")
  cat("Time using full vectorization:", vec_time, "seconds\n")
  
  # Compare results and measure speed-up
  cat("Norm of difference (nested loops vs vectorized loop):", norm(b - bb), "\n")
  cat("Norm of difference (nested loops vs fully vectorized):", norm(b - bbb), "\n")
  cat("Speed-up (nested loops vs vectorized loop):", loop_time / loop_vec_time, "\n")
  cat("Speed-up (nested loops vs fully vectorized):", loop_time / vec_time, "\n")
  cat("Speed-up (vectorized loop vs fully vectorized):", loop_vec_time / vec_time, "\n")
}

# Function for Matrix-Matrix Product
matrix_matrix_product <- function(n) {
  A <- matrix(runif(n^2), ncol = n)
  B <- matrix(runif(n^2), ncol = n)
  
  # Matrix-Matrix product with triple nested loops
  start_time <- Sys.time()
  C <- matrix(0, nrow = n, ncol = n)
  for (i in 1:n) {
    for (j in 1:n) {
      for (k in 1:n) {
        C[i, j] <- C[i, j] + A[i, k] * B[k, j]
      }
    }
  }
  loop_time <- as.numeric(Sys.time() - start_time)
  cat("Result (nested loops):", C, "\n")
  cat("Time using triple nested loops:", loop_time, "seconds\n")
  
  # Matrix-Matrix product with single loop and vectorization
  start_time <- Sys.time()
  CC <- matrix(0, nrow = n, ncol = n)
  for (i in 1:n) {
    CC[, i] <- A %*% B[, i]
  }
  loop_vec_time <- as.numeric(Sys.time() - start_time)
  cat("Result (vectorized loop):", CC, "\n")
  cat("Time using vectorization in loop:", loop_vec_time, "seconds\n")
  
  # Matrix-Matrix product with full vectorization
  start_time <- Sys.time()
  CCC <- A %*% B
  vec_time <- as.numeric(Sys.time() - start_time)
  cat("Result (fully vectorized):", CCC, "\n")
  cat("Time using full vectorization:", vec_time, "seconds\n")
  
  # Compare results and measure speed-up
  cat("Norm of difference (nested loops vs vectorized loop):", norm(C - CC), "\n")
  cat("Norm of difference (nested loops vs fully vectorized):", norm(C - CCC), "\n")
  cat("Speed-up (nested loops vs vectorized loop):", loop_time / loop_vec_time, "\n")
  cat("Speed-up (nested loops vs fully vectorized):", loop_time / vec_time, "\n")
  cat("Speed-up (vectorized loop vs fully vectorized):", loop_vec_time / vec_time, "\n")
}

# Choose which function to run
choose_function <- function() {
  cat("Choose a function to run:\n")
  cat("1. Dot Product\n")
  cat("2. Matrix-Vector Product\n")
  cat("3. Matrix-Matrix Product\n")
  choice <- as.numeric(readline("Enter 1, 2, or 3: "))
  #choice <- as.numeric(readline("Enter 1, 2, or 3: "))
  choice <- 1
  
  for (ns_value in c(10110, 101, 50001)) {
    if (choice == 1) {
      cat("\nDot Product with νs =", ns_value, "\n")
      dot_product(ns_value)
    } else if (choice == 2) {
      cat("\nMatrix-Vector Product with νs =", ns_value, "\n")
      matrix_vector_product(ns_value)
    } else if (choice == 3) {
      cat("\nMatrix-Matrix Product with νs =", ns_value, "\n")
      matrix_matrix_product(ns_value)
    } else {
      cat("Invalid choice. Please enter 1, 2, or 3.\n")
    }
  }
}

# Run the chosen function
choose_function()

