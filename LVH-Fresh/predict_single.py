class LVHPredictor:
    """Safe demo placeholder; no trained medical model is available."""
    def __init__(self, models_dir=None):
        self.models = {}

    def predict(self, file_path, modality=None):
        raise RuntimeError(
            "Demo mode: no trained LVH model is available. "
            "No medical prediction was made."
        )
