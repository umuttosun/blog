import requests

def request(package_name):
	url = 'https://play.google.com/store/apps/details?id=' + package_name

	response = requests.head(url)

	return response.status_code


if __name__ == "__main__":
	with open("packagelist.txt") as fp: 
		for line in fp: 
			response = request(line.strip())

			if response == 200:
				print("# {}".format(line.strip()))
			elif response == 404:
				print("  {}".format(line.strip()))
			else:
				print("? {}".format(line.strip()))
