# Weather Data ETL Pipeline (Python & SQLite)

## Project Overview
This project establishes an **automated ETL pipeline** (Extract, Transform, Load) designed to retrieve current weather data from an external API and store it in a structured local database.

It demonstrates core Data Engineering skills: working with APIs, processing JSON data, and loading data into a relational database.

## Technology Stack

| Category | Tool | Purpose |

| **Core Language** | Python 3.x | Primary language used for the entire pipeline. |
| **Extract (E)** | `requests` | Handles HTTP requests to the OpenWeatherMap API. |
| **Transform (T)** | `pandas` | Data structuring, time formatting, and creating a DataFrame. |
| **Load (L)** | `sqlite3` | Built-in local database for persistent data storage. |
| **Version Control**| Git / GitHub | Version control and portfolio hosting. |

## Pipeline Structure (ETL)

The ETL process is implemented in the `etl_script.py` file and follows three sequential stages:

### 1. Extract
* The `requests` library is used to send a GET request to the **OpenWeatherMap API**.
* Data is requested for the city of **City** (`CITY = 'Name of city'`).
* A raw **JSON object** containing weather metrics is received.

### 2. Transform
* The `pandas` library is used to handle data processing.
* **Parsing:** Only necessary fields are extracted, including city name, temperature, humidity, and weather description.
* **Cleaning:** The UNIX timestamp is converted into a human-readable date/time format (`YYYY-MM-DD HH:MM:SS`) using the `datetime` module.
* The clean data is structured into a **Pandas DataFrame**.

### 3. Load
* The `sqlite3` module is used to connect to the local database file (`weather_data.db`).
* **Loading:** The cleaned DataFrame is loaded into the `weather_records` table.
* The `if_exists='append'` setting ensures that new records are **added** with each script run, building a historical database over time.

## How to Run the Project

To reproduce the project on your machine:

1.  **Clone the repository:**
    ```bash
    git clone [https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories)
    cd weather-etl-pipeline-python
    ```
2.  **Create and activate the Virtual Environment:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configure API Key:** Insert your active OpenWeatherMap key into the `API_KEY` constant in `etl_script.py`.
5.  **Run the ETL Pipeline:**
    ```bash
    python etl_script.py
    ```

## Future Enhancements (Roadmap)
* Implement **error logging** (status, failures) to a separate log file.
* Transfer the API key to environment variables (`.env`) for improved security.
* Integrate a scheduler (**Cron** or **Apache Airflow**) for daily automatic execution.

---

## Final Steps: Finalization and GitHub

Now, execute the final steps to push this project to GitHub:

1.  **Create `requirements.txt`:** This lists all external libraries needed. Run in your active terminal:
    ```bash
    pip freeze > requirements.txt
    ```
2.  **Final Git Commands:**
    ```bash
    # Add all necessary files (the .db file is excluded by .gitignore)
    git add etl_script.py .gitignore README.md requirements.txt 
    
    # Commit the changes
    git commit -m "feat: Completed full ETL pipeline and added project documentation"
    
    # Push the branch to GitHub (it will now appear online)
    git push --set-upstream origin feat/initial-etl-script
    ```