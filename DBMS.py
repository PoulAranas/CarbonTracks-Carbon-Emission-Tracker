CREATE TABLE TransportModes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    mode_name VARCHAR(50) NOT NULL
);

-- Table to store information about routes
CREATE TABLE Routes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    start_location VARCHAR(100) NOT NULL,
    destination_location VARCHAR(100) NOT NULL,
    distance DECIMAL(10, 2) NOT NULL
);

-- Table to store metrics for each transport mode and route
CREATE TABLE TransportMetrics (
    id INT PRIMARY KEY AUTO_INCREMENT,
    route_id INT,
    transport_mode_id INT,
    emissions DECIMAL(10, 2),
    travel_time DECIMAL(10, 2),
    eco_score INT,
    FOREIGN KEY (route_id) REFERENCES Routes(id),
    FOREIGN KEY (transport_mode_id) REFERENCES TransportModes(id)
);

-- Insert default transport modes (Bike, Jeepney, Car)
INSERT INTO TransportModes (mode_name) VALUES ('Bike');
INSERT INTO TransportModes (mode_name) VALUES ('Jeepney');
INSERT INTO TransportModes (mode_name) VALUES ('Car');

INSERT INTO Routes (start_location, destination_location, distance)
VALUES ('City A', 'City B', 120.50);

-- Insert transport metrics for Bike, Jeepney, and Car on a specific route (Assume route_id = 1)
INSERT INTO TransportMetrics (route_id, transport_mode_id, emissions, travel_time, eco_score)
VALUES 
(1, 1, 0, (120.50 / 15) * 60, 100),  -- Bike
(1, 2, 17 * 120.50 / 1000, (120.50 / 16) * 60, 100 - (17 * 120.50 / 1000 * 200)),  -- Jeepney
(1, 3, 120.50 * 0.15, (120.50 / 60) * 60, 100 - (120.50 * 0.15 * 50));  -- Car

