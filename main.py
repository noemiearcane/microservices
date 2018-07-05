from flask import Flask, jsonify, abort, make_response, request, url_for
import connexion

#Create the application instance
app = connexion.App(__name__)

#Read the swagger.yml file to configure the endpoints
app.add_api('app.yaml')


if __name__ == "__main__":
    app.run(debug=True)
