-- script that converts hbtn_0c_0
USE hbtn_0c_0

ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE = utf8_general_ci;

ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE = utf8_general_ci;

ALTER TABLE first_table CHANGE name name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8_general_ci;
