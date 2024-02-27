-- ==========  Запросы к таблице doctors  ==========

SELECT avg(salary) 
FROM doctors;


SELECT avg(premium)
FROM doctors
WHERE salary > 72787.68;

-- ==========  Запросы к таблице vacations  ==========

SELECT CONCAT(doctors.first_name, ' ', doctors.last_name) as names, 
       AVG(DATEDIFF(vacations.end_date, vacations.start_date)) as AvgVacationDays
FROM doctors
JOIN vacations ON doctors.id = vacations.doctors_id
GROUP BY doctors.id
ORDER BY AvgVacationDays;

SELECT 
    CONCAT(doctors.first_name, ' ', doctors.last_name) AS names,
    MIN(YEAR(vacations.start_date)) AS earliest_vacation_year,
    MAX(YEAR(vacations.start_date)) AS latest_vacation_year,
    (MAX(YEAR(vacations.start_date)) - MIN(YEAR(vacations.start_date))) AS year_diff
FROM doctors
JOIN vacations ON doctors.id = vacations.doctors_id
GROUP BY doctors.id
ORDER BY year_diff ASC;

-- ==========  Запросы к таблице donations  ==========


SELECT SUM(amount) as alldonations, departments_id 
FROM donations 
GROUP BY departments_id 
ORDER BY departments_id ASC; 

SELECT 
    sponsors.sponsors,
    SUM(donations.amount) as total_donations,
    sponsors.id,
    DISTINCT donations.DATE as YEARS
FROM donations
JOIN sponsors ON donations.sponsors_id = sponsors.id
GROUP BY sponsors.id
ORDER BY YEARS ASC, sponsors.id ASC;

SELECT sponsors.sponsor as sponsor_name, 
    SUM(donations.amount) as total_donations, 
    sponsors.id, 
    donations.DATE as YEARS 
FROM donations 
JOIN sponsors ON donations.sponsors_id = sponsors.id 
GROUP BY sponsors.id, donations.DATE
ORDER BY YEARS ASC, sponsors.id ASC;