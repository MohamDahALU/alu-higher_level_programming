-- List cities in the state of california
SELECT * FROM cities WHERE state_id IN (
    SELECT id FROM states WHERE name = 'California'
);