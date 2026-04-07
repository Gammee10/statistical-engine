from src.stat_engine import StatEngine
from src.monte_carlo import simulate_crashes
import json

# Load data
with open("data/sample_salaries.json") as f:
    data = json.load(f)

engine = StatEngine(data)

print("Mean:", engine.get_mean())
print("Median:", engine.get_median())
print("Mode:", engine.get_mode())
print("Std Dev:", engine.get_standard_deviation())
print("Outliers:", engine.get_outliers())

# Simulation
for days in [30, 100, 10000]:
    prob = simulate_crashes(days)
    print(f"Days: {days}, Crash Probability: {prob}")