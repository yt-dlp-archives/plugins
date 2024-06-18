from yt_dlp.extractor.unsupported import KnownDRMIE, KnownPiracyIE
import yt_dlp.extractor.common
import yt_dlp.YoutubeDL

def noop(*args, **kwargs):
    pass

yt_dlp.extractor.common.InfoExtractor.report_drm = noop

class KnownDRMIE_uncensoredIE(KnownDRMIE, plugin_name='uncensored'):
    IE_DESC = False
    _VALID_URL = False

class KnownPiracyIE_uncensoredIE(KnownPiracyIE, plugin_name='uncensored'):
    IE_DESC = False
    _VALID_URL = False