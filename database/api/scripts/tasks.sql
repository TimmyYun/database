USE dev;
/* First task */
SELECT d.disease_code, d.description FROM disease d 
LEFT JOIN discover di ON d.disease_code = di.disease_code
WHERE LOWER(d.pathogen) = "bacteria" AND di.first_enc_date < "1990-01-01"

/* Second task */
SELECT u.name, u.surname, d.degree FROM doctor d
LEFT JOIN users u ON d.email = u.email
WHERE "infectious diseases" NOT IN (SELECT LOWER(dt.description) FROM diseasetype dt WHERE dt.id IN (SELECT s.id FROM specialize s WHERE s.email = d.email))

/* Third task */
SELECT u.name, u.surname, d.degree FROM doctor d
LEFT JOIN users u ON d.email = u.email
WHERE (SELECT COUNT(*) FROM diseasetype dt WHERE dt.id IN (SELECT s.id FROM specialize s WHERE s.email = d.email)) > 2

/* Fourth task */
SELECT c.cname, AVG(u.salary) FROM country c
LEFT JOIN users u ON u.cname = c.cname
LEFT JOIN doctor d ON u.email = d.email
WHERE "virology" IN (SELECT LOWER(dt.description) FROM diseasetype dt WHERE dt.id IN (SELECT s.id FROM specialize s WHERE s.email = d.email))
GROUP BY c.cname

/* Fifth task */
SELECT ps.department, COUNT(*) FROM publicservant ps
WHERE (SELECT COUNT(*) FROM record r WHERE r.email = ps.email AND LOWER(disease_code) = "covid-19") > 1
GROUP BY ps.department

/* Sixth task */
SELECT * FROM users;

UPDATE users u
SET u.salary = u.salary * 2
WHERE (SELECT COUNT(*) FROM record r WHERE r.email = u.email AND r.disease_code = "covid-19") > 3;

SELECT * FROM users;

/* Seventh task */
SELECT * FROM users;

DELETE FROM users u WHERE LOWER(u.name) like "%bek%" OR LOWER(u.name) like "%gul%";

SELECT * FROM users;

/* Eighth task */
SELECT * FROM disease;

CREATE INDEX idx_pathogen
ON disease (pathogen);

SELECT * FROM disease;

/* Ninth task */

