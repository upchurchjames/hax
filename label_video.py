import io
import os

from google.cloud import videointelligence

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "uc.json"

video_client = videointelligence.VideoIntelligenceServiceClient()

path = 'cars.mp4'

with io.open(path, 'rb') as movie:
    input_content = movie.read()

features = [videointelligence.enums.Feature.LABEL_DETECTION]

operation = video_client.annotate_video(
    features=features, input_content=input_content)
print('\nProcessing video for label annotations:')

result = operation.result(timeout=120)
print('\nFinished processing.')

# first result is retrieved because a single video was processed
segment_labels = result.annotation_results[0].segment_label_annotations
for i, segment_label in enumerate(segment_labels):
    print('Video label description: {}'.format(
        segment_label.entity.description))
    for category_entity in segment_label.category_entities:
        print('\tLabel category description: {}'.format(
            category_entity.description))

    for i, segment in enumerate(segment_label.segments):
        start_time = (segment.segment.start_time_offset.seconds +
                      segment.segment.start_time_offset.nanos / 1e9)
        end_time = (segment.segment.end_time_offset.seconds +
                    segment.segment.end_time_offset.nanos / 1e9)
        positions = '{}s to {}s'.format(start_time, end_time)
        confidence = segment.confidence
        print('\tSegment {}: {}'.format(i, positions))
        print('\tConfidence: {}'.format(confidence))
    print('\n')