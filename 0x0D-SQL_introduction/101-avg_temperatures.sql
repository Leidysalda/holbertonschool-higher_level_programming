-- script that displays the average temperature (Fahrenheit).
SELECT AVG(value) AS avg_temp FROM temperatures GROUP BY state ORDER BY value DESC;
