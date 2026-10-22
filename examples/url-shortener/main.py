from __future__ import annotations

from typing import Dict


class URLShortener:
    def __init__(self):
        self.mapping: Dict[str, str] = {}
        self.counter = 1

    def shorten(self, long_url: str) -> str:
        short_code = self._encode(self.counter)
        self.mapping[short_code] = long_url
        self.counter += 1
        return short_code

    def resolve(self, short_code: str) -> str:
        return self.mapping[short_code]

    def _encode(self, n: int) -> str:
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        if n == 0:
            return alphabet[0]

        code = ""
        while n > 0:
            n, rem = divmod(n, len(alphabet))
            code = alphabet[rem] + code
        return code


if __name__ == "__main__":
    service = URLShortener()
    original = "https://example.com/very/long/path"
    short_code = service.shorten(original)
    print(f"Short code: {short_code}")
    print(f"Long URL: {service.resolve(short_code)}")
