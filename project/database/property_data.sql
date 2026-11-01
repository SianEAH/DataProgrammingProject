#Create database
CREATE DATABASE property_data;

#Use database
USE property_data;

#Create the table for my cleaned data
CREATE TABLE ppr_clean (
    Date_of_Sale VARCHAR(20), #Use VARCHAR because DATE causes importing issues
    Address TEXT,
    County VARCHAR(50),
    Eircode VARCHAR(10),
    Price_EUR DECIMAL(12,2),
    Not_Full_Market_Price VARCHAR(10),
    VAT_Exclusive VARCHAR(10),
    Description_of_Property VARCHAR(100),
    Year INT,
    Month INT
);

#Check to see if my records are there
SELECT COUNT(*) FROM ppr_clean; 
SELECT COUNT(*) FROM property_data.ppr_clean;





