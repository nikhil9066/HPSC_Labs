library(future)
library(doParallel)
library(Sys.time)

simulate_task <- function(iterations) {
  for (j in seq_len(iterations)) {
    Sys.sleep(0.01)
  }
}

run_parallel_tasks <- function(num_tasks, num_threads) {
  start_time_single_task <- Sys.time()
  simulate_task(1)
  elapsed_time_single_task <- difftime(Sys.time(), start_time_single_task, units = "secs")
  
  start_time_parallel_tasks <- Sys.time()
  plan(multicore, workers = num_threads)
  futures <- future_lapply(seq_len(num_tasks), function(i) simulate_task(1))
  elapsed_time_parallel_tasks <- difftime(Sys.time(), start_time_parallel_tasks, units = "secs")
  
  speedup <- as.numeric(elapsed_time_single_task) / as.numeric(elapsed_time_parallel_tasks)
  efficiency <- speedup / num_tasks
  
  cat("\n")
  cat("Number of tasks: ", num_tasks, "\n")
  cat("Elapsed time for a single task: ", format(elapsed_time_single_task, digits = 3), " seconds\n")
  cat("Elapsed time for parallel tasks: ", format(elapsed_time_parallel_tasks, digits = 3), " seconds\n")
  cat("Speed up: ", format(speedup, digits = 2), "\n")
  cat("Efficiency: ", format(efficiency, digits = 2), "\n")
}

if (interactive()) {
  # Parallel tasks with 10 iterations and 4 threads
  run_parallel_tasks(10, 4)
  run_parallel_tasks(100, 4)
  run_parallel_tasks(1000, 4)
}

