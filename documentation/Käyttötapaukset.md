Käyttötapaukset, ja niiden SQL-kyselyt

- Käyttäjä avaa etusivun, ja näkee viimeisimmät lisätyt uutiset.

	SELECT * FROM News;

- Käyttäjä luo käyttäjän

	INSERT INTO account (date_created, date_modified, name, username, password, acc_type) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?)

- Käyttäjä kirjautuu sisään

	SELECT account.id AS account_id, account.date_created AS account_date_created, account.date_modified AS account_date_modified, account.name AS account_name, account.username AS account_username, account.password AS account_password, account.acc_type AS account_acc_type
		FROM account
		WHERE account.id = ?

- Käyttäjä näkee lukemansa artikkelit sivun oikeasta laidasta

	SELECT News.* FROM News,read,account WHERE account.id = ? AND read.news_id = News.id AND read.account_id = account.id;

- Käyttäjä menee kategorian sivulle ja painaa kategorian nimeä nähdäkseen kaikki kategoriaan kuuluvat artikkelit

	SELECT News.* FROM News,Connect,Tag WHERE tag.id = ? AND Connect.news_id = News.id AND Connect.tag_id = Tag.id;

- Käyttäjä menee lukemaan uutisartikkelia, ja näkee sivulla artikkelin tekstin

	SELECT * FROM News WHERE id = ?;

- Artikkelin alla kerrotaan artikkelin lukeneiden käyttäjien määrä

	SELECT COUNT(*) accounts_id FROM read,news WHERE news.id = ? AND read.news_id = news.id;

- Artikkelin alla kerrotaan myös artikkeliin liittyvät kategoriat

	SELECT Tag.* FROM News,Connect,Tag WHERE news.id = ? AND Connect.news_id = News.id AND Connect.tag_id = Tag.id;

