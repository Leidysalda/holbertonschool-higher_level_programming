-- script that displays the average temperature (Fahrenheit).
SELECT state, MAX (value) AS max_temp FROM temperatures GROUP BY name ORDER BY state;
