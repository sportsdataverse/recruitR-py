import json, requests

def strip_suffix(name):
	if name.endswith(' Jr'):
		name = name.replace('Jr', '')
	elif name.endswith(' Jr.'):
		name = name.replace('Jr.', '')
	elif name.endswith(' II'):
		name = name.replace('II', '')
	elif name.endswith(' III'):
		name = name.replace('III', '')
	elif name.endswith(' IV'):
		name = name.replace('IIII', '')
	elif name.endswith(' V'):
		name = name.replace('V', '')
	elif name.endswith(' VI'):
		name = name.replace('VI', '')
	elif name.endswith(' VII'):
		name = name.replace('VII', '')
	
	return name.strip()

def matching_player(name, year, hometown):
	url = "https://n.rivals.com/api/v1/people"
	
	headers = {
		'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0',
		'Accept': 'application/json, text/plain, */*',
		'Accept-Language': 'en-US,en;q=0.5',
		'Referer': 'https://n.rivals.com/search',
		'Content-Type': 'application/json;charset=utf-8',
		'X-XSRF-TOKEN': 'JWSTp21Yj1wpNjaVz7W7x/wNgbUCNxLTFP0oHbOtYWUXdXMt2hvX+NQ3ejC8as5FAb1RE/KwiH3bY4SlsEl+Sg==',
		'Origin': 'https://n.rivals.com',
		'Connection': 'keep-alive',
		'Cookie': 'A1=d=AQABBL_NHmACEKNsUb5rZatSKxxQNn_WTEQFEgEBAQEfIGAoYAAAAAAA_SMAAA&S=AQAAAkKziEj7gaF2mOKKRDUJWqg; A3=d=AQABBL_NHmACEKNsUb5rZatSKxxQNn_WTEQFEgEBAQEfIGAoYAAAAAAA_SMAAA&S=AQAAAkKziEj7gaF2mOKKRDUJWqg; A1S=d=AQABBL_NHmACEKNsUb5rZatSKxxQNn_WTEQFEgEBAQEfIGAoYAAAAAAA_SMAAA&S=AQAAAkKziEj7gaF2mOKKRDUJWqg; GUC=AQEBAQFgIB9gKEId1wSk; XSRF-TOKEN=JWSTp21Yj1wpNjaVz7W7x%2FwNgbUCNxLTFP0oHbOtYWUXdXMt2hvX%2BNQ3ejC8as5FAb1RE%2FKwiH3bY4SlsEl%2BSg%3D%3D; _rivalry_session_v2=ZWZZQVZSQVh3ZnNaSWxaZlgwNU95aXV3a3VFREM2SE9iME9wZG4yaERvd0hHNjJOekhGZG1BOHo4WDM5OFdCSnFCczRWQ0hKelRzMWJna1NDZXV3MndjNHhaZlU1S0ZEdmJFaTVUR1doQ1RHdUJhRlQxUis2cWRBblUyVlhKcXVnVHE0aFlDODZscVMvQWxwRWxQUmpwUGk4QWdXRWUwdTlIZ2lxUk5YdzlJa3RxVVdac3lBdGRiQkxBOEErYXl2djNGT1dXa1g0c3ozSHJJdDZyMkNFZmd0eDZhUmE5TVFHU2RLc045RHlqMFFjUjJvbzVVOU9MNG9ORU9qdHY4K21wTjdtVlNVVU1KWTFNWlY0MUp6eDY3cnNZMHdNYVg5aGQ5TUZoM2doZnZEK1NvWkRkNjBiVVFlYmlyTzVqb21WVFlRRXlmWEVZSmtHZTVsc0tENkdBPT0tLVNNQmpEbzFNMGI1blVuKzVyR1Q3SFE9PQ%3D%3D--0947bcffa7fd9b9703f5522cb9afa8fac7d83254; GUCS=Ae_tyY5k; ywandp=10002066977754%3A1333922239; _cb_ls=1; _ga=GA1.2.770716812.1612631490; _gid=GA1.2.1018170693.1612631490; _gat=1; A1=d=AQABBL_NHmACEKNsUb5rZatSKxxQNn_WTEQFEgEBAQEfIGAoYAAAAAAA_SMAAA&S=AQAAAkKziEj7gaF2mOKKRDUJWqg; A1S=d=AQABBL_NHmACEKNsUb5rZatSKxxQNn_WTEQFEgEBAQEfIGAoYAAAAAAA_SMAAA&S=AQAAAkKziEj7gaF2mOKKRDUJWqg; A3=d=AQABBL_NHmACEKNsUb5rZatSKxxQNn_WTEQFEgEBAQEfIGAoYAAAAAAA_SMAAA&S=AQAAAkKziEj7gaF2mOKKRDUJWqg; GUC=AQEBAQFgIB9gKEId1wSk; _rivalry_session_v2=QW9Cckk0MGF3bnZtSFBLMFVhNlp3M281bFkzajM0dW9KWjh5clJEUWNNVytqU0w5dDg4OGJFY0NiMDNLZ0N1b3g2NEhWcVNvWm40QVdDNmlROGozMXJGazdMQmsrWUo0ZitnZkhHSFcweERuQkwxNUdQdmFESng0bTdPZlJPcTlhYy94QndBNlNWdERSMzRMVWtSbHFxT1l1VlB3eC9TbGN0OFJId2R0S1AwRE16R09GcDArbDVSUVFWcldxQzFoekJibkxNWjVQOVlRZS9vZVBkcTVpWkFqYUFIRkhLMVluaktxdllUNDRUWGw2SjdteDR3K2VHbmk0TytGWFZHdzVJaUNhanN3OFNlbDlxVGMxVEFNeXUrWFVORmt2N0ZkYnVBRUVEaEtJRTBjbHUzSUxiemRiZU8wN3hqZGJDcFA4Nnk3eDJHOGVRVzdmb2pRYUNNNDJnPT0tLXJ4c1ZUUjFXY0dqUHltWE1sSitjUHc9PQ%3D%3D--ab9e9cd73c80953acce2a86a86eb53ab3b0bfabf',
		'TE': 'Trailers'
	}
	
	payload = "{\"search\": {\"member\": \"Prospect\", \"query\": \"" + strip_suffix(name) + "\", \"sport\": \"Football\", \"page_number\": \"1\", \"page_size\": \"50\", \"recruit_year\": \"" + year + "\"}}"
	
	response = requests.request("POST", url, headers=headers, data=payload)
	
	players = json.loads(response.text)['people']
	
	for player in players:
		player_name = ' '.join(player['full_name'].split())
		if strip_suffix(player_name).lower() == strip_suffix(name).lower() and player['hometown'].replace('Saint', 'St.').lower() == hometown.replace('Saint', 'St.').lower():
			return player

def url(player):
	return player['url']

def score(player):
	return str(player['rivals_rating'])

def stars(player):
	stars = ''
	
	for i in range (1, 6):
		if i <= player['stars']:
			stars += '★'
		else:
			stars += '☆'
	
	return stars

def position_ranking(player):
	if player['position_rank'] is not None:
		return '\#' + str(player['position_rank']) + ' ' + player['position_abbreviation']
	else:
		return 'N/A'

def state_ranking(player):
	if player['state_rank'] is not None:
		return '\#' + str(player['state_rank']) + ' in ' + player['state']
	else:
		return 'N/A'

def overall_ranking(player):
	if player['national_rank'] is not None:
		return '\#' + str(player['national_rank']) + ' overall'
	else:
		return 'N/A'