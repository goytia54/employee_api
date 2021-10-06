### Michael Goytia's Awesome Employee API

* Runs on python3 so create a virtual env in the same directory as `app.py` or `python3 -m venv venv`
* activate the `venv` by running `source venv/bin/activate`
* run `pip install -r requirements` to get all deps
* `export PORT=<desired port>` to set port for api run and curl cmd 
* run api with `flask run --port=$PORT` 
* curl localhost:$PORT/employees
* when all done type `deactivate` to get out of virtual env