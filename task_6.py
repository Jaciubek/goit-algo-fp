def greedy_algorithm(items, budget):
    #  # Calculate the ratio of calories to cost and sort items based on calorie-to-cost ratio in descending order
    sorted_dishes = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_cost = 0
    total_calories = 0
    chosen_items = []
    
    for item, values in sorted_dishes:
        if total_cost + values['cost'] <= budget:
            total_cost += values['cost']
            total_calories += values['calories']
            chosen_items.append(item)
    
    return chosen_items, total_calories, total_cost

# Example usage
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100
chosen_items, total_calories, total_cost = greedy_algorithm(items, budget)
print("Greedy Algorithm Result Selection:")
print("Chosen items:", chosen_items)
print("Total calories:", total_calories)
print("Total cost:", total_cost)



def dynamic_programming(items, budget):
    # Create a list of (cost, calories) tuples from the items dictionary
    food_items = [(values['cost'], values['calories']) for values in items.values()]
    n = len(food_items)
    
    # Create a Dynamic Programing table where dp[i][j] represents the maximum calories with i items and budget j
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    
    # Fill the DP table
    for i in range(1, n + 1):
        cost, calories = food_items[i - 1]
        for j in range(budget + 1):
            if j < cost:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + calories)
    
    # Backtrack to find the chosen items
    total_calories = dp[n][budget]
    chosen_items = []
    total_cost = 0
    j = budget
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            item = list(items.keys())[i - 1]
            chosen_items.append(item)
            total_cost += food_items[i - 1][0]
            j -= food_items[i - 1][0]
    
    return chosen_items, total_calories, total_cost

# Example usage
chosen_items, total_calories, total_cost = dynamic_programming(items, budget)
print("Dynamic Programming Result Selection:")
print("Chosen items:", chosen_items)
print("Total calories:", total_calories)
print("Total cost:", total_cost)