DROP TABLE IF EXISTS Plant;
DROP TABLE IF EXISTS Schedule;
DROP TABLE IF EXISTS Log;

CREATE TABLE Plant(
	id INT PRIMARY KEY,
	species VARCHAR,
	--FOREIGN KEY (schedule) REFERENCES Schedule
	schedule INT,
	FOREIGN KEY (schedule) REFERENCES Schedule

CREATE TABLE Plant(
	id INT PRIMARY KEY,
	species VARCHAR,
	schedule INT
	--FOREIGN KEY (schedule) REFERENCES Schedule
);

CREATE TABLE Schedule(
	interval INT PRIMARY KEY
);

CREATE TABLE Log(
	id INT,
	day DATE,
	PRIMARY KEY (id, day),
	FOREIGN KEY (id) REFERENCES Plant
);
);