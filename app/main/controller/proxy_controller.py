from flask import request
from flask_restx import Resource

from app.main.util.decorator import ip_path_combo_limiter, ip_limiter, path_limiter
from ..util.dto import AccessLogsDto
from ..service.proxy_service import ProxyService

api = AccessLogsDto.api


@api.route("/", defaults={"path": ""})
@api.route("/<path:path>")
class ProxyController(Resource):
    @ip_limiter
    @path_limiter
    @ip_path_combo_limiter
    def get(self, path):
        response = ProxyService.handle_request(request)
        return response

    @ip_limiter
    @path_limiter
    @ip_path_combo_limiter
    def post(self, path):
        response = ProxyService.handle_request(request)
        return response

    @ip_limiter
    @path_limiter
    @ip_path_combo_limiter
    def put(self, path):
        response = ProxyService.handle_request(request)
        return response

    @ip_limiter
    @path_limiter
    @ip_path_combo_limiter
    def delete(self, path):
        response = ProxyService.handle_request(request)
        return response
