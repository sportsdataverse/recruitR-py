import json
from recruitR.library import http


try:
    from recruitR.library.debug import RECRUIT_HEADERS
except ImportError:
    RECRUIT_HEADERS = {
        'Host': '247sports.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
        'Accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'x-tfs-guest': 'true',
        'Connection': 'keep-alive',
        'Referer': 'https://247sports.com/',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }


class APIStatsResponse(http.APIResponse):

    def get_normalized_dict(self):
        raw_data = self.get_dict()

        data = {}

        if 'resultSets' in raw_data:
            results = raw_data['resultSets']
            if 'Meta' in results:
                return results
        else:
            results = raw_data['resultSet']
        if isinstance(results, dict):
            results = [results]
        for result in results:
            name = result['name']
            headers = result['headers']
            row_set = result['rowSet']

            rows = []
            for raw_row in row_set:
                row = {}
                for i in range(len(headers)):
                    row[headers[i]] = raw_row[i]
                rows.append(row)
            data[name] = rows

        return data

    def get_normalized_json(self):
        return json.dumps(self.get_normalized_dict())

    def get_parameters(self):
        if not self.valid_json() or 'parameters' not in self.get_dict():
            return None

        parameters = self.get_dict()['parameters']
        if isinstance(parameters, dict):
            return parameters

        parameters = {}
        for parameter in self.get_dict()['parameters']:
            for key, value in parameter.items():
                parameters.update({key: value})
        return parameters

    def get_headers_from_data_sets(self):
        raw_dict = self.get_dict()
        if 'resultSets' in raw_dict:
            results = raw_dict['resultSets']
        else:
            results = raw_dict['resultSet']
        if isinstance(results, dict):
            if 'name' not in results:
                return {}
            return {results['name']: results['headers']}
        return {result_set['name']: result_set['headers'] for result_set in results}

    def get_data_sets(self):
        raw_dict = self.get_dict()
        if 'resultSets' in raw_dict:
            results = raw_dict['resultSets']
        else:
            results = raw_dict['resultSet']
        if isinstance(results, dict):
            if 'name' not in results:
                return {}
            return {results['name']: {'headers': results['headers'], 'data': results['rowSet']}}
        return {result_set['name']: {'headers': result_set['headers'], 'data': result_set['rowSet']}
                for result_set in results}


class APIStatsHTTP(http.APIHTTP):

    nba_response = APIStatsResponse

    base_url = 'https://stats.nba.com/stats/{endpoint}'

    headers = RECRUIT_HEADERS

    def clean_contents(self, contents):
        if '{"Message":"An error has occurred."}' in contents:
            return '<Error><Message>An error has occurred.</Message></Error>'
        return contents