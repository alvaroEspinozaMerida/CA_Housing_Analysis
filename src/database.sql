CREATE TABLE population (
    year INT,
    region VARCHAR,
    population INT,
    PRIMARY KEY (year, region)
);

CREATE TABLE housing_data (
    year INT,
    region VARCHAR,
    median_price FLOAT,
    total_units INT,
);

CREATE TABLE debt (
    quarter VARCHAR,
    mortgage FLOAT,
    credit_card FLOAT,
    student_loan FLOAT,
    auto_loan FLOAT,
    he_revolving FLOAT,
    other FLOAT,
    total FLOAT
);

INSERT INTO debt (quarter, mortgage, credit_card, student_loan, auto_loan, he_revolving, other, total)
SELECT quarter, Mortgage, "Credit Card" AS credit_card, "Student Loan" AS student_loan, "Auto Loan" AS auto_loan, "HE Revolving" AS he_revolving, other, total
FROM read_csv_auto('../data/debt_2003_2025_clean.csv', header=True)
