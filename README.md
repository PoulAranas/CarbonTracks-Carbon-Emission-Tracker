# Transport Metrics Console Application

## Brief Overview
This program calculates emissions, travel time, and eco-scores for different modes of transport: Bike, Jeepney, and Car. 
It aims to encourage eco-friendly travel choices by providing users with insightful transport metrics.

## Application of Python Concepts and Libraries
1. **Object-Oriented Programming (OOP):**
   - **Abstraction:** Implemented through the `Transport` abstract class.
   - **Inheritance:** Specialized classes (`Bike`, `Jeepney`, `Car`) inherit from the `Transport` class.
   - **Encapsulation:** Used for organizing data and methods within transport and route classes.

2. **Polymorphism:**
   - Each transport mode (`Bike`, `Jeepney`, `Car`) implements its unique behavior for emissions, travel time, and eco-score calculation.

## Details for SDG 13 (Climate Action)
This program supports Sustainable Development Goal 13 by raising awareness about carbon emissions in daily travel. 
By comparing the eco-score and emissions of various transport modes, users are encouraged to choose environmentally friendly options like biking.

## Instructions for Running the Program
1. Ensure you have Python installed on your computer (version 3.6 or later).
2. Save the program code to a file named `transport_metrics.py`.
3. Open your terminal or command prompt.
4. Navigate to the directory containing the `transport_metrics.py` file.
5. Run the program using the following command:
   ```bash
   python transport_metrics.py
   ```
6. Follow the on-screen instructions to input route details and view transport metrics.
