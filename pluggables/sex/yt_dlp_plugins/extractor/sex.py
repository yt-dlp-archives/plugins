from yt_dlp.extractor.common import InfoExtractor
from yt_dlp.utils import traverse_obj, url_or_none, int_or_none, unified_timestamp, float_or_none
import urllib;

class SexShortsIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?sex\.com/(?:\w+/)?shorts/(?P<id>[\w-]+/video/[\w-]+)'
    _TESTS = [{
        'url': 'https://www.sex.com/en/shorts/nightivy/video/do-curls-look-good-on-me',
        'md5': '246d58fbb861c24206812fedb1932fc4',
        'info_dict': {
            'id': '4222a290-ae4e-4b37-a0e5-26cbb0f46c0d',
            'title': 'nightivy-video-do-curls-look-good-on-me',
            'age_limit': 18,
            'thumbnail':
            'https://m2.cdn.sex.com/videos/4222a290-ae4e-4b37-a0e5-26cbb0f46c0d/3c5ed16f-498e-4eea-aa99-d2e8d5b39158_thumbnail.jpg',
            'description': 'Do curls look good on me?',
            'duration': 48.321667,
            'uploader': 'nightivy',
            'uploader_id': '7518ecd4-2f94-40af-ae00-285d9f7dcca6',
            'uploader_url': 'https://m2.cdn.sex.com/pictures/7518ecd4-2f94-40af-ae00-285d9f7dcca6/9471871e-d905-42c5-9919-ddb7b150ea2e_wm',
            'timestamp': 1708542095,
            'release_timestamp': 1708542096,
            'like_count': 250,
            'comment_count': 6,
            'webpage_url': 'https://www.sex.com/en/shorts/nightivy/video/do-curls-look-good-on-me',
            'media_type': 'shorts',
            'tags': ['teen', 'sexybody', 'natural', 'curls', 'onlyfans', 'gfe', 'girl-next-door', 'ass', 'booty', 'naked'],
            'availability':'public',
            'formats': [
                {
                    'url': 'https://m2.cdn.sex.com/videos/4222a290-ae4e-4b37-a0e5-26cbb0f46c0d/df6e55f2-48cd-4b61-b848-9b3002c0b236_full-video_1080p_normal.mp4',
                    'format': 'video/mp4',
                    'format_id': 'FullVideo_1080p_normal',
                    'width': 2160,
                    'height': 3840,
                    'http_headers': {
                        'Referer': 'https://iframe.sex.com/'
                    }
                },
                {
                    'url': 'https://m2.cdn.sex.com/videos/4222a290-ae4e-4b37-a0e5-26cbb0f46c0d/0c2a333e-bc61-439b-a1c0-3ded594c5fd2_full-video_1080p_normal__blurred.mp4',
                    'format': 'video/mp4',
                    'format_id': 'FullVideo_1080p_blurred',
                    'width': 2160,
                    'height': 3840,
                    'http_headers': {
                        'Referer': 'https://iframe.sex.com/'
                        }
                    }
            ]
        }
    }]

    @staticmethod
    def _get_formats(meta: dict) -> list[dict] | None:
        streams: list = traverse_obj(meta, ('media', 'sources'), expected_type=list, default=[])
        return [dict(
            url=stream.get('fullPath'),
            format=stream.get('fileType'),
            format_id=stream.get('quality').replace("-", "_"),
            width=traverse_obj(meta, ('media', 'width'), expected_type=int),
            height=traverse_obj(meta, ('media', 'height'), expected_type=int),
            http_headers=dict(
                Referer="https://iframe.sex.com/"
            )
        ) for stream in streams]

    def _real_extract(self, url):
        rel_url = self._match_id(url)
        meta: dict = self._download_json(f'https://iframe.sex.com/api/media/getMedia?relativeUrl={urllib.parse.quote(rel_url)}', video_id=rel_url)

        return dict(
            id=traverse_obj(meta, ('media', 'videoUid'), expected_type=str),
            title=rel_url.replace("/", "-"),
            age_limit=18,
            thumbnail=traverse_obj(meta, ('media', 'thumbnail', 'fullPath'), expected_type=url_or_none),
            description=traverse_obj(meta, ('media', 'caption'), expected_type=str),
            duration=float_or_none(traverse_obj(meta, ('media', 'originalVideoDuration'), expected_type=float)),
            uploader=traverse_obj(meta, ('media', 'user', 'username'), expected_type=str),
            uploader_id=traverse_obj(meta, ('media', 'user', 'userUid'), expected_type=str),
            uploader_url=traverse_obj(meta, ('media', 'user', 'avatar', 'fullPath'), expected_type=url_or_none),
            timestamp=unified_timestamp(traverse_obj(meta, ('media', 'createdAt'), expected_type=str)),
            release_timestamp=unified_timestamp(traverse_obj(meta, ('media', 'publishAt'), expected_type=str)),
            like_count=traverse_obj(meta, ('media', 'likes'), expected_type=int_or_none),
            comment_count=traverse_obj(meta, ('media', 'totalCommentsCount'), expected_type=int_or_none),
            webpage_url=url,
            media_type='shorts',
            tags=traverse_obj(meta, ('media', 'tags'), expected_type=list),
            availability=traverse_obj(meta, ('media', 'visibility'), expected_type=str),
            formats=SexDotComShortsIE._get_formats(meta),
        )