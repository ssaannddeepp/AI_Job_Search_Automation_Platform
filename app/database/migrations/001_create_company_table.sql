create table company (
	company_id serial primary key,
	company_name varchar(255) not null unique,
	website varchar(255),
	industry varchar(100),
	linkedin_url varchar(255),
	career_page_url varchar(255),
	created_at timestamptz not null default current_timestamp,
	updated_at timestamptz not null default current_timestamp
);