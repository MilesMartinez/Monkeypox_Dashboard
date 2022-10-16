# Monkeypox Dashboard

Dashboard for tracking the spread of Monkeypox. Check it out [here](https://public.tableau.com/app/profile/miles6013/viz/MonkeypoxDashboard_16592277053130/Dashboard1).

![Screenshot of Monkeypox Dashboard](dashboard.png)

Note: Daily batch load is currently suspended. Dashboard was last updated September 9, 2022.

## Methodology

The dashboard is desighed to update daily with the latest reported monkeypox cases. The ETL is as follows.

![Monkeypox ETL Flowchart](diagram.png)

The Lamda function executes a python script that submits a GET request to a URL on this [GitHub repo](https://github.com/globaldothealth/monkeypox) containing a JSON file (which is no longer being uploaded), converts it into a Pandas dataframe, and then loads it into a PostgreSQL database hosted on Amazon RDS.
