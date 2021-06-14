
-- free_prod_request table ** main table
CREATE TABLE free_prod_request(
	request_id varchar(50) not null, -- 14
    prod_request varchar(50), -- 9
    email varchar(50), -- 2
    constraint request_id_pk primary key (request_id)
    );
    
CREATE TABLE order_table(
	request_id varchar(50), -- 14
	order_id varchar(25) not null, -- 3
	prod_purch varchar(50), -- 5
	age_of_order varchar(50), -- 15
    duplicatebool bool not null default 0,
    experience varchar(50), -- 7
    review varchar(5000), -- 8
	constraint order_id_pk primary key (order_id, prod_purch),
    constraint fk_request_id foreign key (request_id) references free_prod_request (request_id)
    );
    
CREATE TABLE customer_table(
	-- customer_id int(6) not null auto_increment,
    request_id varchar(50), -- 14
    customer_email varchar(50), -- 2
    phone_number varchar(50), -- 4
    first_name varchar(50), -- 0
    last_name varchar(50), -- 1
    constraint customer_email_pk primary key (customer_email),
    constraint request_id_fk foreign key (request_id) references free_prod_request (request_id)
    );
   
-- Address Table 2 
CREATE TABLE addresses(
	-- customer_id varchar(100),
    customer_email varchar(50) not null, -- 2
    address varchar(100), -- 10
    city varchar(100), -- 11
    state varchar(5), -- 12
    zipcode varchar(10), -- 13
    constraint pk_customer_email primary key (customer_email),
    constraint customer_email_fk foreign key (customer_email) references customer_table (customer_email))
    ;

CREATE TABLE updated_name(
	customer_email varchar(50) not null,
    first_name varchar(50),
    last_name varchar(50),
    time_stamp timestamp
    );
    
CREATE TABLE updated_address(
customer_email varchar(50),
address varchar(100), -- 10
city varchar(100), -- 11
state varchar(5), -- 12
zipcode varchar(10), -- 13
time_stamp timestamp)
 ;
 
CREATE TABLE duplicate_requests(
request_id varchar(50), -- 14
order_id varchar(25) not null, -- 3
prod_purch varchar(50), -- 5
age_of_order varchar(50), -- 15
duplicatebool bool not null default 1,
experience varchar(10), -- 7
review varchar(500)
);

    
-- Trigger on repeat order and product entries
DELIMITER //
CREATE TRIGGER Duplicate_Requests
BEFORE INSERT ON order_table
FOR EACH ROW
BEGIN
	IF(EXISTS(SELECT * FROM order_table WHERE order_id = NEW.order_id AND prod_purch = NEW.prod_purch)) THEN
    INSERT INTO duplicate_requests (request_id, order_id, prod_purch, age_of_order, experience, review)
    VALUES (NEW.request_id, NEW.order_id, NEW.prod_purch, NEW.age_of_order, NEW.experience, NEW.review);
    END IF;
    END //
    DELIMITER ;

-- Trigger on updated name    
DELIMITER //
CREATE TRIGGER Change_Name
AFTER UPDATE ON customer_table
FOR EACH ROW
BEGIN
IF(EXISTS(SELECT * FROM customer_table WHERE OLD.customer_email=NEW.customer_email AND OLD.first_name != NEW.first_name OR OLD.last_name != NEW.last_name))
THEN
INSERT INTO updated_name (customer_email, first_name, last_name, time_stamp)
VALUES (OLD.customer_email, OLD.first_name, OLD.last_name, CURRENT_TIMESTAMP);
END IF;
END //
DELIMITER ;

-- Trigger on updated address   
DELIMITER //
CREATE TRIGGER Change_Address
AFTER UPDATE ON addresses
FOR EACH ROW
BEGIN
IF(EXISTS(SELECT * FROM addresses WHERE OLD.customer_email=NEW.customer_email AND OLD.address != NEW.address OR OLD.city != NEW.city OR OLD.state != NEW.state OR OLD.zipcode != NEW.zipcode))
THEN
INSERT INTO updated_address (customer_email, address, city, state, zipcode, time_stamp)
VALUES (OLD.customer_email, OLD.address, OLD.city, OLD.state, OLD.zipcode, CURRENT_TIMESTAMP);
END IF;
END //
DELIMITER ;
    




