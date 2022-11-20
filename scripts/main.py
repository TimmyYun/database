from sqlalchemy import create_engine
from sqlalchemy.sql import text

engine = create_engine('mysql+pymysql://timur:12345@localhost/dev')

conn = engine.connect()

first_task = text(
    "SELECT d.disease_code, d.description FROM disease d LEFT JOIN discover di ON d.disease_code = di.disease_code WHERE LOWER(d.pathogen) = 'bacteria' AND di.first_enc_date < '1990-01-01'")

print(conn.execute(first_task, x='m', y='z',
      e1='%@aol.com', e2='%@msn.com').fetchall())

second_task = text(
    "SELECT u.name, u.surname, d.degree FROM doctor d LEFT JOIN users u ON d.email = u.email WHERE 'infectious diseases' NOT IN (SELECT LOWER(dt.description) FROM diseasetype dt WHERE dt.id IN (SELECT s.id FROM specialize s WHERE s.email = d.email))"
)

print(conn.execute(second_task, x='m', y='z',
      e1='%@aol.com', e2='%@msn.com').fetchall())

third_task = text("SELECT u.name, u.surname, d.degree FROM doctor d LEFT JOIN users u ON d.email = u.email WHERE (SELECT COUNT(*) FROM diseasetype dt WHERE dt.id IN (SELECT s.id FROM specialize s WHERE s.email = d.email)) > 2")

print(conn.execute(third_task, x='m', y='z',
      e1='%@aol.com', e2='%@msn.com').fetchall())

fourth_task = text("SELECT c.cname, AVG(u.salary) FROM country c LEFT JOIN users u ON u.cname = c.cname LEFT JOIN doctor d ON u.email = d.email WHERE 'virology' IN (SELECT LOWER(dt.description) FROM diseasetype dt WHERE dt.id IN (SELECT s.id FROM specialize s WHERE s.email = d.email)) GROUP BY c.cname")

print(conn.execute(fourth_task, x='m', y='z',
      e1='%@aol.com', e2='%@msn.com').fetchall())

fifth_task = text("SELECT ps.department, COUNT(*) FROM publicservant ps WHERE (SELECT COUNT(*) FROM record r WHERE r.email = ps.email AND LOWER(disease_code) = 'covid-19') > 1 GROUP BY ps.department")

print(conn.execute(fifth_task, x='m', y='z',
      e1='%@aol.com', e2='%@msn.com').fetchall())

sixth_task = text("UPDATE users u SET u.salary = u.salary * 2 WHERE (SELECT COUNT(*) FROM record r WHERE r.email = u.email AND r.disease_code = 'covid-19') > 3")

conn.execute(sixth_task, x='m', y='z',
      e1='%@aol.com', e2='%@msn.com')

seventh_task = text("DELETE FROM users u WHERE LOWER(u.name) like '%bek%' OR LOWER(u.name) like '%gul%'")

conn.execute(seventh_task, x='m', y='z',
      e1='%@aol.com', e2='%@msn.com')

eighth_task = text("CREATE INDEX idx_pathogen ON disease (pathogen)")

conn.execute(eighth_task, x='m', y='z',
      e1='%@aol.com', e2='%@msn.com')

ninth_task = text("SELECT u.email, u.name, ps.department FROM users u LEFT JOIN publicservant ps ON ps.email = u.email WHERE u.email in (SELECT r.email FROM record r WHERE r.total_patients > 100000 AND r.total_patients < 999999)")

print(conn.execute(ninth_task, x='m', y='z',
      e1='%@aol.com', e2='%@msn.com').fetchall())

tenth_task = text("SELECT c.cname, SUM(r.total_patients) AS Total FROM country c LEFT JOIN record r on c.cname = r.cname GROUP BY c.cname ORDER BY Total DESC LIMIT 5;")

print(conn.execute(tenth_task, x='m', y='z',
      e1='%@aol.com', e2='%@msn.com').fetchall())

eleventh_task = text("SELECT d.disease_code, SUM(r.total_patients) FROM disease d LEFT JOIN record r ON d.disease_code = r.disease_code GROUP BY disease_code")

print(conn.execute(eleventh_task, x='m', y='z',
      e1='%@aol.com', e2='%@msn.com').fetchall())
