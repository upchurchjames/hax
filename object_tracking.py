"""Object Tracking."""
import os
import io

from google.cloud import videointelligence_v1p2beta1 as videointelligence

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "uc.json"

video_client = videointelligence.VideoIntelligenceServiceClient()
features = [videointelligence.enums.Feature.OBJECT_TRACKING]

path = 'lights.mp4'

with io.open(path, 'rb') as file:
    input_content = file.read()

# It is recommended to use location_id as 'us-east1' for the best latency
# due to different types of processors used in this region and others.
operation = video_client.annotate_video(
    input_content=input_content, features=features, location_id='us-east1')
print('\nProcessing video for object annotations.')

result = operation.result(timeout=300)
print('\nFinished processing.\n')

# The first result is retrieved because a single video was processed.
object_annotations = result.annotation_results[0].object_annotations
entities = []

for i, object_annotation in enumerate(object_annotations):
    if object_annotation.entity.entity_id:
        entities.append(object_annotation.entity.entity_id);

print(entities)
