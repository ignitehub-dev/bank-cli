# Bank CLI Tool

Welcome to the Bank CLI tool! This is a simple command-line tool that allows you to interact with a virtual bank account. You can deposit money, withdraw money, and check your balance—all from the terminal!

## Prerequisites

- Python (version 3.6 or higher recommended)
- pip (usually comes with Python)

## Setting Up

### Step 1: Organize Your Files

Make sure your files and directories are structured like this:

```
mybanktool/
|-- bank_cli/
|   |-- __init__.py
|   `-- bank_cli.py
`-- setup.py
```

- **mybanktool/**: This is the main folder where everything resides.
- **bank_cli/**: A sub-folder which will contain the main logic of our tool.
- ****init**.py**: An empty file that tells Python that `bank_cli/` should be treated as a package or module.
- **bank_cli.py**: This is where the bank logic resides (like depositing, withdrawing, etc.).
- **setup.py**: A special script that helps package our tool so you can use it from the terminal.

### Step 2: Installation

To install the tool:

1. Open your terminal or command prompt.
2. Navigate to the `mybanktool/` directory using the `cd` command:
   ```bash
   cd path/to/mybanktool/
   ```
3. First, uninstall any previous versions of the tool:
   ```bash
   pip uninstall bank-cli
   ```
4. Then, install the tool:
   ```bash
   pip install .
   ```

Congratulations! The bank tool is now installed.

## Using the Bank CLI Tool

With the tool installed, you can now use it directly from the terminal. Here's how:

1. **Check Balance**:

   ```bash
   bank get_balance
   ```

   This will show you the current balance in your virtual bank account.

2. **Deposit Money**:

   ```bash
   bank deposit 100
   ```

   This will deposit $100 into your account.

3. **Withdraw Money**:
   ```bash
   bank withdraw 50
   ```
   This will withdraw $50 from your account.

That's it! Enjoy managing your virtual finances!

---

**Note**: This is a basic guide and the tool itself is quite simple. In a real-world scenario, you'd probably want features like persistent storage, user accounts, and more. But this guide is meant to get you started with the basics.
