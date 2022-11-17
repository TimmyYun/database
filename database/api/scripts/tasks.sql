USE dev;
/* First task */
SELECT d.disease_code, d.description FROM disease d 
LEFT JOIN discover di ON d.disease_code = di.disease_code
WHERE d.pathogen = 'Bacteria' AND di.first_enc_date < '1990-01-01'

/* Second task */
SELECT u.name, u.surname, d.degree FROM doctor d
LEFT JOIN users u ON d.email = u.email
WHERE 'infectious diseases' NOT IN (SELECT dt.description FROM diseasetype dt WHERE dt.id IN (SELECT s.id FROM specialize s WHERE s.email = d.email))

/* Third task */
SELECT u.name, u.surname, d.degree FROM doctor d
LEFT JOIN users u ON d.email = u.email
WHERE (SELECT COUNT(*) FROM diseasetype dt WHERE dt.id IN (SELECT s.id FROM specialize s WHERE s.email = d.email)) > 2

/* Fourth task */
SELECT c.cname, AVG(u.salary) FROM country c
LEFT JOIN users u ON u.cname = c.cname
LEFT JOIN doctor d ON u.email = d.email
WHERE 'virology' IN (SELECT dt.description FROM diseasetype dt WHERE dt.id IN (SELECT s.id FROM specialize s WHERE s.email = d.email))
GROUP BY c.cname

/* Fifth task */
