CREATE TYPE plan_t AS ENUM (
       'PLAN_A',
       'PLAN_A+',       
       'PLAN_B'
);


CREATE TABLE accounts (
       id SERIAL PRIMARY KEY,
       client_name TEXT NOT NULL,
       credits NUMERIC(12,4) NOT NULL DEFAULT 0,
       plan plan_t NOT NULL DEFAULT 'PLAN_A',
       ctime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
       mtime TIMESTAMP
);


-- plpgsql
CREATE FUNCTION update_mtime()
       RETURNS TRIGGER
AS $$
   BEGIN
	NEW.mtime = NOW();
	RETURN NEW;
   END
$$
LANGUAGE plpgsql;


CREATE TRIGGER trg_accounts_update_mtime BEFORE UPDATE
    ON accounts FOR EACH ROW EXECUTE PROCEDURE update_mtime();


CREATE TABLE phone_numbers (
       id SERIAL PRIMARY KEY,
       phone_number TEXT NOT NULL UNIQUE,
       account_id INTEGER DEFAULT NULL REFERENCES accounts(id)
           ON UPDATE CASCADE ON DELETE CASCADE
);
