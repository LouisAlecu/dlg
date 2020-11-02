from flask import Blueprint, jsonify, request
from functs import get_total

total_blueprint = Blueprint("data", __name__)


@total_blueprint.route("/total", methods=["GET"], endpoint="total")
def total():
    """
    Endpoint to return the sum of a list. For now hardcode the request_list, so the endpoint returns the same number
    """
    # request_data = request.get_json()
    # list_in_request = request_data['somelist']

    list_in_request = list(range(10000001))
    return_data = get_total(list_in_request)

    return jsonify({"total": return_data})
