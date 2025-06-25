
-- Material Requests Table
CREATE TABLE material_requests (
    id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(id),
    boq_item_id INTEGER,
    quantity_requested INTEGER,
    status VARCHAR(50) DEFAULT 'pending',
    requested_by INTEGER REFERENCES users(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Material Deliveries Table
CREATE TABLE material_deliveries (
    id SERIAL PRIMARY KEY,
    request_id INTEGER REFERENCES material_requests(id),
    quantity_delivered INTEGER,
    delivery_date DATE,
    delivery_note TEXT,
    dispatched_by INTEGER REFERENCES users(id)
);

-- Site Inventory Table
CREATE TABLE site_inventory (
    id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(id),
    boq_item_id INTEGER,
    quantity_on_site INTEGER DEFAULT 0,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
