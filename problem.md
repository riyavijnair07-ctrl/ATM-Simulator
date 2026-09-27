Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> """
... ===============================================================================
... PROJECT PROBLEM STATEMENT: AUTOMATED TELLER MACHINE (ATM) SIMULATOR
... ===============================================================================
... 
... OBJECTIVE:
... Design and implement a menu-driven Python program that simulates the core 
... operations of an Automated Teller Machine (ATM) for a single user account.
... The program must run continuously within the Python IDLE shell until the user 
... explicitly chooses to exit.
... 
... SYSTEM REQUIREMENTS & FUNCTIONALITIES:
... 
... 1. INITIAL SETUP & VALIDATION:
...    - Configure a default account balance (e.g., ₹10,000) and a fixed 
...      4-digit PIN (e.g., '1234').
...    - Secure the interface by prompting the user for their PIN upon startup. 
...    - Grant access only if the PIN matches. Provide a maximum of 3 entry attempts 
...      before locking out the session.
... 
... 2. MENU-DRIVEN INTERACTION:
...    Once authenticated, present a clear, interactive choice menu:
...    [1] Check Balance
...    [2] Deposit Funds
...    [3] Withdraw Cash
...    [4] Change PIN
...    [5] Exit System
... 
... 3. CORE UTILITIES:
...    - Check Balance: Display the exact current account balance formatted properly.
...    - Deposit Funds: Prompt for a cash amount. Validate that the input is a 
...      positive number, update the account balance, and show the confirmation.
...    - Withdraw Cash: Prompt for a withdrawal amount. Check for two rules:
...      a) The amount must be positive.
...      b) The user must have sufficient funds. 
     If valid, deduct the amount and display the updated balance; otherwise, 
     throw an appropriate error message (e.g., "Insufficient Balance").
   - Change PIN: Allow the user to update their 4-digit PIN after confirming 
     their current PIN.
   - Exit System: Terminate the loop cleanly with a polite parting message.

4. EXCEPTION HANDLING & VALIDATION:
   - Protect the simulator from crashing if a user enters letters/symbols 
     instead of numbers during transaction prompts.
===============================================================================
