CREATE TABLE webhook_registrations (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    url VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE event_types (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT
);

CREATE TABLE webhook_configurations (
    id INT PRIMARY KEY AUTO_INCREMENT,
    webhook_id INT NOT NULL,
    event_type_id INT NOT NULL,
    custom_headers TEXT,  
    custom_payload TEXT, 
    FOREIGN KEY (webhook_id) REFERENCES webhook_registrations(id),
    FOREIGN KEY (event_type_id) REFERENCES event_types(id)
);

CREATE TABLE error_log (
    id INT PRIMARY KEY AUTO_INCREMENT,
    webhook_execution_id INT NOT NULL,
    error_message TEXT NOT NULL,
    retry_count INT DEFAULT 0,
    next_retry_time TIMESTAMP,
    FOREIGN KEY (webhook_execution_id) REFERENCES webhook_executions(id)
);