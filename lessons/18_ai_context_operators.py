# ==========================================
# Lesson 18: AI Context - Operators and Conditional Control
# ==========================================
# In this lesson, we look at how operators (math, comparison) 
# and conditional statements (if/elif/else) are used for evaluating metrics 
# and routing logic based on dataset characteristics.

# 1. CALCULATING METRICS
# Basic arithmetic operators are used to calculate metrics like accuracy.

correct_predictions = 850
total_predictions = 1000

# Calculate percentage
accuracy_percent = (correct_predictions / total_predictions) * 100
print(f"Model's Accuracy: {accuracy_percent:.1f}%\n")


# 2. EVALUATING TARGETS
# Conditional statements verify if a model meets the required threshold before deployment.

target_accuracy = 0.90
current_accuracy = 0.87

print("--- Target Evaluation ---")
if current_accuracy >= target_accuracy:
    print("SUCCESS: Model meets the performance requirements for deployment.")
else:
    # Calculate how much more accuracy is needed
    shortfall = target_accuracy - current_accuracy
    print(f"WARNING: Model failed to meet requirements.")
    # The :.2% format specifier multiplies by 100 and adds a % sign
    print(f"Need {shortfall:.2%} more accuracy to reach the target threshold.\n")


# 3. CONDITIONAL ROUTING (Model Selection)
# AI pipelines frequently select different algorithms depending on the data
# or the specific task being performed.

task_type = "classification"
dataset_size = 50000

print("--- Model Selection ---")
print(f"Task Type: {task_type}")
print(f"Dataset Size: {dataset_size}")

if task_type == "classification" and dataset_size < 10000:
    # Small structured datasets often work well with simpler models
    model = "Logistic Regression"
    print("Decision: Using simple linear model for small classification task.")
    
elif task_type == "classification" and dataset_size >= 10000:
    # Larger datasets generally benefit from deep learning
    model = "Neural Network"
    print("Decision: Using deep learning for large classification task.")
    
elif task_type == "text_generation":
    # Generative tasks require specialized architectures
    model = "GPT-based Transformer"
    print("Decision: Using generative model for text generation.")
    
else:
    model = "Custom Model"
    print("Decision: Fallback - Building a custom architecture.")

print(f"\nSelected Architecture: {model}")
