CREATE TABLE IF NOT EXISTS zoo_animal (
animal_id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
species TEXT NOT NULL,
age_years INTEGER NOT NULL,
weight_kg REAL NOT NULL);


INSERT INTO zoo_animal VALUES (1,'Lion','Big Cat',5,190.0);
INSERT INTO zoo_animal VALUES (2,'Tiger','Big Cat',3,220.0);
INSERT INTO zoo_animal VALUES (3,'Elephant','Pachyderm',12,4500.0);
INSERT INTO zoo_animal VALUES (4,'Giraffe','Ungulate',7,800.0);
INSERT INTO zoo_animal VALUES (5,'Penguin','Bird',2,5.0);
INSERT INTO zoo_animal VALUES (6,'Panda','Bear',6,950.0);
INSERT INTO zoo_animal VALUES (7,'Cheetah','Big Cat',4,110.0);
INSERT INTO zoo_animal VALUES (8,'Rhino','Pachyderm',9,2300.0);

SELECT * FROM zoo_animal;
SELECT species FROM zoo_animal;
SELECT DISTINCT species FROM zoo_animal;
SELECT COUNT(DISTINCT species) AS unique_species FROM zoo_animal;

SELECT COUNT(animal_id) AS total_animals FROM zoo_animal;
SELECT COUNT(animal_id) AS older_than_5 FROM zoo_animal WHERE age_years > 5;

SELECT SUM(weight_kg) AS total_weight_kg FROM zoo_animal;

SELECT AVG(age_years) AS avg_age_years FROM zoo_animal;

SELECT
    COUNT(animal_id) AS total_animals,
    COUNT(DISTINCT species) AS unique_species,
    SUM(weight_kg) AS total_weight_kg,
    AVG(age_years) AS avg_age_years
FROM zoo_animal;