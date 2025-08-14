import requests
from bs4 import BeautifulSoup
import json

headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get("https://www.melon.com/album/detail.htm?albumId=11859863", headers=headers)
# print(f"response: {response.content}")
soup = BeautifulSoup(response.content, 'lxml')
input_tags = soup.select('tr[data-group-items="cd1"] input.input_check ')

print(f"tr: {len(input_tags)}")

song_urls = [ f'https://www.melon.com/song/detail.htm?songId={data.get("value""")}' for data in input_tags]

song_datas = []

for url in song_urls:
    song_response = requests.get(url, headers=headers)
    song_soup = BeautifulSoup(song_response.content, 'lxml')
    # 태그모음
    lyric_tag = song_soup.select_one('div.lyric')
    song_tag = song_soup.select_one('div.song_name')
    artist_tag = song_soup.select_one('.artist_name span')
    # print(f"lyric_tag: {lyric_tag}")

    # 텍스트 모음
    song_text =  song_tag.get_text(strip=True)  # 줄바꿈, 공백 제거
    lyric_text = lyric_tag.get_text(strip=True) if lyric_tag else ""  # 줄바꿈, 공백 제거
    artist_text = artist_tag.get_text(strip=True) if lyric_tag else ""  # 줄바꿈, 공백 제거

    if lyric_tag:
        data = {
            "name": song_text,
            "artist": artist_text,
            "lyric": lyric_text
        }
        song_datas.append(data)

for data in song_datas:
    print(data)
    print('='*30)

with open("kpop_demon_hunters.json", "w", encoding="utf-8") as f:
    json.dump(song_datas, f, ensure_ascii=False, indent=4)

print("kpop_demon_hunters.json 파일 저장 완료")
print("dev 브랜치 추가33")

