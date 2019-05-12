import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/names<br/>"
        f"/api/v1.0/passengers"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    """Convert the query results to a Dictionary using `date` as the key and `prcp` as the value."""
    # Query all measurements
    results = session.query(Measurement.date, Measurement.prcp).all()

    # Create a dictionary from the row data and append to a list of all_passengers
    all_measurements = []
    for name, age, sex in results:
        measurement_dict = {}
        measurement_dict["date"] = date
        measurement_dict["prcp"] = prcp
        all_measurements.append(measurement_dict)

    return jsonify(all_measurements)




@app.route("/api/v1.0/stations")
def stations():
    """Return a list of all stations"""
    # Query all passengers
    results = session.query(Station.name).all()

    # Convert list of tuples into normal list
    all_stations = list(np.ravel(results))

    return jsonify(all_stations)




@app.route("/api/v1.0/tobs")
def tobs():
    """Query for the dates and temperature observations from a year from the last data point."""
    # Query measurements
    results = session.query(Measurement.date, Measurement.tobs).filter(Mearsurement.date >= '2016-08-23')

    # Create a dictionary from the row data and append to a list of all_passengers
    all_tobs = []
    for date, tobs in results:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
        all_tobs.append(tobs_dict)

    return jsonify(all_tobs)




if __name__ == '__main__':
    app.run(debug=True)
