import random
import matplotlib.pyplot as plt

def simulate_dice_throws(num_throws):
    sum_frequencies = {i: 0 for i in range(2, 13)} # Index from 0 to 12, we will use index 2 to 12
    
    for _ in range(num_throws):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        dice_sum = die1 + die2
        sum_frequencies[dice_sum] += 1
    
    return sum_frequencies

# Calculate probabilities
def calculate_probabilities(sum_frequencies, num_throws):
    probabilities = {s: (count / num_throws) * 100 for s, count in sum_frequencies.items()}
    return probabilities


# Theoretical probabilities
def display_results(simulated_probabilities, theoretical_probabilities):
    print("Sum\tSimulated Probability\tTheoretical Probability")
    for sum_val in range(2, 13):
        print(f"{sum_val}\t{simulated_probabilities[sum_val]:.2f}%\t\t{theoretical_probabilities[sum_val]:.2f}%")

def plot_probabilities(simulated_probabilities, theoretical_probabilities):
    sums = list(range(2, 13))
    sim_probs = [simulated_probabilities[sum_val] for sum_val in sums]
    theo_probs = [theoretical_probabilities[sum_val] for sum_val in sums]
    
    plt.figure(figsize=(10, 6))
    plt.plot(sums, sim_probs, label="Simulated Probabilities", marker='o')
    plt.plot(sums, theo_probs, label="Theoretical Probabilities", marker='x')
    plt.xlabel('Sum of Dice')
    plt.ylabel('Probability (%)')
    plt.title('Simulated vs Theoretical Probabilities of Dice Sums')
    plt.legend()
    plt.grid(True)
    plt.show()

# Theoretical probabilities for comparison
theoretical_probabilities = {
    2: (1/36) * 100,
    3: (2/36) * 100,
    4: (3/36) * 100,
    5: (4/36) * 100,
    6: (5/36) * 100,
    7: (6/36) * 100,
    8: (5/36) * 100,
    9: (4/36) * 100,
    10: (3/36) * 100,
    11: (2/36) * 100,
    12: (1/36) * 100
}

# Simulate dice throws
num_throws = 100000  # Example: 100,000 throws
sum_frequencies = simulate_dice_throws(num_throws)

# Calculate simulated probabilities
simulated_probabilities = calculate_probabilities(sum_frequencies, num_throws)

# Display results
display_results(simulated_probabilities, theoretical_probabilities)

# Plot results
plot_probabilities(simulated_probabilities, theoretical_probabilities)