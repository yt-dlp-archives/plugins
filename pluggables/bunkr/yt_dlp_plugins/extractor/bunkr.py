import re

from yt_dlp.utils import get_element_by_id, traverse_obj
from yt_dlp.utils._utils import _UnsafeExtensionError
from yt_dlp.extractor.common import InfoExtractor


class BunkrVideoIE(InfoExtractor):
    _TYPE = 'url'
    _VALID_URL = r'^https://bunkr+\.\w+/v/(?P<id>\S+)$'

    def _real_extract(self, url):
        file_id = self._match_id(url)
        webpage = self._download_webpage(url, file_id)

        video = self._html_search_regex('<source src="([^"]*)" type="video/mp4" />', webpage, 'video')
        name = self._html_search_regex('data-v="([^"]*)"', webpage, 'name')

        return {
            'id': file_id,
            'title': name,
            'formats': [{
                'url': video,
            }],
        }

class BunkrImageIE(InfoExtractor):
    _TYPE = 'url'
    _VALID_URL = r'^https://bunkr+\.\w+/i/(?P<id>\S+)$'

    def _real_extract(self, url):
        file_id = self._match_id(url)
        webpage = self._download_webpage(url, file_id)

        image = self._html_search_regex('<img src="([^"]*)"', webpage, 'image')
        name = self._html_search_regex('data-v="([^"]*)"', webpage, 'name')

        return {
            'id': file_id,
            'title': name,
            'formats': [{
                'url': image,
            }],
        }

class BunkrArchiveIE(InfoExtractor):
    _TYPE = 'url'
    _VALID_URL = r'^https://bunkr+\.\w+/d/(?P<id>\S+)$'

    def _real_extract(self, url):
        # Add archive formats to allowed downloads
        _UnsafeExtensionError.ALLOWED_EXTENSIONS = frozenset([*_UnsafeExtensionError.ALLOWED_EXTENSIONS, 'zip', 'rar'])

        file_id = self._match_id(url)
        webpage = self._download_webpage(url, file_id)

        name = self._html_search_regex('data-v="([^"]*)"', webpage, 'name')
        url_id = self._html_search_regex('data-file-id="([^"]*)"', webpage, 'url_id')
        download_url = self._html_search_regex(f'href="([^"]*/{url_id})"', webpage, 'download_url')

        download_webpage = self._download_webpage(download_url, url_id)
        download = self._html_search_regex(f'href="([^"]*/{name})"', download_webpage, 'download')

        return {
            'id': file_id,
            'title': name,
            'formats': [{
                'url': download,
                'ext': 'zip',
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
