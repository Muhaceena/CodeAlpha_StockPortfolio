import yfinance as yf
class StockPortfolio:
    def __init__(self):
        self.portfolio = {}
    def update_portfolio(self, stock_symbol, shares):
        if stock_symbol in self.portfolio:
            self.portfolio[stock_symbol] += shares
        else:
            self.portfolio[stock_symbol] = shares
        print(f"Updated portfolio: {stock_symbol} - {shares} shares")
    def display_portfolio_summary(self):
        print("\nPortfolio Summary:")
        for stock_symbol, shares in self.portfolio.items():
            stock = yf.Ticker(stock_symbol)
            stock_data = stock.history(period="1d")
            current_price = stock_data['Close'].iloc[0]  # Use iloc to access the first row
            total_value = current_price * shares
            print(f"{stock_symbol}: {shares} shares")
            print(f"Current Price: ${current_price:.2f}")
            print(f"Total Value: ${total_value:.2f}")
            print("-" * 40)
    def view_stock_price(self):
        stock_symbol = input("Enter stock symbol: ").upper()
        stock = yf.Ticker(stock_symbol)
        stock_data = stock.history(period="1d")
        current_price = stock_data['Close'].iloc[0]  # Use iloc to access the first row
        print(f"The current price of {stock_symbol} is: ${current_price:.2f}")   
    def run(self):
        while True:
            print("\nStock Portfolio Tracker Menu:")
            print("1. Update Portfolio")
            print("2. Display Portfolio Summary")
            print("3. View Current Stock Price")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                stock_symbol = input("Enter stock symbol: ").upper()
                shares = int(input("Enter number of shares: "))
                self.update_portfolio(stock_symbol, shares)
            elif choice == '2':
                self.display_portfolio_summary()
            elif choice == '3':
                self.view_stock_price()
            elif choice == '4':
                print("Exiting the portfolio tracker.")
                break
            else:
                print("Invalid choice. Please try again.")
if __name__ == "__main__":
    portfolio = StockPortfolio()
    portfolio.run()

