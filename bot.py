import requests
import json
import os
import urllib.parse
from datetime import datetime
import time
from colorama import *
import pytz

wib = pytz.timezone('Asia/Jakarta')

class Birds:
    def __init__(self) -> None:
        self.session = requests.Session()
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Origin': 'https://birdx.birds.dog',
            'Pragma': 'no-cache',
            'Referer': 'https://birdx.birds.dog/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
        }

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def log(self, message):
        print(
            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}{message}",
            flush=True
        )

    def welcome(self):
        print(
            f"""
        {Fore.GREEN + Style.BRIGHT}Auto Claim {Fore.BLUE + Style.BRIGHT}Birds - BOT
            """
            f"""
        {Fore.GREEN + Style.BRIGHT}Rey? {Fore.YELLOW + Style.BRIGHT}<INI WATERMARK>
            """
        )

    def format_seconds(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"
    
    def load_data(self, query: str):
        query_params = urllib.parse.parse_qs(query)
        query = query_params.get('user', [None])[0]

        if query:
            user_data_json = urllib.parse.unquote(query)
            user_data = json.loads(user_data_json)
            first_name = user_data['first_name']
            last_name = user_data['last_name']
            name = f"{first_name} {last_name}"
            username = user_data['username']
            return name, username
        else:
            raise ValueError("User data not found in query.")
        
    def get_user(self, query: str):
        url = 'https://api.birds.dog/user'
        self. headers.update({
            'Telegramauth': f'tma {query}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        if response.status_code == 200:
            try:
                return response.json()
            except json.JSONDecodeError:
                return None
        else:
            return None
        
    def post_user(self, query: str, name: str, username: str,):
        url = 'https://api.birds.dog/user'
        data = json.dumps({'name':name, 'referId':'1493482017', 'username':username })
        self. headers.update({
            'Telegramauth': f'tma {query}',
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, data=data)
        if response.status_code == 200:
            return response.json()
        else:
            return None
        
    def worms_status(self, query: str):
        url = 'https://worm.birds.dog/worms/mint-status'
        self. headers.update({
            'Authorization': f'tma {query}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        result = response.json()
        if result['message'] == 'SUCCESS':
            return result['data']
        else:
            return None
        
    def mint_worms(self, query: str):
        url = 'https://worm.birds.dog/worms/mint'
        data = {}
        self. headers.update({
            'Authorization': f'tma {query}',
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, json=data)
        result = response.json()
        if result['message']:
            return result
        else:
            return None
        
    def incubate_info(self, query: str):
        url = 'https://api.birds.dog/minigame/incubate/info'
        self. headers.update({
            'Telegramauth': f'tma {query}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)

        if response.status_code != 200 or not response.text.strip():
            return None

        try:
            return response.json()
        except json.JSONDecodeError as e:
            self.log(f"[ JSON Error ]: {e}")
            return None
        
    def incubate_upgrade(self, query: str):
        url = 'https://api.birds.dog/minigame/incubate/upgrade'
        self. headers.update({
            'Telegramauth': f'tma {query}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        result = response.json()
        if result:
            return result
        else:
            return None
        
    def confirm_upgrade(self, query: str):
        url = 'https://api.birds.dog/minigame/incubate/confirm-upgraded'
        self. headers.update({
            'Telegramauth': f'tma {query}',
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers)
        if response.status_code == 200:
            return True
        else:
            return False
        
    def egg_join(self, query: str):
        url = 'https://api.birds.dog/minigame/egg/join'
        self. headers.update({
            'Telegramauth': f'tma {query}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None
        
    def egg_turn(self, query: str):
        url = 'https://api.birds.dog/minigame/egg/turn'
        self. headers.update({
            'Telegramauth': f'tma {query}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None
        
    def egg_play(self, query: str):
        url = 'https://api.birds.dog/minigame/egg/play'
        self. headers.update({
            'Telegramauth': f'tma {query}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None
        
    def egg_claim(self, query: str):
        url = 'https://api.birds.dog/minigame/egg/claim'
        self. headers.update({
            'Telegramauth': f'tma {query}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        if response.status_code == 200:
            return True
        else:
            return False
        
    def projects(self, query: str):
        url = 'https://api.birds.dog/project'
        self. headers.update({
            'Telegramauth': f'tma {query}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None
        
    def join_tasks(self, query: str):
        url = 'https://api.birds.dog/project/join-task'
        self. headers.update({
            'Telegramauth': f'tma {query}',
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None
        
    def question(self):
        while True:
            upgrade_egg = input("Auto Incubate and Upgrade Egg? [y/n] -> ").strip().lower()
            if upgrade_egg in ["y", "n"]:
                upgrade_egg = upgrade_egg == "y"
                break
            else:
                print(f"{Fore.RED+Style.BRIGHT}Invalid Input.{Fore.WHITE+Style.BRIGHT} Choose 'y' to Yes or 'n' to Skip.{Style.RESET_ALL}")

        return upgrade_egg
    
    def process_query(self, query: str, upgarde_egg: bool):

        name, username = self.load_data(query)

        user = self.get_user(query)
        if not user:
            create_user = self.post_user(query, name, username)
            if create_user:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {create_user['name']} {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Balance{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {create_user['balance']} Birds {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
            user = self.get_user(query)

        time.sleep(1)

        if user:
            self.log(
                f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                f"{Fore.WHITE+Style.BRIGHT} {user['name']} {Style.RESET_ALL}"
                f"{Fore.MAGENTA+Style.BRIGHT}] [ Balance{Style.RESET_ALL}"
                f"{Fore.WHITE+Style.BRIGHT} {user['balance']} Birds {Style.RESET_ALL}"
                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
            )

            worms = self.worms_status(query)
            if worms:
                status = worms['status']
                if status == 'MINT_OPEN':
                    mint = self.mint_worms(query)
                    if mint['message'] == 'SUCCESS' and mint:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Worms{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} {mint['minted']['type']} {Style.RESET_ALL}"
                            f"{Fore.GREEN+Style.BRIGHT} Is Minted {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}] [ Reward {Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} {mint['minted']['reward']} Birds {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Worms{Style.RESET_ALL}"
                            f"{Fore.RED+Style.BRIGHT} Is Escaped {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}-{Style.RESET_ALL}"
                            f"{Fore.YELLOW+Style.BRIGHT} Try Again Later {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                else:
                    next_mint = worms['nextMintTime']
                    next_mint_utc = datetime.strptime(next_mint, '%Y-%m-%dT%H:%M:%S.%fZ')
                    next_mint_wib = pytz.utc.localize(next_mint_utc).astimezone(wib).strftime('%x %X %Z')
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Worms{Style.RESET_ALL}"
                        f"{Fore.YELLOW+Style.BRIGHT} Is Already Minted {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}] [ Next Mint at{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {next_mint_wib} {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
            else:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Worms{Style.RESET_ALL}"
                    f"{Fore.RED+Style.BRIGHT} Is None {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )

            join = self.egg_join(query)
            if join:
                turn = self.egg_turn(query)
                if turn:
                    count = turn['turn']
                    if count > 0:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Breaking Egg{Style.RESET_ALL}"
                            f"{Fore.GREEN+Style.BRIGHT} Is Started {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}] [ Turn{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} {count} Left {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )

                        while count > 0:
                            join = self.egg_join(query)
                            if not join:
                                self.log(f"{Fore.RED+Style.BRIGHT}[ Failed to Join Egg Breaking ]{Style.RESET_ALL}")
                                break

                            turn = self.egg_turn(query)
                            if not turn:
                                self.log(f"{Fore.RED+Style.BRIGHT}[ Failed to Get Turn ]{Style.RESET_ALL}")
                                break

                            count = turn['turn']
                            if count <= 0:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Breaking Egg{Style.RESET_ALL}"
                                    f"{Fore.YELLOW+Style.BRIGHT} Isn't Started {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Reason{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {count} Turn Left {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                                break

                            play = self.egg_play(query)
                            if play:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Breaking Egg{Style.RESET_ALL}"
                                    f"{Fore.GREEN+Style.BRIGHT} Is Success {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Reward{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {play['result']} Birds {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Turn{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {play['turn']} Left {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                                count -= 1
                            else:
                                break

                            time.sleep(1)

                        if count == 0:
                            claim = self.egg_claim(query)
                            if claim:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Breaking Egg{Style.RESET_ALL}"
                                    f"{Fore.GREEN+Style.BRIGHT} Is Claimed {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Reward Total{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {turn['total']} Birds {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                            else:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Breaking Egg{Style.RESET_ALL}"
                                    f"{Fore.RED+Style.BRIGHT} Isn't Claimed {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Breaking Egg{Style.RESET_ALL}"
                            f"{Fore.YELLOW+Style.BRIGHT} Isn't Started {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}] [ Reason{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} {count} Turn Left {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                else:
                    self.log(f"{Fore.RED+Style.BRIGHT}[ Failed to Get Turn ]{Style.RESET_ALL}")
            else:
                self.log(f"{Fore.RED+Style.BRIGHT}[ Failed to Join Egg Breaking ]{Style.RESET_ALL}")

            if upgarde_egg:
                incubate = self.incubate_info(query)
                if not incubate:
                    upgrade = self.incubate_upgrade(query)
                    if upgrade:
                        upgrade_time = upgrade['upgradedAt'] / 1000
                        duration = upgrade['duration'] * 3600
                        complete_incubate = upgrade_time + duration
                        complete_incubate_wib = datetime.fromtimestamp(complete_incubate).astimezone(wib).strftime('%x %X %Z')

                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Egg{Style.RESET_ALL}"
                            f"{Fore.GREEN+Style.BRIGHT} Is Incubated {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}] [ Complete at{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} {complete_incubate_wib} {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )

                    incubate = self.incubate_info(query)

                if incubate:
                    user = self.get_user(query)
                    balance = user['balance']
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Egg{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} Level {incubate['level']} {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}] [ Balance{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {balance} Birds {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )

                    status = incubate['status']
                    if status == "confirmed" and incubate['nextLevel']:
                        required_balance = incubate['nextLevel']['birds']

                        if balance >= required_balance:
                            upgrade = self.incubate_upgrade(query)
                            if upgrade:
                                upgrade_time = upgrade['upgradedAt'] / 1000
                                duration = upgrade['duration'] * 3600
                                complete_incubate = upgrade_time + duration
                                complete_incubate_wib = datetime.fromtimestamp(complete_incubate).astimezone(wib).strftime('%x %X %Z')

                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Egg{Style.RESET_ALL}"
                                    f"{Fore.GREEN+Style.BRIGHT} Is Incubated {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Complete at{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {complete_incubate_wib} {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                        else:
                            need_more = required_balance - user['balance']
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Egg{Style.RESET_ALL}"
                                f"{Fore.RED+Style.BRIGHT} Isn't Incubated {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}] [ Reason{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} -{need_more} Birds {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )

                    elif status == "processing":
                        upgrade_time = incubate['upgradedAt'] / 1000
                        duration = incubate['duration'] * 3600
                        complete_incubate = upgrade_time + duration
                        complete_incubate_datetime = datetime.fromtimestamp(complete_incubate, wib)

                        formatted_time = complete_incubate_datetime.strftime('%x %X %Z')

                        now = datetime.now(wib).replace(microsecond=0)

                        if now > complete_incubate_datetime:
                            confirm = self.confirm_upgrade(query)
                            if confirm:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Egg{Style.RESET_ALL}"
                                    f"{Fore.GREEN+Style.BRIGHT} Is Upgraded {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                                time.sleep(1)

                                required_balance = incubate['nextLevel']['birds']
                                if user['balance'] >= required_balance:
                                    upgrade = self.incubate_upgrade(query)
                                    if upgrade:
                                        upgrade_time = upgrade['upgradedAt'] / 1000
                                        duration = upgrade['duration'] * 3600
                                        complete_incubate = upgrade_time + duration
                                        complete_incubate_wib = datetime.fromtimestamp(complete_incubate).astimezone(wib).strftime('%x %X %Z')

                                        self.log(
                                            f"{Fore.MAGENTA+Style.BRIGHT}[ Egg{Style.RESET_ALL}"
                                            f"{Fore.GREEN+Style.BRIGHT} Is Incubated {Style.RESET_ALL}"
                                            f"{Fore.MAGENTA+Style.BRIGHT}] [ Complete at{Style.RESET_ALL}"
                                            f"{Fore.WHITE+Style.BRIGHT} {complete_incubate_wib} {Style.RESET_ALL}"
                                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                        )
                                else:
                                    need_more = required_balance - user['balance']
                                    self.log(
                                        f"{Fore.MAGENTA+Style.BRIGHT}[ Egg{Style.RESET_ALL}"
                                        f"{Fore.RED+Style.BRIGHT} Isn't Incubated {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT}] [ Reason{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} -{need_more} Birds {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                    )
                            else:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Egg{Style.RESET_ALL}"
                                    f"{Fore.RED+Style.BRIGHT} Isn't Upgraded {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Egg{Style.RESET_ALL}"
                                f"{Fore.YELLOW+Style.BRIGHT} In Incubation {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}] [ Confirm at{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {formatted_time} {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Egg{Style.RESET_ALL}"
                            f"{Fore.YELLOW+Style.BRIGHT} Is Reached Max Level {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
            else:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Egg{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} Incubate and Upgrade {Style.RESET_ALL}"
                    f"{Fore.YELLOW+Style.BRIGHT}Skipped{Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                )

    def main(self):
        try:
            with open('query.txt', 'r') as file:
                queries = [line.strip() for line in file if line.strip()]

            upgrade_egg = self.question()

            while True:
                self.clear_terminal()
                time.sleep(1)
                self.welcome()
                self.log(
                    f"{Fore.GREEN + Style.BRIGHT}Account's Total: {Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT}{len(queries)}{Style.RESET_ALL}"
                )
                self.log(f"{Fore.CYAN + Style.BRIGHT}-------------------------------------------------------------------------{Style.RESET_ALL}")

                for query in queries:
                    query = query.strip()
                    if query:
                        self.process_query(query, upgrade_egg)
                        time.sleep(3)
                        self.log(f"{Fore.CYAN+Style.BRIGHT}-------------------------------------------------------------------------{Style.RESET_ALL}")

                seconds = 1800
                while seconds > 0:
                    formatted_time = self.format_seconds(seconds)
                    print(
                        f"{Fore.CYAN+Style.BRIGHT}[ Wait for{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {formatted_time} {Style.RESET_ALL}"
                        f"{Fore.CYAN+Style.BRIGHT}... ]{Style.RESET_ALL}",
                        end="\r"
                    )
                    time.sleep(1)
                    seconds -= 1

        except KeyboardInterrupt:
            self.log(f"{Fore.RED + Style.BRIGHT}[ EXIT ] Birds - BOT.{Style.RESET_ALL}")
        except Exception as e:
            self.log(f"{Fore.RED + Style.BRIGHT}An error occurred: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    birds = Birds()
    birds.main()