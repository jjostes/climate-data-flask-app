from flask import Flask, jsonify

import sqlalchemy
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

import numpy as np
import datetime as dt

engine = create_engine('sqlite:///Resources/hawaii.sqlite')
Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

app = Flask(__name__)

#Creating flask routes
@app.route('/')
def welcome():
    return (
        f'Available Routes: </br>'
        f'/api/v1.0/precipitation: </br>'
        f'/api/v1.0/stations: </br>'
        f'/api/v1.0/tobs: </br>'
        f'/api/v1.0/<start>: (enter: yyyy-mm-dd)</br>'
        f'/api/v1.0/<start>/<end>: (enter: yyyy-mm-dd/yyyy-mm-dd)'
    )
#Returns precipitation dictionary
@app.route('/api/v1.0/precipitation')
def precipitation():
    session = Session(engine)

    results = session.query(Measurement.date, Measurement.prcp).order_by(Measurement.date.desc()).all()

    session.close()

    dictionary = {}

    for d,p in results:
        dictionary.update({d:p})

    return jsonify(dictionary)

#returns list of stations
@app.route('/api/v1.0/stations')
def stations():
    session = Session(engine)

    results = session.query(Station.station, Station.name).all()
    
    session.close()

    station_list = []

    for s,n in results:
        station_list.append((s,n))

    return jsonify(station_list)


#returns json list of last 12 months of temperature observations for the most active station
#I wasn't sure if I could use the answers from jupyter notebook and not re-query, but I went ahead
#   and re-queried again under the assumption it is better that this run independent from the other. 
@app.route('/api/v1.0/tobs')
def tobs():
    session = Session(engine)

    year_ago = dt.datetime(2017,8,22) - dt.timedelta(weeks=52)

    most_active = session.query(func.count(Measurement.station), Measurement.station).\
                    group_by(Measurement.station).\
                    order_by(func.count(Measurement.station).desc()).first()

    tobs_last12 = session.query(Measurement.date, Measurement.tobs).\
                    filter(Measurement.date > year_ago).\
                    filter(Measurement.station == most_active[1]).all()

    session.close()

    return jsonify(tobs_last12)


@app.route('/api/v1.0/<start>')
def start_date(start):
    session = Session(engine)

    result = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                filter(Measurement.date >= start).all()
    
    session.close()
    
    return jsonify(result)

@app.route('/api/v1.0/<start>/<end>')
def start_end(start, end):
    session = Session(engine)

    result = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                filter(Measurement.date >= start).\
                filter(Measurement.date <= end).all()
    
    session.close()
    
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)

