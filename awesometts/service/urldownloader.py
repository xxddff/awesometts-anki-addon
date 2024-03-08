import json
from .base import Service
from .common import Trait

__all__ = ['URLDownloader']

# 仅支持ja
VOICES = {
    'ja': '日语',
}

class URLDownloader(Service):
    """
    Provides a Service-compliant implementation for URLDownloader.
    """

    __slots__ = []

    NAME = "URL下载"

    TRAITS = [Trait.INTERNET, Trait.DICTIONARY]

    def desc(self):
        """Returns a short, static description."""

        return "URL下载"

    def options(self):
        """Provides access to voice only."""

        return [
            dict(
                key='voice',
                label="语言",
                values=[(code, "%s (%s)" % (name, code))
                        for code, name
                        in sorted(VOICES.items(), key=lambda t: t[1])],
                transform=self.normalize,
            ),
        ]

    def run(self, text, options, path):

        # from urllib.parse import quote
        # url = 'https://apicorporate.forvo.com/api2/v1.1/d6a0d68b18fbcf26bcbb66ec20739492/word-pronunciations/word/%s/language/%s/order/rate-desc' % (
        #     quote(text.encode('utf-8')),
        #     quote(options['voice'])
        # )

        # payload = self.net_stream(url)
        #
        # try:
        #     data = json.loads(payload)
        # except ValueError:
        #     raise ValueError("无法获取来自URL的响应")

        # try:
        #     audio_url = data['data']['items'][0]['realmp3']
        # except KeyError:
        #     raise KeyError("在来自Forvo API的响应中找不到音频URL")
        # except IndexError:
        #     raise IOError("Forvo没有此音频。")

        try:
            audio_url = text
        except:
            raise KeyError("未知错误")

        self.net_download(
            path,
            audio_url,
        )