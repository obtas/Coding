CREATE TABLE IF NOT EXISTS cats(
    cat_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_type VARCHAR(30) NOT NULL,
    weight_kg INTEGER NOT NULL,
    patterned BOOLEAN NOT NULL
);

INSERT INTO cats (name_type, weight_kg, patterned) VALUES ("tiger", 120, true);
INSERT INTO cats (name_type, weight_kg, patterned) VALUES ("lion", 150, false);
INSERT INTO cats (name_type, weight_kg, patterned) VALUES ("jaguar", 90, false);
INSERT INTO cats (name_type, weight_kg, patterned) VALUES ("leopard", 100, true)