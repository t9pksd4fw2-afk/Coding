CREATE TABLE IF NOT EXISTS MARINE(
observation_id INTEGER PRIMARY KEY,
animal_name TEXT NOT NULL,
animal_group TEXT NOT NULL,
habitat TEXT NOT NULL,
depth_m INTEGER NOT NULL,
estimated_weight_kg REAL NOT NULL);

INSERT INTO MARINE VALUES
(1,'Blue Whale','Mammal','Open Ocean', 30, 120000.0);
INSERT INTO MARINE VALUES
(2,'Bottlenose Dolphin','Mammal',     'Open Ocean', 15,250.0);
INSERT INTO MARINE VALUES
(3, 'Green Sea Turtle','Reptile',    'Coral Reef', 10, 160.0);
INSERT INTO MARINE VALUES
(4, 'Clownfish','Fish','Coral Reef',5, 0.3);
INSERT INTO MARINE VALUES
(5, 'Hammerhead Shark', 'Fish',       'Open Ocean', 70,230.0);
INSERT INTO MARINE VALUES
(6, 'Giant Octopus', 'Mollusc',    'Seabed'  40, 25.0);
INSERT INTO MARINE VALUES
(7, 'Manta Ray', 'Fish', 'Open Ocean', 25,1350.0);
INSERT INTO MARINE VALUES
(8, 'Starfish','Echinoderm', 'Seabed', 20,0.5);

SELECT * FROM MARINE;

SELECT animal_group FROM MARINE;

SELECT DISTINCT animal_group FROM MARINE;

SELECT COUNT(DISTINCT animal_group) AS unique_animal_groups
FROM MARINE;

SELECT COUNT(observation_id) AS open_ocean_observations
FROM MARINE
WHERE habitat = 'Open Ocean';

SELECT SUM(estimated_weight_kg) AS total_estimated_weight_kg 
FROM MARINE;

SELECT AVG(depth_m) AS
average_observation_depth_m
FROM MARINE;

SELECT
    COUNT(observation_id) AS total_observations,
    COUNT(DISTINCT animal_group) AS unique_animal_groups,
    SUM(estimated_weight_kg) AS total_estimated_weight_kg,
    AVG(depth_m) AS average_observation_depth_m
FROM MARINE;
