-- SQL file that will make an SQL table and put some data into it

-- Create a table if this one doesn't already exists
CREATE TABLE IF NOT EXISTS chocolate(
    choc_id INTEGER PRIMARY KEY AUTOINCREMENT,
    flavour VARCHAR(30) NOT NULL,
    weight_gr INTEGER NOT NULL,
    fairtrade BOOLEAN NOT NULL
);

INSERT INTO chocolate (flavour, weight_gr, fairtrade) VALUES ("Salted Caramel", 60, true);
INSERT INTO chocolate (flavour, weight_gr, fairtrade) VALUES ("Strawberry", 150, true);
INSERT INTO chocolate (flavour, weight_gr, fairtrade) VALUES ("Milk", 80, true);