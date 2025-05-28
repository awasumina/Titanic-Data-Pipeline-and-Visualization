-- Count Passengers by Gender
SELECT 
  sex, 
  COUNT(*) AS total_passengers
FROM 
  titanic_raw
GROUP BY 
  sex;


-- Count Survivors by Gender
SELECT 
  sex, 
  COUNT(*) AS survived_passengers
FROM 
  titanic_raw
WHERE 
  survived = 1
GROUP BY 
  sex;


--Calculate Survival Rate by Gender
SELECT  
  sex,  
  COUNT(*) AS total_passengers, 
  SUM(survived) AS survived_passengers, 
  ROUND(100.0 * SUM(survived) / COUNT(*), 2) AS survival_rate
FROM 
  titanic_raw 
GROUP BY 
  sex;


--Breakdown by Class and Gender
SELECT  
  sex,
  pclass,
  COUNT(*) AS total_passengers,
  SUM(survived) AS survived_passengers,
  ROUND(100.0 * SUM(survived) / COUNT(*), 2) AS survival_rate
FROM 
  titanic_raw
GROUP BY 
  sex, pclass
ORDER BY 
  sex, pclass;
