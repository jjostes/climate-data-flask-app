# Climate Data Flask App

<!-- ABOUT THE PROJECT -->
## About The Project

This project uses Python and SQLAlchemy to do basic climate analysis and data exploration of a climate database [Resources/hawaii.sqlite], specifically temperature observation data (TOBS) . The following analysis was completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

## Usage

### Precipitation

Queried the last 12 months of precipitation data from all stations

![chart]

### Station

Designed a query to find the most active weather station, and from this plotted a histogram of activity for the last 12 months

![histogram] 

### Flask App

Home page with routes listed

can return min, avg, and max temperatures on a given date

  * Home page.

  * List all routes that are available.

* `/api/v1.0/precipitation`

  * Convert the query results to a dictionary using `date` as the key and `prcp` as the value.

  * Return the JSON representation of your dictionary.

* `/api/v1.0/stations`

  * Return a JSON list of stations from the dataset.

* `/api/v1.0/tobs`
  * Query the dates and temperature observations of the most active station for the last year of data.
  
  * Return a JSON list of temperature observations (TOBS) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

  * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.


<!-- CONTACT -->
## Contact

John Jostes - [https://www.linkedin.com/in/john-jostes-386b841a0/](https://www.linkedin.com/in/john-jostes-386b841a0/)

Project Link: [https://github.com/jjostes/climate-data-flask-app](https://github.com/jjostes/climate-data-flask-app)

<!-- MARKDOWN LINKS & IMAGES -->
[chart]: https://github.com/jjostes/climate-data-flask-app/tree/master/Figures/Precipitation.png
[histogram]: https://github.com/jjostes/climate-data-flask-app/tree/master/Figures/histogram.png

