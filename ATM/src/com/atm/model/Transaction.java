package com.atm.model;

import java.time.LocalDateTime;

public class Transaction {
    private final String transactionId;
    private final String accountNumber;
    private final LocalDateTime timestamp;
    private final String type; // "WITHDRAWAL", "DEPOSIT", "TRANSFER"
    private final double amount;
    private final String description;

    public Transaction(String transactionId, String accountNumber, String type,
                       double amount, String description) {
        this.transactionId = transactionId;
        this.accountNumber = accountNumber;
        this.timestamp = LocalDateTime.now();
        this.type = type;
        this.amount = amount;
        this.description = description;
    }

    // Getters
    public String getTransactionId() {
        return transactionId;
    }

    public String getAccountNumber() {
        return accountNumber;
    }

    public LocalDateTime getTimestamp() {
        return timestamp;
    }

    public String getType() {
        return type;
    }

    public double getAmount() {
        return amount;
    }

    public String getDescription() {
        return description;
    }
}
