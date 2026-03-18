# ============================================================
# 12 - Modules
# Modules are pre-built libraries that extend what Python can do.
# Import them instead of writing everything from scratch.
# ============================================================

import datetime
import os
import math
import random

# ── datetime — working with dates and times ──────────────────
print("── datetime ────────────────────────")
now   = datetime.datetime.now()
today = datetime.date.today()

print(f"Right now:  {now}")
print(f"Today:      {today}")
print(f"Year:       {today.year}")
print(f"Month:      {today.month}")
print(f"Day:        {today.day}")

# Format dates into readable strings
print(f"Formatted:  {now.strftime('%d %B %Y, %I:%M %p')}")

# ── os — interact with the operating system & file system ───
print("\n── os ──────────────────────────────")
print(f"Current directory: {os.getcwd()}")
print(f"Files here:        {os.listdir('.')[:5]}...")  # first 5 entries

path_exists = os.path.exists("../data/test.txt")
print(f"data/test.txt exists: {path_exists}")

# ── math — mathematical functions ───────────────────────────
print("\n── math ────────────────────────────")
print(f"π          = {math.pi:.5f}")
print(f"√144       = {math.sqrt(144)}")
print(f"ceil(4.2)  = {math.ceil(4.2)}")       # round up
print(f"floor(4.9) = {math.floor(4.9)}")      # round down
print(f"2¹⁰        = {math.pow(2, 10):.0f}")  # power

# ── random — generate random values ─────────────────────────
print("\n── random ──────────────────────────")
print(f"Random int (1-10):  {random.randint(1, 10)}")
print(f"Random float (0-1): {random.random():.4f}")

colours = ["red", "green", "blue", "yellow", "purple"]
print(f"Random choice:      {random.choice(colours)}")

deck = list(range(1, 11))
random.shuffle(deck)
print(f"Shuffled cards:     {deck}")

# ── Importing specific items (instead of the whole module) ───
print("\n── targeted imports ────────────────")
from math import pi, sqrt
print(f"π = {pi:.4f}")
print(f"√81 = {sqrt(81):.0f}")