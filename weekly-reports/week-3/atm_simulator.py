"""
Week 3 — ATM Simulator
A loop-based ATM simulator with balance tracking, exception handling, and transaction history.
Run:  python weekly-reports/week-3/atm_simulator.py
"""


def atm_simulator():
    """
    Interactive ATM Simulator with:
    - Balance inquiry
    - Deposit with validation
    - Withdrawal with overdraft protection
    - Transaction history log
    - Exception handling for invalid inputs
    """
    balance = 5000.00
    pin = "1234"
    transaction_history = []
    max_withdrawal = 10000.00

    print("=" * 55)
    print("       🏦  WELCOME TO PYTHON BANK ATM  🏦")
    print("=" * 55)

    # ─── PIN Authentication ──────────────────────────────
    attempts = 3
    authenticated = False
    while attempts > 0:
        try:
            entered_pin = input(f"\n🔑 Enter your 4-digit PIN ({attempts} attempts left): ")
            if entered_pin == pin:
                authenticated = True
                print("\n✅ Authentication successful!")
                break
            else:
                attempts -= 1
                if attempts > 0:
                    print(f"❌ Incorrect PIN. {attempts} attempt(s) remaining.")
                else:
                    print("🚫 Account locked. Too many failed attempts.")
                    return
        except KeyboardInterrupt:
            print("\n\n⚠️  Session cancelled by user.")
            return

    if not authenticated:
        return

    # ─── Main ATM Loop ───────────────────────────────────
    while True:
        print("\n" + "─" * 45)
        print("  📋  MAIN MENU")
        print("─" * 45)
        print("  [1]  💰 Check Balance")
        print("  [2]  📥 Deposit Money")
        print("  [3]  📤 Withdraw Money")
        print("  [4]  📜 Transaction History")
        print("  [5]  🚪 Exit")
        print("─" * 45)

        try:
            choice = input("  👉 Select an option (1-5): ").strip()

            if choice == "1":
                # ── Balance Inquiry ──
                print(f"\n  💳 Current Balance: ${balance:,.2f}")
                transaction_history.append(f"Balance Inquiry → ${balance:,.2f}")

            elif choice == "2":
                # ── Deposit ──
                try:
                    amount = float(input("\n  📥 Enter deposit amount: $"))
                    if amount <= 0:
                        print("  ⚠️  Deposit amount must be positive.")
                    elif amount > 50000:
                        print("  ⚠️  Maximum single deposit is $50,000.")
                    else:
                        balance += amount
                        print(f"  ✅ Deposited ${amount:,.2f} successfully!")
                        print(f"  💳 New Balance: ${balance:,.2f}")
                        transaction_history.append(
                            f"Deposit: +${amount:,.2f} → Balance: ${balance:,.2f}"
                        )
                except ValueError:
                    print("  ❌ Invalid amount. Please enter a valid number.")

            elif choice == "3":
                # ── Withdrawal ──
                try:
                    amount = float(input("\n  📤 Enter withdrawal amount: $"))
                    if amount <= 0:
                        print("  ⚠️  Withdrawal amount must be positive.")
                    elif amount > max_withdrawal:
                        print(f"  ⚠️  Maximum withdrawal per transaction: ${max_withdrawal:,.2f}")
                    elif amount > balance:
                        print(f"  🚫 Insufficient funds! Current balance: ${balance:,.2f}")
                    else:
                        balance -= amount
                        print(f"  ✅ Withdrew ${amount:,.2f} successfully!")
                        print(f"  💳 Remaining Balance: ${balance:,.2f}")
                        transaction_history.append(
                            f"Withdrawal: -${amount:,.2f} → Balance: ${balance:,.2f}"
                        )
                except ValueError:
                    print("  ❌ Invalid amount. Please enter a valid number.")

            elif choice == "4":
                # ── Transaction History ──
                print("\n  📜 TRANSACTION HISTORY")
                print("  " + "─" * 40)
                if transaction_history:
                    for i, txn in enumerate(transaction_history, 1):
                        print(f"    {i}. {txn}")
                else:
                    print("    No transactions yet.")
                print("  " + "─" * 40)

            elif choice == "5":
                # ── Exit ──
                print("\n" + "=" * 55)
                print("  👋 Thank you for using Python Bank ATM!")
                print(f"  💳 Final Balance: ${balance:,.2f}")
                print("=" * 55)
                break

            else:
                print("  ⚠️  Invalid option. Please select 1-5.")

        except KeyboardInterrupt:
            print("\n\n  ⚠️  Session interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"  ❌ Unexpected error: {e}")


if __name__ == "__main__":
    atm_simulator()
