# ============================================================
# Matplotlib — Training Visualization
# Generates training/validation loss and accuracy plots.
# Concepts: plt.figure(), plt.plot(), plt.savefig(), plt.show()
# ============================================================

import matplotlib.pyplot as plt
import numpy as np

print("Creating Training Visualizations...")

# ── Generate simulated training data over 10 epochs ──────────
epochs = np.arange(1, 11)                       # [1, 2, ..., 10]
train_loss = 1.0 / np.sqrt(epochs)              # decreasing loss curve
val_loss   = 1.0 / np.sqrt(epochs) + 0.1        # validation always slightly higher

# ── Plot 1: Loss Curves ─────────────────────────────────────
plt.figure(figsize=(10, 6))

# Plot training loss (blue dashed line with circle markers)
plt.plot(epochs, train_loss, 'b--', label='Training Loss', marker='o')

# Plot validation loss (red dashed line with square markers)
plt.plot(epochs, val_loss, 'r--', label='Validation Loss', marker='s')

# Axis labels, title, legend, and grid
plt.xlabel('Epoch', fontsize=12)
plt.ylabel('Loss', fontsize=12)
plt.title('Model Training Progress', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(True, alpha=0.3)

# Save to file and display
plt.savefig('training_progress.png', dpi=150, bbox_inches='tight')
print("Saved training_progress.png")
plt.show()

# ── Plot 2: Accuracy Curves ─────────────────────────────────
plt.figure(figsize=(10, 6))

# Simulated accuracy values (approaching 1.0 over time)
train_acc = 1 - (1 / (epochs + 1))              # training accuracy
val_acc   = train_acc - 0.05                     # validation lags slightly

# Plot training accuracy (green dashed) and validation accuracy (orange dashed)
plt.plot(epochs, train_acc, 'g--', label='Training Accuracy', marker='o')
plt.plot(epochs, val_acc, 'orange', label='Validation Accuracy', marker='s', linestyle='--')

# Axis labels, title, legend, and grid
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('Model Accuracy Over Time')
plt.legend()
plt.grid(True, alpha=0.2)

# Save to file and display
plt.savefig('accuracy_progress.png', dpi=150, bbox_inches='tight')
print('Saved accuracy_progress.png')
plt.show()