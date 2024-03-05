library(rootSolve)
library(parallel)
library(ggplot2)

# Define the function
f <- function(x) {
  sin(3 * pi * cos(2 * pi * x) * sin(pi * x))
}

# Function to find roots using Newton's method
find_root_newton <- function(x) {
  tryCatch({
    root <- uniroot(f, c(x - 0.1, x + 0.1))
    return(root$root)
  }, error = function(e) {
    return(NULL)
  })
}

# Sequential solver
sequential_solver <- function(x_values) {
  roots <- sapply(x_values, find_root_newton)
  roots <- roots[!sapply(roots, is.null)]
  return(roots)
}

# Parallel worker function
parallel_worker <- function(start_idx, end_idx, x_values) {
  roots <- sapply(x_values[start_idx:end_idx], find_root_newton)
  roots <- roots[!sapply(roots, is.null)]
  return(roots)
}

# Function to plot roots and function
plot_roots_and_function <- function(xx, f_values, roots, title) {
  # Filter out non-numeric roots and convert to numeric
  numeric_roots <- as.numeric(roots[sapply(roots, is.numeric)])
  
  # Calculate function values for numeric roots
  f_numeric_roots <- f(numeric_roots)
  
  # Create a data frame with numeric roots and function values
  roots_df <- data.frame(xx = numeric_roots, f_values = f_numeric_roots)
  
  ggplot(data.frame(xx, f_values), aes(x = xx, y = f_values)) +
    geom_line(color = "black", size = 2, linetype = "solid") +
    geom_point(data = roots_df, aes(x = xx, y = f_values), 
               color = "red", size = 3, shape = 16) +
    xlim(min(xx), max(xx)) +
    ylim(-1, 1) +
    scale_y_continuous(breaks = c(-1, 0, 1)) +
    xlab("x") +
    ylab("f(x)") +
    theme_minimal() +
    ggtitle(title) +
    theme(legend.position = "bottom")
}

# Main script
a <- -1
b <- 1
n <- 1000
x_values <- seq(a, b, length.out = n)

# Sequential execution
S_time <- Sys.time()
seq_roots <- sequential_solver(x_values)
E_time <- Sys.time()
seq_time <- as.numeric(E_time - S_time, units = "secs")

# Parallel execution
N_cores <- detectCores()
C_size <- n %/% N_cores
proc <- vector("list", length = N_cores)

parallel_roots <- mclapply(1:N_cores, function(core) {
  S_idx <- (core - 1) * C_size + 1
  E_idx <- S_idx + C_size - 1
  parallel_worker(S_idx, E_idx, x_values)
}, mc.cores = N_cores)

parallel_roots <- unique(unlist(parallel_roots))
P_time <- as.numeric(Sys.time() - S_time, units = "secs")
S_up <- seq_time / P_time
effi <- S_up / N_cores

cat("Speed up: ", S_up, "\n")
cat("Efficiency: ", effi, "\n")

# Plot the function and roots
xx <- seq(a, b, length.out = 1001)
f_values <- f(xx)

# For sequential roots
plot_roots_and_function(xx, f_values, seq_roots, "Sequential_Roots")

# For parallel roots
plot_roots_and_function(xx, f_values, parallel_roots, "Parallel_Roots")
