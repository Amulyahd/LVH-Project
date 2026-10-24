"""Empty dashboard service for website demo mode."""

class DashboardService:
    def log_prediction(self, *args, **kwargs):
        pass

    def get_analytics_data(self, *args, **kwargs):
        return {}

    def get_usage_analytics(self, *args, **kwargs):
        return {}

    def get_performance_metrics(self, *args, **kwargs):
        return {}

    def get_system_metrics(self, *args, **kwargs):
        return {"mode": "demo", "models_available": 0}

    def get_recent_predictions(self, *args, **kwargs):
        return []

    def get_model_performance(self, *args, **kwargs):
        return {}

    def cleanup_old_data(self, *args, **kwargs):
        pass

dashboard_service = DashboardService()
