CarbonTracks: The Carbon Emission Tracker
Welcome to CarbonTracks, a simple Python-based tool that helps you calculate carbon emissions, travel time, and eco-scores for different modes of transport. Whether you're planning your next trip or trying to reduce your carbon footprint, CarbonTracks can help you make informed decisions.

Features
Carbon Emissions Calculation: Estimate the CO₂ emissions for different transport modes based on the distance traveled.
Travel Time Calculation: Calculate the time required to reach your destination based on different transport modes.
Eco-Score Calculation: Get a score reflecting the environmental impact of your journey, helping you make eco-conscious travel choices.
Modes of Transport Supported
Bike: No emissions, fast travel times, and a high eco-score.
Jeepney: Public transport option with moderate emissions, average travel times, and a reasonable eco-score.
Car: Private transport with higher emissions, longer travel times, and a lower eco-score.

Installation
Clone this repository 

git clone https://github.com/yourusername/CarbonTracks.git

Navigate into the project directory:
cd CarbonTracks


Run the program:
python carbontracks.py


CarbonTracks: The Carbon Emission Tracker
Welcome to CarbonTracks, a simple Python-based tool that helps you calculate carbon emissions, travel time, and eco-scores for different modes of transport. Whether you're planning your next trip or trying to reduce your carbon footprint, CarbonTracks can help you make informed decisions.

Features
Carbon Emissions Calculation: Estimate the CO₂ emissions for different transport modes based on the distance traveled.
Travel Time Calculation: Calculate the time required to reach your destination based on different transport modes.
Eco-Score Calculation: Get a score reflecting the environmental impact of your journey, helping you make eco-conscious travel choices.
Modes of Transport Supported
Bike: No emissions, fast travel times, and a high eco-score.
Jeepney: Public transport option with moderate emissions, average travel times, and a reasonable eco-score.
Car: Private transport with higher emissions, longer travel times, and a lower eco-score.
Installation
Clone this repository to your local machine:

bash
Copy code
git clone https://github.com/yourusername/CarbonTracks.git
Navigate into the project directory:

bash
Copy code
cd CarbonTracks
Ensure you have Python 3.x installed on your machine.

Run the program:

bash
Copy code
python carbontracks.py
How It Works
Code Structure
Abstract Base Class Transport: This is the base class for all transport modes. It defines the common interface for calculating emissions, travel time, and eco-score.
Subclasses (Bike, Jeepney, Car): These implement the methods for calculating emissions, travel time, and eco-score based on the specifics of each mode of transport.
Route Class: Represents a route with a starting point, destination, and distance. It allows you to fetch the details of the route for each transport mode.
Main Logic: The program allows the user to input start and destination locations and distance. It then calculates the emissions, travel time, and eco-score for each transport mode.
Example Workflow
Input: You are prompted to enter:

Starting location
Destination
Distance (in kilometers)
Output: For each transport mode (Bike, Jeepney, and Car), the program will display:

Emissions (in kg CO₂)
Travel Time (in minutes)
Eco-Score (a score out of 100 reflecting the environmental impact)
Repeat: You can continue calculating for different routes until you decide to quit.
