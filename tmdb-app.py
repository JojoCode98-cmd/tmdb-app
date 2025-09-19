import requests
import argparse
import os

def main():
	parser=argparse.ArgumentParser(description="Manage command")
	parser.add_argument("--type",choices=["playing","top","upcoming","popular"],required=True,help="command to communicate with the programme: playing,top,upcoming,popular")
	args=parser.parse_args()
	
	endpoint_map={"playing":"now_playing","popular":"popular","top":"top_rated","upcoming":"upcoming"}
	
	select_endpoint=endpoint_map.get(args.type)
	
	if select_endpoint:
		print(fetch_movies(select_endpoint))
	else:
		print("There isn't anything about you ask")
def fetch_movies(action):
	API_KEY=os.getenv("TMDB_API_KEY")
	if not API_KEY:
		print(f"Error something is wrong")
		return 
	url=f"https://api.themoviedb.org/3/movie/{action}"
	params={"api_key":API_KEY,"language":"en-US","page":1}
	response=requests.get(url,params=params)
	if response.status_code==200:
		datas=response.json()
		datas=datas["results"]
		for data in datas:
			print(f"\n=== {action.replace('_',' ').title()}===")
			print(f"_"*70)
			print(f"\nTile:{data['title']}\n\nRelease Date {data['release_date']}\n\nSynopsy:{data['overview']}")
		
	else:
		print(f"Error: it's not the true url you map")
	
if __name__=="__main__":
	main()	