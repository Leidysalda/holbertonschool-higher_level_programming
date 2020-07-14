-- script that converts hbtn_0c_0
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE first_table COLLATE utf8_general_ci;
SELECT name CONVERT(CAST(name) USING utf8) FROM first_table;
