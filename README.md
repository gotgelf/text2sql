# Text2SQL: Transform Natural Language to SQL

Text2SQL is an open-source project designed to leverage the power of language models in order to convert natural language into SQL queries. 

At its core, Text2SQL utilizes the [LangChain framework](https://python.langchain.com/docs/get_started/introduction.html), a robust platform for developing applications that are powered by language models. For the user interface, we have employed the [Streamlit framework](https://streamlit.io), making our project both interactive and visually appealing. 

The primary objective of Text2SQL is to provide a blueprint for transforming human text into SQL queries. As such, our project is an ideal starting point for anyone interested in exploring the intersection of natural language processing and database querying. 

Additionally, Text2SQL is designed with flexibility in mind. It can be adjusted to work with any SQL dialect that's supported by SQLAlchemy, making it compatible with a wide range of databases, including MS SQL, MySQL, MariaDB, PostgreSQL, Oracle SQL, Databricks, and SQLite.

## 🏃‍♀️ How to Run It Locally

Here are the steps to run Text2SQL on your local machine:

1. **Clone the repository**: Use the following command in your terminal to clone the repository: `git clone https://github.com/gotgelf/text2sql.git`

2. **Install dependencies**: Navigate to the directory where you cloned the repository and install the necessary dependencies by running: `pip install -r requirements.txt`

3. **Run the application**: Start the application using the command: `streamlit run app.py`

## Demo Database

For demonstration purposes, Text2SQL uses a SQLite database named `movie.sqlite` that is publicly available on Kaggle. This database contains two tables, `directors` and `movies`. You can download it from [here](https://www.kaggle.com/datasets/divyaanshiee/moviesqlite?resource=download).

The demo version of Text2SQL is configured to generate SQL queries compatible with this SQLite database. This allows you to see the project in action immediately after setup. 

Please note that Text2SQL can be configured to work with any SQL dialect supported by SQLAlchemy. Therefore, you are not limited to SQLite for your own use case.

### Directors Table Sample Data

| id    | name             | gender | uid    | department |
|-------|------------------|--------|--------|------------|
| 4762  | James Cameron    | 2      | 2710   | Directing  |
| 4763  | Gore Verbinski   | 2      | 1704   | Directing  |
| 4764  | Sam Mendestt     | 2      | 39     | Directing  |


### Movies Table Sample Data

| id | original_title | budget | popularity | release_date | revenue | title | vote_average | vote_count | overview | uid |
|----|----------------|--------|------------|--------------|---------|-------|--------------|------------|----------|-----|
| 43597  | Avatar | 237000000 | 150  | 2009-12-10   | 2787965087 | Avatar | 7.2  | 11800 | In the 22nd century, a paraplegic Marine is dispatched to the moon Pandora on a unique mission, but ... | 43597   |
| 43598  | Pirates of the Caribbean: At World's End | 300000000 | 139 | 2007-05-19   | 961000000 | Pirates of the Caribbean: At World's End | 6.9  | 4500 | Captain Barbossa, long believed to be dead, has come back to life and is headed to the edge of the E... | 43598 |
| 43599  | Spectre | 245000000  | 107  | 2015-10-26   | 880674609  | Spectre | 6.3  | 4466  | A cryptic message from Bond’s past sends him on a trail to uncover a sinister organization. While M ... | 43599 |

### Example Questions

Text2SQL app can help you translate natural language questions into SQL queries. Here are a few examples:

1. **List the top 10 popular movies.**
   
2. **List the director with the maximum number of movies.**
   
3. **Which movie was the most expensive?**
   
4. **Which movie has the greatest revenue?**
   
5. **Which movie has the best rating?**
   
Feel free to explore different questions and see how Text2SQL can assist you in generating SQL queries from natural language inputs.

## Connecting to a Different Database

To connect the Text2SQL application to any SQL database supported by SQLAlchemy, you will need to update the app.py file.

On line 43, we have the following code:

```python
db = SQLDatabase.from_uri(
    "sqlite:///data/movie.sqlite"
)
```

Replace the SQLite connection string with a connection string appropriate for your database.

For example, to connect to a PostgreSQL database, use:

```python
db = SQLDatabase.from_uri(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"        
)
```

Replace {DB_USER}, {DB_PASSWORD}, {DB_HOST}, {DB_PORT}, and {DB_NAME} with your actual PostgreSQL database credentials.

Please consult the SQLAlchemy documentation for more details on connecting to other types of databases.

## 🚀 Roadmap

The roadmap for Text2SQL is currently being outlined. Please stay tuned for updates. Your suggestions and contributions are always welcome!

## 📝 License

This project is licensed under the terms of the MIT license.
