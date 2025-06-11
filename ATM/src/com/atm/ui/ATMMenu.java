package com.atm.ui;

import com.atm.model.account;
import com.atm.model.Transaction;
import com.atm.services.ATMService;

import java.text.NumberFormat;
import java.time.format.DateTimeFormatter;
import java.util.List;
import java.util.Scanner;

public class ATMMenu {
    private final ATMService atmService;
    private final Scanner scanner;
    private final NumberFormat currencyFormat;

    public ATMMenu(ATMService atmService) {
        this.atmService = atmService;
        this.scanner = new Scanner(System.in);
        this.currencyFormat = NumberFormat.getCurrencyInstance();
    }

    public void start() {
        System.out.println("Welcome to the ATM System");

        while (true) {
            if (atmService.getCurrentAccount() == null) {
                showLoginMenu();
            } else {
                showMainMenu();
            }
        }
    }

    private void showLoginMenu() {
        System.out.println("\nPlease enter your credentials:");
        System.out.print("Account Number: ");
        String accountNumber = scanner.nextLine();
        System.out.print("PIN: ");
        String pin = scanner.nextLine();

        if (atmService.authenticate(accountNumber, pin)) {
            account account = atmService.getCurrentAccount();
            System.out.println("\nWelcome, " + account.getCustomerName() + "!");
        } else {
            System.out.println("\nInvalid account number or PIN. Please try again.");
        }
    }

    private void showMainMenu() {
        System.out.println("\nMain Menu:");
        System.out.println("1. Check Balance");
        System.out.println("2. Deposit");
        System.out.println("3. Withdraw");
        System.out.println("4. Transfer");
        System.out.println("5. Transaction History");
        System.out.println("6. Logout");
        System.out.print("Please select an option: ");

        int choice;
        try {
            choice = Integer.parseInt(scanner.nextLine());
        } catch (NumberFormatException e) {
            System.out.println("Invalid input. Please enter a number.");
            return;
        }

        switch (choice) {
            case 1:
                checkBalance();
                break;
            case 2:
                deposit();
                break;
            case 3:
                withdraw();
                break;
            case 4:
                transfer();
                break;
            case 5:
                showTransactionHistory();
                break;
            case 6:
                atmService.logout();
                System.out.println("You have been logged out. Thank you!");
                break;
            default:
                System.out.println("Invalid option. Please try again.");
        }
    }

    private void checkBalance() {
        double balance = atmService.checkBalance();
        System.out.println("\nYour current balance is: " + currencyFormat.format(balance));
    }

    private void deposit() {
        System.out.print("\nEnter deposit amount: ");
        try {
            double amount = Double.parseDouble(scanner.nextLine());
            atmService.deposit(amount);
            System.out.println("Deposit successful. New balance: " +
                    currencyFormat.format(atmService.checkBalance()));
        } catch (NumberFormatException e) {
            System.out.println("Invalid amount format.");
        } catch (IllegalArgumentException | IllegalStateException e) {
            System.out.println(e.getMessage());
        }
    }

    private void withdraw() {
        System.out.print("\nEnter withdrawal amount: ");
        try {
            double amount = Double.parseDouble(scanner.nextLine());
            atmService.withdraw(amount);
            System.out.println("Withdrawal successful. New balance: " +
                    currencyFormat.format(atmService.checkBalance()));
        } catch (NumberFormatException e) {
            System.out.println("Invalid amount format.");
        } catch (IllegalArgumentException | IllegalStateException e) {
            System.out.println(e.getMessage());
        }
    }

    private void transfer() {
        System.out.print("\nEnter target account number: ");
        String targetAccount = scanner.nextLine();
        System.out.print("Enter transfer amount: ");

        try {
            double amount = Double.parseDouble(scanner.nextLine());
            atmService.transfer(targetAccount, amount);
            System.out.println("Transfer successful. New balance: " +
                    currencyFormat.format(atmService.checkBalance()));
        } catch (NumberFormatException e) {
            System.out.println("Invalid amount format.");
        } catch (IllegalArgumentException | IllegalStateException e) {
            System.out.println(e.getMessage());
        }
    }

    private void showTransactionHistory() {
        List<Transaction> transactions = atmService.getTransactionHistory();
        System.out.println("\nTransaction History:");
        System.out.println("-----------------------------------------------");
        System.out.printf("%-20s %-10s %-10s %s%n",
                "Date/Time", "Type", "Amount", "Description");
        System.out.println("-----------------------------------------------");

        if (transactions.isEmpty()) {
            System.out.println("No transactions found.");
        } else {
            DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
            for (Transaction t : transactions) {
                System.out.printf("%-20s %-10s %-10s %s%n",
                        t.getTimestamp().format(formatter),
                        t.getType(),
                        currencyFormat.format(t.getAmount()),
                        t.getDescription());
            }
        }
        System.out.println("-----------------------------------------------");
    }
}
