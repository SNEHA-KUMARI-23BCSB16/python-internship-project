
# calling Blueprint and jsonify class from flask package
from flask import Blueprint,jsonify

# assining an error object to error blueprint
error= Blueprint('errors',__name__)

# server-client request error it gets executed when the particular page is not fiund by server 
@error.app_errorhandler(404)
def not_found_error(error):
    return jsonify({"error":"Resource not found"}),404

# server-client request error where serve doesn't process the request of client
@error.app_errorhandler(400)
def bad_request_error(error):
    return jsonify({"error":"Bad request"}),400

# an internal server error mainly due to unexpected condition
@error.app_errorhandler(500)
def internal_error(error):
    return jsonify({"error":"Internal server error"}),500