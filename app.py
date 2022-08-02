# Regular depencies

import datetime as dt
import numpy as np
import pandas as pd

# SQLAlchemy dependencies

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Flask dependency

from flask import Flask, jsonify

# Create engine

engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect the database into our classes

Base = automap_base()

# Reflect the database

Base.prepare(engine, reflect=True)

# Create variable for each class to make it easier for referencing later

Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link from Python to our database

session = Session(engine)

# Define the flask app

app = Flask(__name__)

# Define welcome route aka "root"

@app.route("/")

# Add routing info

def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# Build precipitation analysis route

@app.route("/api/v1.0/precipitation")

def precipitation():

    prev_year = dt.date(2017,8,23) - dt.timedelta(days=365)

    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()

    precip = {date: prcp for date, prcp in precipitation}

    return jsonify(precip)

# Build station route

@app.route("/api/v1.0/stations")

def stations():

    results = session.query(Station.station).all()

    stations = list(np.ravel(results))

    return jsonify(stations=stations)

# Build temperature route

@app.route("/api/v1.0/tobs")

def temp_monthly():

    prev_year = dt.date(2017,8,23) - dt.timedelta(days=365)

    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()

    temps = list(np.ravel(results))    

    return jsonify(temps=temps)

# Build two routes for starting and ending dates

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

def stats(start=None, end=None):

    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))

        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)