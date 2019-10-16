CREATE TABLE news (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        title VARCHAR(144) NOT NULL,
        content VARCHAR(8000) NOT NULL,
        writer VARCHAR(144) NOT NULL,
        PRIMARY KEY (id)
);

CREATE TABLE tag (
        id INTEGER NOT NULL,
        name VARCHAR(144) NOT NULL,
        PRIMARY KEY (id)
);

CREATE TABLE account (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(144) NOT NULL,
        username VARCHAR(144) NOT NULL,
        password VARCHAR(144) NOT NULL,
        acc_type VARCHAR(144) NOT NULL,
        PRIMARY KEY (id)
);

CREATE TABLE read (
        news_id INTEGER,
        account_id INTEGER,
        FOREIGN KEY(news_id) REFERENCES news (id),
        FOREIGN KEY(account_id) REFERENCES account (id)
);

CREATE TABLE connect (
        news_id INTEGER,
        tag_id INTEGER,
        FOREIGN KEY(news_id) REFERENCES news (id),
        FOREIGN KEY(tag_id) REFERENCES tag (id)
);