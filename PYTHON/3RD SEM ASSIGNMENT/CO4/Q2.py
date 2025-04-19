population_mean = 55000
sample_mean = 53000
sample_std_dev = 4000
sample_size = 50

z_score = (sample_mean - population_mean) / (sample_std_dev / (sample_size ** 0.5))

print("Z-score:", z_score)

if abs(z_score) > 1.96:
    print("Reject null hypothesis.")
else:
    print("Fail to reject null hypothesis.")

print("Ayon_Aryan\n1RVU23CSE093")