import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style
import time

def check_profile(platform_url, nickname):
    try:
        url = platform_url.format(nickname)
        response = requests.get(url)
        if response.status_code == 200:
            return url
    except Exception as e:
        print(f"Error checking {platform_url}: {e}")
    return None

intro = r"""
{banner_color}
/$$$$$$$                     /$$                     /$$      
| $$__  $$                   | $$                    | $$      
| $$  \ $$ /$$$$$$  /$$$$$$$ | $$  /$$$$$$  /$$   /$$| $$   /$$
| $$$$$$$/|____  $$| $$__  $$| $$ /$$__  $$|  $$ /$$/| $$  /$$/
| $$____/  /$$$$$$$| $$  \ $$| $$| $$  \__/ \  $$$$/ | $$$$$$/ 
| $$      /$$__  $$| $$  | $$| $$| $$        >$$  $$ | $$_  $$ 
| $$     |  $$$$$$$| $$  | $$| $$| $$       /$$/\  $$| $$ \  $$ 
|__/      \_______/|__/  |__/|__/|__/      |__/  \__/|__/  \__/  by Twiez
{reset}
"""  

print(intro.format(banner_color=Fore.CYAN, reset=Style.RESET_ALL))

def main(nickname):
    platforms = {
        "Twitter": "https://twitter.com/{}",
        "Instagram": "https://www.instagram.com/{}",
        "Facebook": "https://www.facebook.com/{}",
        "LinkedIn": "https://www.linkedin.com/in/{}",
        "YouTube": "https://www.youtube.com/c/{}",
        "TikTok": "https://www.tiktok.com/@{}",
        "Reddit": "https://www.reddit.com/user/{}",
        "Pinterest": "https://www.pinterest.com/{}/",
        "Tumblr": "https://{}.tumblr.com/",
        "Snapchat": "https://www.snapchat.com/add/{}",
        "GitHub": "https://github.com/{}",
        "Twitch": "https://www.twitch.tv/{}",
        "Flickr": "https://www.flickr.com/photos/{}",
        "SoundCloud": "https://soundcloud.com/{}",
        "Vimeo": "https://vimeo.com/{}",
        "WhatsApp": "https://wa.me/{}",
        "Quora": "https://www.quora.com/profile/{}",
        "Meetup": "https://www.meetup.com/members/{}/",
        # "TurkHackTeam": "https://www.turkhackteam.org/members/{}",
        "DeviantArt": "https://www.deviantart.com/{}",
        "GitLab": "https://gitlab.com/{}",
        "Blogger": "https://{}.blogspot.com/",
        "Medium": "https://medium.com/@{}",
        "Foursquare": "https://foursquare.com/user/{}",
        "Trello": "https://trello.com/{}",
        "MySpace": "https://myspace.com/{}",
        "Weibo": "https://www.weibo.com/{}",
        "Xing": "https://www.xing.com/profile/{}",
        "VKontakte": "https://vk.com/{}",
        "TryHackMe": "https://tryhackme.com/p/{}",
        "LeetCode": "https://leetcode.com/u/{}",
        "Codewars": "https://www.codewars.com/users/{}",
        "HackerRank": "https://www.hackerrank.com/{}",
        "Stack Overflow": "https://stackoverflow.com/users/{}",
        "Dev.to": "https://dev.to/{}",
        "Product Hunt": "https://www.producthunt.com/@{}",
        "Behance": "https://www.behance.net/{}",
        "Dribbble": "https://dribbble.com/{}",
        "Codecademy": "https://www.codecademy.com/profiles/{}",
        "LinkedIn Learning": "https://www.linkedin.com/learning/instructors/{}",
        "Skillshare": "https://www.skillshare.com/user/{}",
        "Udemy": "https://www.udemy.com/user/{}",
        "Coursera": "https://www.coursera.org/user/{}",
        "Kaggle": "https://www.kaggle.com/{}",
        # Diğer platformlar buraya eklenebilir
    }
    
    found_profiles = []
    
    for platform, url in platforms.items():
        profile_url = check_profile(url, nickname)
        if profile_url:
            found_profiles.append((platform, profile_url))
            print(f"{Fore.GREEN}[✓] {platform}: {profile_url}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[X] {platform} profil bulunamadı.{Style.RESET_ALL}")
        time.sleep(1)  # İstekler arası gecikme
    
    if found_profiles:
        print(f"\n{Fore.YELLOW}Bulunan Profiller:{Style.RESET_ALL}")
        for platform, url in found_profiles:
            print(f"{Fore.LIGHTYELLOW_EX}{platform}: {url}{Style.RESET_ALL}")  # Turuncu renk için LIGHTYELLOW_EX
    else:
        print(f"\n{Fore.YELLOW}Profiller bulunamadı.{Style.RESET_ALL}")

if __name__ == "__main__":
    user_nickname = input("Nickname girin: ")
    main(user_nickname)
