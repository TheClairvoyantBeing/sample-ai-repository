# ==========================================
# Lesson 16: AI Context - Data Types
# ==========================================
# In this lesson, we explore how standard Python data types
# are used specifically within Machine Learning and AI contexts.
# We will define various hyperparameters and configuration blocks.

# 1. INTEGERS (int)
# Used for discrete counts that cannot be fractional.
# Examples: Number of complete passes over the dataset (epochs),
# or number of parallel threads.
epochs = 100
batch_size = 32
cuda_threads = 2

print(f"Starting training for {epochs} epochs with batch size {batch_size}...")

# 2. FLOATS (float)
# Used for continuous values, like learning rates, probabilities, and weights.
learning_rate = 0.001
frequency = 0.95
temperature = 0.7  # Controls randomness in generative models (e.g., LLMs)

print(f"Learning rate set to {learning_rate}. Temperature is {temperature}.")

# 3. STRINGS (str)
# Used for text data, model identifiers, or user prompts.
model_name = "gpt-4.0-turbo"
prompt = "Explain Machine Learning in simple terms"

print(f"Sending prompt '{prompt}' to model '{model_name}'.")

# 4. BOOLEANS (bool)
# Used for true/false flags, typically enabling/disabling features or tracking states.
is_trained = False
use_gpu = True
verbose = True

if use_gpu:
    print("GPU acceleration is ENABLED.")
else:
    print("Using CPU for computation.")

# 5. DICTIONARIES (dict)
# Extensively used used for grouping related configuration settings together.
config = {
    'model': 'llama-2',
    'max_tokens': 2048,
    'temperature': 0.7,
    'top_p': 0.9
}

print("\nModel Configuration:")
for key, value in config.items():
    print(f"  - {key}: {value}")
