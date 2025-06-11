package com.atm.services;

import com.atm.model.Transaction;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import com.atm.model.account;


public class ATMService {
    private final Map<String, account> accounts;
    private final List<Transaction> transactions;
    private account currentAccount;

    public ATMService() {
        this.accounts = new HashMap<>();
        this.transactions = new ArrayList<>();
        initializeSampleAccounts();
    }

    private void initializeSampleAccounts() {
        // Sample accounts for testing
        accounts.put("123456", new Account("123456", "1234", 1000.00, "John Doe"));
        accounts.put("654321", new Account("654321", "4321", 500.00, "Jane Smith"));
    }

    public boolean authenticate(String accountNumber, String pin) {
        account account = accounts.get(accountNumber);
        if (account != null && account.getPin().equals(pin)) {
            currentAccount = account;
            return true;
        }
        return false;
    }

    public void logout() {
        currentAccount = null;
    }

    public double checkBalance() {
        if (currentAccount != null) {
            return currentAccount.getBalance();
        }
        throw new IllegalStateException("No account is currently logged in");
    }

    public void deposit(double amount) {
        if (currentAccount == null) {
            throw new IllegalStateException("No account is currently logged in");
        }
        if (amount <= 0) {
            throw new IllegalArgumentException("Deposit amount must be positive");
        }

        currentAccount.setBalance(currentAccount.getBalance() + amount);
        recordTransaction("DEPOSIT", amount, "ATM Deposit");
    }

    public void withdraw(double amount) {
        if (currentAccount == null) {
            throw new IllegalStateException("No account is currently logged in");
        }
        if (amount <= 0) {
            throw new IllegalArgumentException("Withdrawal amount must be positive");
        }
        if (currentAccount.getBalance() < amount) {
            throw new IllegalArgumentException("Insufficient funds");
        }

        currentAccount.setBalance(currentAccount.getBalance() - amount);
        recordTransaction("WITHDRAWAL", amount, "ATM Withdrawal");
    }

    public void transfer(String targetAccountNumber, double amount) {
        if (currentAccount == null) {
            throw new IllegalStateException("No account is currently logged in");
        }
        if (amount <= 0) {
            throw new IllegalArgumentException("Transfer amount must be positive");
        }
        if (currentAccount.getBalance() < amount) {
            throw new IllegalArgumentException("Insufficient funds");
        }

        account targetAccount = accounts.get(targetAccountNumber);
        if (targetAccount == null) {
            throw new IllegalArgumentException("Target account not found");
        }

        // Perform transfer
        currentAccount.setBalance(currentAccount.getBalance() - amount);
        targetAccount.setBalance(targetAccount.getBalance() + amount);

        // Record transactions for both accounts
        recordTransaction("TRANSFER", amount, "Transfer to " + targetAccountNumber);
    }

    private void recordTransaction(String type, double amount, String description) {
        String transactionId = "TXN" + System.currentTimeMillis();
        Transaction transaction = new Transaction(
                transactionId,
                currentAccount.getAccountNumber(),
                type,
                amount,
                description
        );
        transactions.add(transaction);
    }

    public List<Transaction> getTransactionHistory() {
        if (currentAccount == null) {
            throw new IllegalStateException("No account is currently logged in");
        }

        List<Transaction> accountTransactions = new ArrayList<>();
        for (Transaction t : transactions) {
            if (t.getAccountNumber().equals(currentAccount.getAccountNumber())) {
                accountTransactions.add(t);
            }
        }
        return accountTransactions;
    }

    public account getCurrentAccount() {
        return currentAccount;
    }
}
