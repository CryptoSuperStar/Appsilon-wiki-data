# Appsilon-wiki-data

1,2. Get some raw data from  https://query.wikidata.org/  and save data to SQLite.

Install the necessary Python packages using pip:

pip install requests sqlite3

Run the script by executing the command:

python getJson.py

This will run the script and retrieve a list of movies that were released after 2013 from Wikidata using a SPARQL query. 
The movie data will then be stored in a local SQLite database, and the data for any movies that were already stored in the database will be updated.

If the script runs successfully, the data should be stored in the movie.db file in the same directory where the script is located.

3. Show data in SQLite using Flask-AppBuilder.

Open a terminal or command prompt in your project directory.

Activate your Python virtual environment (if you're using one) by running the appropriate command for your operating system. For example, on Mac/Linux, you can run:

source venv/bin/activate
On Windows, you can run:

venv\Scripts\activate
Run your Flask application by executing the python app.py command on the command line:

python app.py
If everything is setup correctly, Flask should provide a message saying something like:

Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
Open a web browser and navigate to the address provided in the message (e.g. http://127.0.0.1:5000/) to view the Flask website.

That's it! Your Flask application should now be up and running.