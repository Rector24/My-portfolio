package com.atm;

import com.atm.services.ATMService;
import com.atm.ui.ATMMenu;

public class ATMMachine {
    public static void main(String[] args) {
        ATMService atmService = new ATMService();
        ATMMenu atmMenu = new ATMMenu(atmService);
        atmMenu.start();
    }
}
