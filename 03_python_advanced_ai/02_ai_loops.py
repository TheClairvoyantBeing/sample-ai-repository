# ==========================================
# Lesson 17: AI Context - Loops and Batch Processing
# ==========================================
# This lesson demonstrates how loops are used in AI for 
# training over multiple epochs and processing data in batches.
# These are fundamental concepts when writing custom model training scripts.

# 1. TRAINING LOOPS (Epochs)
# An 'epoch' is one complete pass through the entire training dataset.
num_epochs = 10
initial_loss = 1.0

print("--- Starting Training Loop ---")
for epoch in range(1, num_epochs + 1):
    # Simulating loss decreasing and accuracy increasing over time
    loss = initial_loss / epoch
    accuracy = 1 - (1 / (epoch + 1))
    
    # Outputting statistics for the current epoch
    print(f"Epoch {epoch}/{num_epochs}")
    print(f"  Loss:     {loss:.4f}")
    print(f"  Accuracy: {accuracy:.4f}")
    print("-" * 30)

# 2. BATCH PROCESSING
# Datasets are often too large to fit into memory all at once.
# We divide the dataset into smaller 'batches' and process them sequentially.
dataset_size = 1_000_000
batch_size = 200

# Calculate how many full batches we have. 
# We use integer division (//) to get a whole number.
num_batches = dataset_size // batch_size

print("\n--- Starting Batch Processing ---")
print(f"Total dataset size: {dataset_size}")
print(f"Batch size: {batch_size}")
print(f"Total batches to process: {num_batches}\n")

# For demonstration, we'll only print the first 5 batches so we don't flood the console.
display_limit = 5

for batch_num in range(num_batches):
    # Calculate starting and ending index for the current batch
    start_idx = batch_num * batch_size
    end_idx = start_idx + batch_size
    
    if batch_num < display_limit:
        print(f"Processing Batch {batch_num + 1:04d}: Samples {start_idx:07d} to {end_idx:07d}")
    elif batch_num == display_limit:
        print(f"... continuing for {num_batches - display_limit} more batches ...")

print("\nBatch processing complete.")
