import requests

from requests.models import Response


def main():
    text = """
    {
	"message": null,
	"results": [
		{
			"address1": "東京都",
			"address2": "足立区",
			"address3": "大谷田",
			"kana1": "ﾄｳｷｮｳﾄ",
			"kana2": "ｱﾀﾞﾁｸ",
			"kana3": "ｵｵﾔﾀ",
			"prefcode": "13",
			"zipcode": "1200001"
		}
	],
	"status": 200
}"""
    import json

    print(json.loads(text))


if __name__ == '__main__':
    main()
