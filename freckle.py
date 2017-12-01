import requests
import json
import datetime

FRECKLE_API_VERSION = '0.0.1'


class FreckleClientV2(object):
    def __init__(self, access_token):
        """
        Creates a ``FreckleClient`` instance.
        :access_token: Your Freckle API token.
        """
        self.access_token = access_token

    def log_entry(self, uri_path, data={}):

        # set content type and accept headers to handle JSON
        headers = {
            'Accept': 'application/json',
            'User-Agent': 'freckle_api/{}'.format(FRECKLE_API_VERSION),
            'X-FreckleToken': self.access_token
        }

        # construct the full URL without query parameters
        url = 'https://api.letsfreckle.com/v2/{0}/'.format(uri_path)

        # perform the HTTP requests, if possible uses OAuth authentication
        response = requests.request('POST', url, headers=headers, data=json.dumps(data))

        # if request failed (i.e. HTTP status code not 20x), raise appropriate
        # error
        response.raise_for_status()

        return {
            'status': response.status_code,
            'user': response.json().get('user'),
            'freckle_dashboard': 'https://andela.letsfreckle.com/time/dashboard/recent',
            'date': data.get('date')
        }
