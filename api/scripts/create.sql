USE dev;

CREATE TABLE diseaseType (
    id INT,
    description VARCHAR(140),
    PRIMARY KEY(id)
);

CREATE TABLE country (
    cname VARCHAR(50),
    population BIGINT,
    PRIMARY KEY(cname)
);

CREATE TABLE disease (
    id BIGINT,
    disease_code VARCHAR(50),
    pathogen VARCHAR(20),
    description VARCHAR(140),
    disease_id INT,
    PRIMARY KEY(disease_code),
    FOREIGN KEY (disease_id) REFERENCES diseaseType(id)
);

CREATE TABLE discover(
    cname VARCHAR (50),
    disease_code VARCHAR (50),  
    first_enc_date DATE,
    FOREIGN KEY (disease_code) REFERENCES disease(disease_code),
    FOREIGN KEY (cname) REFERENCES country(cname)
);

CREATE TABLE users(
    id BIGINT,
    email VARCHAR (60),
    name varchar (30),
    surname varchar (40),
    salary INT,
    phone VARCHAR (20),
    cname VARCHAR (50),
    PRIMARY KEY (email),
    FOREIGN KEY (cname) REFERENCES country(cname)
);

CREATE TABLE publicservant(
    id BIGINT,
    email VARCHAR(60),
    department VARCHAR(50),
    FOREIGN KEY (email) REFERENCES users(email) ON DELETE CASCADE
);

CREATE TABLE doctor(
    id BIGINT,    
    email VARCHAR (60),
    degree VARCHAR (20),
    FOREIGN KEY (email) REFERENCES users(email) ON DELETE CASCADE
);

CREATE TABLE specialize(
    id BIGINT,
    disease_id INT,
    email VARCHAR (60),
    FOREIGN KEY (disease_id) REFERENCES diseasetype(id) ON DELETE CASCADE,
    FOREIGN KEY (email) REFERENCES doctor(email) ON DELETE CASCADE
);

CREATE TABLE record(
    id BIGINT,    
    email VARCHAR (60),
    cname VARCHAR (50),
    disease_code VARCHAR(50),
    total_deaths INT,
    total_patients INT,
    FOREIGN KEY (disease_code) REFERENCES disease(disease_code) ON DELETE CASCADE,
    FOREIGN KEY (cname) REFERENCES country(cname) ON DELETE CASCADE,
    FOREIGN KEY (email) REFERENCES publicservant(email) ON DELETE CASCADE
);