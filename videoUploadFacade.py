"""Video Upload facade, contains couple of hypothetical services which gets invoked when handling upload video."""


class VideoProcessorService:
    def process_video(self, video_file):
        pass


class MetadataService:
    def extract_metadata(self, video_file):
        pass


class ThumbnailService:
    def generate_thumbnail(self, video_file):
        pass


class NotificationService:
    def notify_users(self, user_info):
        pass


class TagService:
    def add_tags(self, video_file, tags):
        pass


class YouTube:
    def __init__(self):
        self.videoProcessor = VideoProcessorService()
        self.metadataService = MetadataService()
        self.thumbnailService = ThumbnailService()
        self.notificationService = NotificationService()
        self.tagService = TagService()
        # self.tagService = TagService()

    def upload_video_facade(self, video_file, user_info, user_input):
        """Facade method that orchestrates all the sub processes."""
        try:
            self.videoProcessor.process_video(video_file)
            self.metadataService.extract_metadata(video_file)
            self.thumbnailService.generate_thumbnail(video_file)
            self.notificationService.notify_users(user_info)
            self.tagService.add_tags(video_file, user_input["tags"])
            return {"status": "success", "message": "Video uploaded successfully."}
        except Exception as e:
            return {"status": "failure", "error": str(e)}


def get_user_info_from_token():
    pass


# @app.route('/video', methods=['POST'])        
def upload_video(request):  # In flask you will get request within the func.
    """REST API handler for upload video."""
    try:
        # Authenticate and athorize user for upload action from JWT token
        user_info = get_user_info_from_token()
        video_file = request.files['video']
        user_input = {
            "tags": request.form.getlist('tags'),
            "description": request.form.get('description'),
            "privacy": request.form.get('privacy')
        }

        youtube_service = YouTube()  # In a real-world case, this would be injected or initialized at startup
        # result = youtube_service.upload_video_facade(video_file, user_info, user_input)
        return None  # jsonify(result)
    except Exception:
        # General error handling
        return None#jsonify({"status": "failure", "error": str(e)}), 500
