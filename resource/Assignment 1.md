## Assignment 1: 

### Coffee Shop POS System with Python and SQLite

#### Overview

Your task is to develop a simple Point of Sale (POS) system for a coffee shop using Python and SQLite. The coffee shop sells three types of coffee, each at a different price. You will implement functionality to process sales, record transactions, and generate end-of-day reports.



#### Objectives

1. **Develop a POS System**: Create a Python program that allows the user to enter the type and quantity of coffee sold. Prices are fixed: Type A - 10 Rs, Type B - 15 Rs, and Type C - 20 Rs.

2. **Database Integration**: Use SQLite to store transaction data.

3. **Generate Reports**: At the end of the day, generate a report showing the total number of coffees sold and the total revenue from each POS terminal.

4. **Data Modeling**: Design and implement a database schema suitable for this application.

   

#### Requirements

1. **Python Classes**: Use OOP practices to create classes representing the different components of your system (e.g., `Transaction`, `ReportGenerator`, etc.).

2. **SQLite Database**: Store transaction data in a SQLite database.

3. **Report Generation**: Implement functionality to produce a daily sales report.

   

#### Tasks

1. **Data Modeling**:

   - Define a schema for your SQLite database. You will at least need a table for transactions. This table should include columns for the transaction ID, type of coffee, quantity, total price, and timestamp.

2. **POS System Development**:

   - Implement a class to handle POS operations. This should include methods for processing a sale, which involves accepting the type and quantity of coffee, calculating the total cost, and storing the transaction in the database.

3. **Database Integration**:

   - Implement a class for database operations. This class should handle opening a connection to the SQLite database, executing SQL commands, and closing the connection.
   - Ensure your program creates the database and table(s) if they don't already exist.

4. **Report Generation**:

   - Develop a method to query the database and generate a report of daily sales. The report should include the total number of each type of coffee sold and the total revenue generated from each type.

5. **Optional - JSON Report**:

   - If you prefer, create functionality to export the daily report as a JSON file in addition to or instead of displaying it in the terminal.

     

#### Evaluation Criteria

1. **Functionality**: The system accurately processes transactions and generates reports.

2. **Code Quality**: Code is well-organized, commented, and follows Python best practices.

3. **Database Integration**: Efficient and correct use of SQLite for data storage and retrieval.

4. **Error Handling**: The system gracefully handles invalid inputs and errors.

5. **Documentation**: Include clear instructions on how to run your program and any dependencies it has.

   

#### Submission

Submit your code along with a README file containing instructions for setting up and running your application. If you have implemented any additional features, make sure they are documented.