clear all; 
close all; % Start fresh

% Get the number of cores
numCores = feature('numcores');

% Create a parallel pool if none exists
if isempty(gcp('nocreate'))
    parpool('local', numCores);
end

% Organizing Inputs
f = @(x) sin(3*pi*cos(2*pi*x).*sin(pi*x));
a = -3; 
b = 5; 
n = 4^9;
x0 = linspace(a, b, n); % Vector containing initial starting points
q = zeros(size(x0)); % Preallocate a vector for storing roots.

% Timing the serial execution
tic
for i = 1:n
    q(i) = fzero(f, x0(i));
end
serialTime = toc;

% Parallel execution
tic
parfor i = 1:n
    q(i) = fzero(f, x0(i));
end
parallelTime = toc;

% Processing Outputs
q = unique(q); % Keep roots with unique values only.

% Calculate Speedup and Efficiency
speedup = serialTime / parallelTime;
efficiency = speedup / numCores;

% Display the results
disp("Using " + num2str(numCores) + " cores");
disp(['Serial Execution Time: ' num2str(serialTime) ' seconds']);
disp(['Parallel Execution Time: ' num2str(parallelTime) ' seconds']);
disp(['Speedup: ' num2str(speedup)]);
disp(['Efficiency: ' num2str(efficiency)]);

% Close the parallel pool
delete(gcp);
