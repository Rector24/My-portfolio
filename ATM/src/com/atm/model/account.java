package com.atm.model;

public class account {
    private String accountNumber;
    private String pin;
    private double balance;
    private String customerName;

    public void Account(String accountNumber, String pin, double balance, String customerName) {
        this.accountNumber = accountNumber;
        this.pin = pin;
        this.balance = balance;
        this.customerName = customerName;
    }

    // Getters and Setters
    public String getAccountNumber() {
        return accountNumber;
    }

    public String getPin() {
        return pin;
    }

    public double getBalance() {
        return balance;
    }

    public void setBalance(double balance) {
        this.balance = balance;
    }

    public String getCustomerName() {
        return customerName;
    }

}