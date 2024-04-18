% Scenario 1: CPU, single precision
A_single = single(rand(2000,2000)); % Create a single precision random matrix
b_single = single(rand(2000,1)); % Create a single precision random vector
tic; % Start timer
for i = 1:20000
    y = A_single * b_single; % Matrix-vector multiplication
end
time_cpu_single = toc; % Stop timer and record time

% Scenario 2: CPU, double precision
A_double = double(rand(2000,2000)); % Create a double precision random matrix
b_double = double(rand(2000,1)); % Create a double precision random vector
tic; % Start timer
for i = 1:20000
    y = A_double * b_double; % Matrix-vector multiplication
end
time_cpu_double = toc; % Stop timer and record time

% Check if GPU is available
if gpuDeviceCount > 0
    % Scenario 3: GPU, single precision
    A_gpu_single = gpuArray(single(rand(2000,2000))); % Create a single precision random matrix on GPU
    b_gpu_single = gpuArray(single(rand(2000,1))); % Create a single precision random vector on GPU
    tic; % Start timer
    for i = 1:20000
        y = A_gpu_single * b_gpu_single; % Matrix-vector multiplication on GPU
    end
    time_gpu_single = toc; % Stop timer and record time

    % Scenario 4: GPU, double precision
    A_gpu_double = gpuArray(double(rand(2000,2000))); % Create a double precision random matrix on GPU
    b_gpu_double = gpuArray(double(rand(2000,1))); % Create a double precision random vector on GPU
    tic; % Start timer
    for i = 1:20000
        y = A_gpu_double * b_gpu_double; % Matrix-vector multiplication on GPU
    end
    time_gpu_double = toc; % Stop timer and record time
else
    disp('GPU is not available on this system.');
    time_gpu_single = NaN;
    time_gpu_double = NaN;
end

% Display times
fprintf('CPU Single Precision Time: %.3f seconds\n', time_cpu_single);
fprintf('CPU Double Precision Time: %.3f seconds\n', time_cpu_double);
fprintf('GPU Single Precision Time: %.3f seconds\n', time_gpu_single);
fprintf('GPU Double Precision Time: %.3f seconds\n', time_gpu_double);
