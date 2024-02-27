CREATE TABLE webhook_registrations (
    id  UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    user_id INT NOT NULL,
    url VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
);

CREATE TABLE event_types (
    id   UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT
);

CREATE TABLE webhook_configurations (
    id  UUID DEFAULT gen_random_uuid()  PRIMARY KEY,
    webhook_id UUID NOT NULL,
    event_type_id UUID NOT NULL,
    custom_headers JSON,  
    custom_payload JSON, 
    FOREIGN KEY (webhook_id) REFERENCES webhook_registrations(id),
    FOREIGN KEY (event_type_id) REFERENCES event_types(id)
);

INSERT INTO event_types (name, description)
VALUES ('upload file', 'Event type for file upload operations');