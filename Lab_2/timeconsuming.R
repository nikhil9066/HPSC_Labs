library(parallel)
library(microbenchmark)

time_consuming_fun <- function() {
  pause_time <- runif(1, 1, 5)  # Random pause between 1 and 5 seconds
  Sys.sleep(pause_time)
}

run_experiment <- function(n) {
  serial_times <- microbenchmark(
    for (i in 1:n) time_consuming_fun(),
    times = 1
  )

  parallel_times <- microbenchmark(
    mclapply(1:n, function(i) time_consuming_fun(), mc.cores = detectCores()),
    times = 1
  )

  serial_time <- summary(serial_times)[, "median"]
  parallel_time <- summary(parallel_times)[, "median"]
  
  speedup <- serial_time / parallel_time
  efficiency <- speedup / detectCores()

  cat("Number of iterations:", n, "\n")
  cat("Serial time:", serial_time, "seconds\n")
  cat("Parallel time:", parallel_time, "seconds\n")
  cat("Speedup:", speedup, "\n")
  cat("Efficiency:", efficiency, "\n\n")
}

run_experiment(100)
run_experiment(1000)
run_experiment(10000)