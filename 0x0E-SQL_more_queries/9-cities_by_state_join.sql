USE hbtn_0d_usa;
SELECT cities.id, cities.name, states.name FROM cities NATURAL JOIN states ON states.id = cities.state_id ORDER BY cities.id;