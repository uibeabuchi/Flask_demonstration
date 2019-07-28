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
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB


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
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        
    )


@app.route("/api/v1.0/names")
def names():
    """Return a list of all passenger names"""
    # Query all passengers
    session = Session(engine)
    results = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >='2016-08-23').\
    filter(Measurement.date <='2017-08-23').all()

    # Convert list of tuples into normal list
    all_prcp = list(np.ravel(results))
    #all_names = [name[0] for name in results]

    return jsonify(all_prcp)


# @app.route("/api/v1.0/stations")
# def stations():
#     """Return a list of passenger data including the name, age, and sex of each passenger"""
#     # Query all passengers
#     session = Session(engine)
#     results = session.query(func.count(Station.station)).all()

#     # Create a dictionary from the row data and append to a list of all_passengers
#     all_stations = []
#     for stations in results:
#         station_dict = {}
#         station_dict["id"] = id
#         station_dict["station"] = station
#         station_dict["name"] = name
#         all_stations.append(station_dict)

#     return jsonify(all_stations)


if __name__ == '__main__':
    app.run(debug=True)
