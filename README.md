# CodeAlpha_StockPortfolio
A stock portfolio management system to track investments and visualize performance for Python Progamming Internship at CodeAlpha (Task 2)


Here's a *README.md* file for your *Stock Portfolio Tracker* project:

markdown
# Stock Portfolio Tracker 📈

The Stock Portfolio Tracker is a Python-based application that allows users to manage and track their stock investments. With features like real-time stock price updates using the `yfinance` library, it helps users calculate the value of their portfolio and stay informed about stock prices.

---

## Features 🚀

1. **Update Portfolio**:
   - Add or update the number of shares for any stock in your portfolio.
   - Keeps a running record of your stock holdings.

2. **Display Portfolio Summary**:
   - Fetches the latest stock prices in real-time using `yfinance`.
   - Calculates and displays the total value of each stock in your portfolio.

3. **View Current Stock Price**:
   - Allows you to check the current price of any stock by entering its symbol.

4. **User-Friendly Menu**:
   - A menu-driven interface to easily manage your portfolio.

5. **Real-Time Updates**:
   - Leverages the `yfinance` library to fetch up-to-date stock data.

---

## Installation ⚙

### Prerequisites:
- Python 3.6 or higher
- `yfinance` library

### Steps:
1. Clone this repository:
   bash
   git clone https://github.com/your-username/stock-portfolio-tracker.git
   
2. Navigate to the project directory:
   bash
   cd stock-portfolio-tracker
   
3. Install the required dependencies:
   bash
   pip install yfinance
   
4. Run the script:
   bash
   python portfolio_tracker.py
   

---

## Usage 📝

1. Launch the program.
2. Select an option from the menu:
   - **Option 1**: Add or update your portfolio by entering the stock symbol and the number of shares.
   - **Option 2**: View a detailed summary of your portfolio, including current prices and total values.
   - **Option 3**: Check the current price of any stock by entering its symbol.
   - **Option 4**: Exit the application.
3. Follow the prompts to manage your portfolio effectively.

---

## Example Output 📊


Stock Portfolio Tracker Menu:
1. Update Portfolio
2. Display Portfolio Summary
3. View Current Stock Price
4. Exit
Enter your choice: 1
Enter stock symbol (e.g., AAPL, GOOG): AAPL
Enter number of shares: 10
Updated portfolio: AAPL - 10 shares

Stock Portfolio Tracker Menu:
1. Update Portfolio
2. Display Portfolio Summary
3. View Current Stock Price
4. Exit
Enter your choice: 2

Portfolio Summary:
AAPL: 10 shares
Current Price: $150.00
Total Value: $1500.00
----------------------------------------


---

## Future Enhancements 🔮

1. Add error handling for invalid stock symbols or network issues.
2. Include support for selling shares or removing stocks from the portfolio.
3. Provide graphical visualization of portfolio performance over time.
4. Enable saving and loading portfolio data from a file.

---

## Contributing 🤝

Contributions are welcome! Feel free to open an issue or submit a pull request for improvements or new features.

---

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgements 🙏

- Built using the [`yfinance`](https://github.com/ranaroussi/yfinance) library for fetching real-time stock data.
- Inspired by the need for simple and effective stock management tools.

---

## Contact 📬

If you have any questions or suggestions, feel free to reach out:
- **Email**: muhsinaaaa14@gmail.com

Done by Muhaceena M
