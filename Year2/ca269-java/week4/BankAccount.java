//adding getters and setters

public class BankAccount
{
    
    double balance;
    
    public BankAccount()
    {
        balance = 100.00;
    }
    
    public BankAccount(double val)
    {
        balance = val;
    }
    
    public void withdraw(double amount)
    {
        balance = balance - amount;
    }
    
    public void deposit(double amount)
    {
        balance = balance + amount;
    }
    
    public void setBalance(double newVal)
    {
        balance = newVal;
    }
    
    public double getBalance()
    {
        return balance;
    }
    public String toString()
    {
        return "The balance is " + balance;   
    }
}