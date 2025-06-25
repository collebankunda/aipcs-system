
CREATE TABLE IF NOT EXISTS projects (
    id UUID PRIMARY KEY,
    name VARCHAR(255),
    location VARCHAR(255),
    client VARCHAR(100),
    budget DECIMAL(18,2),
    start_date DATE,
    end_date DATE,
    status VARCHAR(20)
);
