import logging

from django.http import JsonResponse
from django.views import View
from django.db import connection

logger = logging.getLogger(__name__)


class HealthCheckView(View):
    def get(self, request, *args, **kwargs):
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
            db_status = "healthy"
        except Exception as e:
            logger.error(e)
            db_status = "unhealthy"

        return JsonResponse({"status": "ok", "components": {"database": db_status}})
