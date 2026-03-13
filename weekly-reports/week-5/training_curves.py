"""
Week 5 — Training vs Validation Curves
Generates: accuracy & loss plots simulating a sentiment analysis model training.
Run:  python weekly-reports/week-5/training_curves.py
"""

import numpy as np
import matplotlib.pyplot as plt

# ─── Simulate 30 epochs of training data ─────────────────
np.random.seed(42)
epochs = np.arange(1, 31)

# Training metrics (smooth improvement curve)
train_loss = 0.95 * np.exp(-0.12 * epochs) + 0.08 + np.random.normal(0, 0.015, 30)
train_acc  = 1 - 0.85 * np.exp(-0.15 * epochs) - 0.02 + np.random.normal(0, 0.012, 30)

# Validation metrics (slightly worse, with realistic gap)
val_loss = 0.95 * np.exp(-0.10 * epochs) + 0.15 + np.random.normal(0, 0.025, 30)
val_acc  = 1 - 0.85 * np.exp(-0.11 * epochs) - 0.06 + np.random.normal(0, 0.018, 30)

# Clamp to realistic ranges
train_acc = np.clip(train_acc, 0, 1)
val_acc   = np.clip(val_acc, 0, 1)
train_loss = np.clip(train_loss, 0.01, 2)
val_loss   = np.clip(val_loss, 0.01, 2)

# ─── Plot Setup ──────────────────────────────────────────
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))
fig.patch.set_facecolor('#0d1117')
fig.suptitle('Sentiment Analysis Model — Training Report',
             fontsize=16, fontweight='bold', color='#e2e8f0', y=1.02)

for ax in (ax1, ax2):
    ax.set_facecolor('#161b22')
    ax.spines['bottom'].set_color('#30363d')
    ax.spines['left'].set_color('#30363d')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.tick_params(colors='#8b949e')
    ax.set_xlabel('Epoch', fontsize=11, color='#8b949e')
    ax.grid(True, alpha=0.15, color='#8b949e')

# ─── Loss Plot ───────────────────────────────────────────
ax1.plot(epochs, train_loss, color='#58a6ff', linewidth=2.2,
         label='Training Loss', marker='o', markersize=3, alpha=0.9)
ax1.plot(epochs, val_loss, color='#f97583', linewidth=2.2,
         label='Validation Loss', marker='s', markersize=3, alpha=0.9)
ax1.fill_between(epochs, train_loss, val_loss, alpha=0.08, color='#f97583')
ax1.set_ylabel('Loss', fontsize=11, color='#8b949e')
ax1.set_title('Loss Over Epochs', fontsize=13, fontweight='bold', color='#c9d1d9', pad=10)
ax1.legend(loc='upper right', fontsize=9, facecolor='#21262d',
           edgecolor='#30363d', labelcolor='#c9d1d9')

# ─── Accuracy Plot ───────────────────────────────────────
ax2.plot(epochs, train_acc * 100, color='#3fb950', linewidth=2.2,
         label='Training Accuracy', marker='o', markersize=3, alpha=0.9)
ax2.plot(epochs, val_acc * 100, color='#d29922', linewidth=2.2,
         label='Validation Accuracy', marker='s', markersize=3, alpha=0.9)
ax2.fill_between(epochs, train_acc * 100, val_acc * 100, alpha=0.08, color='#d29922')
ax2.set_ylabel('Accuracy (%)', fontsize=11, color='#8b949e')
ax2.set_title('Accuracy Over Epochs', fontsize=13, fontweight='bold', color='#c9d1d9', pad=10)
ax2.legend(loc='lower right', fontsize=9, facecolor='#21262d',
           edgecolor='#30363d', labelcolor='#c9d1d9')

# ─── Annotations ─────────────────────────────────────────
best_epoch = np.argmax(val_acc) + 1
best_val_acc = val_acc[best_epoch - 1] * 100
ax2.annotate(f'Best: {best_val_acc:.1f}%\n(Epoch {best_epoch})',
             xy=(best_epoch, best_val_acc),
             xytext=(best_epoch + 4, best_val_acc - 8),
             fontsize=9, color='#d29922', fontweight='bold',
             arrowprops=dict(arrowstyle='->', color='#d29922', lw=1.5))

# ─── Final metrics box ──────────────────────────────────
final_text = (f"Final Train Acc: {train_acc[-1]*100:.1f}%\n"
              f"Final Val Acc:   {val_acc[-1]*100:.1f}%\n"
              f"Final Train Loss: {train_loss[-1]:.4f}\n"
              f"Final Val Loss:   {val_loss[-1]:.4f}")
fig.text(0.5, -0.08, final_text, ha='center', fontsize=10,
         color='#8b949e', fontfamily='monospace',
         bbox=dict(boxstyle='round,pad=0.6', facecolor='#21262d',
                   edgecolor='#30363d'))

plt.tight_layout()
save_path = "weekly-reports/evidence/week5-training-curves.png"
plt.savefig(save_path, dpi=150, bbox_inches='tight', facecolor='#0d1117')
plt.show()
print(f"\n✅ Plot saved → {save_path}")
