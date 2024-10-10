# https://github.com/yt-dlp/yt-dlp/blob/master/CONTRIBUTING.md#developer-instructions
# https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/extractor/common.py
import re, os

from yt_dlp.utils import get_element_by_id, traverse_obj
from yt_dlp.utils._utils import _UnsafeExtensionError
from yt_dlp.extractor.common import InfoExtractor


class BunkrVideoIE(InfoExtractor):
    _TYPE = 'url'
    _VALID_URL = r'^https://bunkr+\.\w+/v/(?P<id>\S+)$'

    def _real_extract(self, url):
        url_id = self._match_id(url)
        webpage = self._download_webpage(url, url_id)

        name = self._html_search_regex('data-v="([^"]*)"', webpage, 'name')
        file_id = self._html_search_regex('data-file-id="([^"]*)"', webpage, 'file_id')
        video = self._html_search_regex('<source src="([^"]*)" type="video/mp4" />', webpage, 'video')

        return {
            'id': file_id,
            'title': os.path.splitext(name)[0],
            'formats': [{
                'url': video,
            }],
        }

class BunkrImageIE(InfoExtractor):
    _TYPE = 'url'
    _VALID_URL = r'^https://bunkr+\.\w+/i/(?P<id>\S+)$'

    def _real_extract(self, url):
        url_id = self._match_id(url)
        webpage = self._download_webpage(url, url_id)

        name = self._html_search_regex('data-v="([^"]*)"', webpage, 'name')
        file_id = self._html_search_regex('data-file-id="([^"]*)"', webpage, 'file_id')
        image = self._html_search_regex('<img src="([^"]*)"', webpage, 'image')

        return {
            'id': file_id,
            'title': os.path.splitext(name),
            'formats': [{
                'url': image,
                'ext': ext,
            }],
        }

class BunkrArchiveIE(InfoExtractor):
    _TYPE = 'url'
    _VALID_URL = r'^https://bunkr+\.\w+/d/(?P<id>\S+)$'

    def _real_extract(self, url):
        # Add archive formats to allowed downloads
        _UnsafeExtensionError.ALLOWED_EXTENSIONS = frozenset([*_UnsafeExtensionError.ALLOWED_EXTENSIONS, 'zip', 'rar'])

        url_id = self._match_id(url)
        webpage = self._download_webpage(url, url_id)

        name = self._html_search_regex('data-v="([^"]*)"', webpage, 'name')
        file_id = self._html_search_regex('data-file-id="([^"]*)"', webpage, 'file_id')
        download_url = self._html_search_regex(f'href="([^"]*/{file_id})"', webpage, 'download_url')

        download_webpage = self._download_webpage(download_url, file_id)
        download = self._html_search_regex(f'href="([^"]*/{name})"', download_webpage, 'download')

        return {
            'id': file_id,
            'title': os.path.splitext(name),
            'formats': [{
                'url': download,
            }],
        }


class BunkrAlbumIE(InfoExtractor):
    _TYPE = 'url'
    _VALID_URL = r'^https://bunkr+\.\w+/a/(?P<id>\S+)$'

    def _real_extract(self, url):
        album_id = self._match_id(url)
        webpage = self._download_webpage(url, album_id)

        links = re.findall(r'href="(https://bunkr+\.\w+/(?:v|i|d)/\S+)"', webpage)
        return self.playlist_result((self.url_result(link) for link in links), album_id, album_id)
