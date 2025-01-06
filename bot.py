from aiohttp import (
    ClientResponseError,
    ClientSession,
    ClientTimeout
)
from colorama import *
from datetime import datetime
from urllib.parse import parse_qs, unquote
from fake_useragent import FakeUserAgent
import asyncio, time, json, os, pytz

wib = pytz.timezone('Asia/Jakarta')

class Birds:
    def __init__(self) -> None:
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
            'User-Agent': FakeUserAgent().random
        }
        self.id = '7143283584'

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
        {Fore.GREEN + Style.BRIGHT}Auto Claim {Fore.BLUE + Style.BRIGHT}Birds SUI - BOT
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
        query_params = parse_qs(query)
        query = query_params.get('user', [None])[0]

        if query:
            user_data_json = unquote(query)
            user_data = json.loads(user_data_json)
            first_name = user_data.get('first_name', '')
            last_name = user_data.get('last_name', '')
            name = f"{first_name} {last_name}"
            username = user_data.get('username', '')
            return name, username
        else:
            raise ValueError("User data not found in query.")
        
    async def user_data(self, query: str, retries=5):
        url = 'https://api.birds.dog/user'
        headers = {
            **self.headers,
            'Telegramauth': f'tma {query}',
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=30)) as session:
                    async with session.get(url=url, headers=headers) as response:
                        response.raise_for_status()
                        if response.content_type != "application/json":
                            return None
                        
                        return await response.json()
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(2)
                else:
                    return None
        
    async def user_register(self, query: str, name: str, username: str, retries=5):
        url = 'https://api.birds.dog/user'
        data = json.dumps({'name':name, 'referId':self.id, 'username':username })
        headers = {
            **self.headers,
            'Telegramauth': f'tma {query}',
            'Content-Length': str(len(data)),
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=30)) as session:
                    async with session.post(url=url, headers=headers, data=data) as response:
                        response.raise_for_status()
                        return await response.json()
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(2)
                else:
                    return None
        
    async def worms_status(self, query: str, retries=5):
        url = 'https://worm.birds.dog/worms/mint-status'
        headers = {
            **self.headers,
            'Authorization': f'tma {query}',
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=30)) as session:
                    async with session.get(url=url, headers=headers) as response:
                        response.raise_for_status()
                        result = await response.json()
                        return result['data']
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(2)
                else:
                    return None
        
    async def mint_worms(self, query: str, retries=5):
        url = 'https://worm.birds.dog/worms/mint'
        headers = {
            **self.headers,
            'Authorization': f'tma {query}',
            'Content-Length': '2',
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=30)) as session:
                    async with session.post(url=url, headers=headers, json={}) as response:
                        response.raise_for_status()
                        return await response.json()
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(2)
                else:
                    return None

    async def egg_join(self, query: str, retries=5):
        url = 'https://api.birds.dog/minigame/egg/join'
        headers = {
            **self.headers,
            'Telegramauth': f'tma {query}',
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=30)) as session:
                    async with session.get(url=url, headers=headers) as response:
                        response.raise_for_status()
                        return await response.json()
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(2)
                else:
                    return None
        
    async def egg_turn(self, query: str, retries=5):
        url = 'https://api.birds.dog/minigame/egg/turn'
        headers = {
            **self.headers,
            'Telegramauth': f'tma {query}',
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=30)) as session:
                    async with session.get(url=url, headers=headers) as response:
                        response.raise_for_status()
                        return await response.json()
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(2)
                else:
                    return None
        
    async def egg_play(self, query: str, retries=5):
        url = 'https://api.birds.dog/minigame/egg/play'
        headers = {
            **self.headers,
            'Telegramauth': f'tma {query}',
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=30)) as session:
                    async with session.get(url=url, headers=headers) as response:
                        response.raise_for_status()
                        return await response.json()
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(2)
                else:
                    return None
        
    async def egg_claim(self, query: str, retries=5):
        url = 'https://api.birds.dog/minigame/egg/claim'
        headers = {
            **self.headers,
            'Telegramauth': f'tma {query}',
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=30)) as session:
                    async with session.get(url=url, headers=headers) as response:
                        response.raise_for_status()
                        return True
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(2)
                else:
                    return None
        
    async def incubate_info(self, query: str, retries=5):
        url = 'https://api.birds.dog/minigame/incubate/info'
        headers = {
            **self.headers,
            'Telegramauth': f'tma {query}',
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=30)) as session:
                    async with session.get(url=url, headers=headers) as response:
                        if response.status == 400:
                            return None
                        
                        response.raise_for_status()
                        return await response.json()
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(2)
                else:
                    return None
        
    async def incubate_upgrade(self, query: str, retries=5):
        url = 'https://api.birds.dog/minigame/incubate/upgrade'
        headers = {
            **self.headers,
            'Telegramauth': f'tma {query}',
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=30)) as session:
                    async with session.get(url=url, headers=headers) as response:
                        if response.status == 400:
                            return None
                        
                        response.raise_for_status()
                        return await response.json()
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(2)
                else:
                    return None
        
    async def confirm_upgrade(self, query: str, retries=5):
        url = 'https://api.birds.dog/minigame/incubate/confirm-upgraded'
        headers = {
            **self.headers,
            'Telegramauth': f'tma {query}',
            'Content-Length': '0',
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=30)) as session:
                    async with session.post(url=url, headers=headers) as response:
                        response.raise_for_status()
                        return True
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(2)
                else:
                    return None

    async def boost_speed(self, query: str, retries=5):
        url = 'https://api.birds.dog/minigame/boost-speed'
        headers = {
            **self.headers,
            'Telegramauth': f'tma {query}',
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=30)) as session:
                    async with session.get(url=url, headers=headers) as response:
                        response.raise_for_status()
                        return await response.json()
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(2)
                else:
                    return None

    async def update_speed(self, query: str, next_speed: int, retries=5):
        url = 'https://api.birds.dog/minigame/boost-speed/update-speed'
        data = json.dumps({'speed':next_speed})
        headers = {
            **self.headers,
            'Telegramauth': f'tma {query}',
            'Content-Length': str(len(data)),
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=30)) as session:
                    async with session.post(url=url, headers=headers, data=data) as response:
                        if response.status == 400:
                            return None
                        
                        response.raise_for_status()
                        return await response.json()
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(2)
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
    
    async def process_query(self, query: str, upgarde_egg: bool):
        name, username = self.load_data(query)

        user = await self.user_data(query)
        if not user:
            register = await self.user_register(query, name, username)
            if not register:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {name} {Style.RESET_ALL}"
                    f"{Fore.RED+Style.BRIGHT}Data Is None{Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                )
                return

            user = await self.user_data(query)

        self.log(
            f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
            f"{Fore.WHITE+Style.BRIGHT} {user['name']} {Style.RESET_ALL}"
            f"{Fore.MAGENTA+Style.BRIGHT}] [ Balance{Style.RESET_ALL}"
            f"{Fore.WHITE+Style.BRIGHT} {user['balance']:.1f} Birds {Style.RESET_ALL}"
            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
        )
        await asyncio.sleep(3)

        worms = await self.worms_status(query)
        if worms:
            if worms['status'] == 'MINT_OPEN':
                mint = await self.mint_worms(query)
                if mint and mint['message'] == 'SUCCESS':
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
                f"{Fore.RED+Style.BRIGHT} Data Is None {Style.RESET_ALL}"
                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
            )
        await asyncio.sleep(3)

        join = await self.egg_join(query)
        turn = await self.egg_turn(query)
        if join and turn:
            count = turn['turn']
            reward_total = 0
            if count > 0:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Breaking Egg{Style.RESET_ALL}"
                    f"{Fore.GREEN+Style.BRIGHT} Is Started {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Turn{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {count} Left {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
                await asyncio.sleep(1)

                while count > 0:
                    if count <= 0:
                        break

                    play = await self.egg_play(query)
                    if play:
                        count = play['turn']
                        reward = play['result']
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Breaking Egg{Style.RESET_ALL}"
                            f"{Fore.GREEN+Style.BRIGHT} Is Success {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}] [ Reward{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} {reward} Birds {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}] [ Turn{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} {count} Left {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                    else:
                        break

                    reward_total += reward

                    await asyncio.sleep(2)

                claim = await self.egg_claim(query)
                if claim:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Breaking Egg{Style.RESET_ALL}"
                        f"{Fore.GREEN+Style.BRIGHT} Is Claimed {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}] [ Reward Total{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {reward_total} Birds {Style.RESET_ALL}"
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
                    f"{Fore.YELLOW+Style.BRIGHT} No Available Turn Left {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
        else:
            self.log(
                f"{Fore.MAGENTA+Style.BRIGHT}[ Breaking Egg{Style.RESET_ALL}"
                f"{Fore.RED+Style.BRIGHT} Data Is None {Style.RESET_ALL}"
                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
            )
        await asyncio.sleep(3)

        incubate = await self.incubate_info(query)
        if not incubate:
            upgrade = await self.incubate_upgrade(query)
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
            user = await self.user_data(query)
            if not user:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Egg{Style.RESET_ALL}"
                    f"{Fore.RED+Style.BRIGHT} GET Balance Failed {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
                return
            
            current_level = incubate['level']
            next_level_birds = incubate['nextLevel']
            
            balance = user['balance']
            boost = await self.boost_speed(query)
            if boost:
                current_speed = boost['speed']
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Egg{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} Level {current_level} {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Balance{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {balance:.1f} Birds {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Speed{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} x{current_speed} {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
                await asyncio.sleep(1)

                boost_level = [1, 1.2, 1.4, 1.6, 1.8, 2, 2.5]
                if current_speed in boost_level:
                    current_index = boost_level.index(current_speed)
                    if current_index + 1 < len(boost_level):
                        next_speed = boost_level[current_index + 1]

                        update_boost = await self.update_speed(query, next_speed)
                        if update_boost:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Boost Speed{Style.RESET_ALL}"
                                f"{Fore.GREEN+Style.BRIGHT} Is Upgraded {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}] [ Spped{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} x{next_speed} {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Boost Speed{Style.RESET_ALL}"
                                f"{Fore.YELLOW+Style.BRIGHT} Isn't Upgraded {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}] [ Reason{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} Not Eligible {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Boost Speed{Style.RESET_ALL}"
                            f"{Fore.GREEN+Style.BRIGHT} Already at The Maximum Speed Level {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Boost Speed{Style.RESET_ALL}"
                        f"{Fore.RED+Style.BRIGHT} Current Speed Not Found in Boost Levels {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                await asyncio.sleep(1)

            if upgarde_egg:
                status = incubate['status']
                if status == "confirmed":
                    if current_level < 35:
                        required_balance = next_level_birds['birds']

                        if balance >= required_balance:
                            upgrade = await self.incubate_upgrade(query)
                            if upgrade:
                                upgrade_time = upgrade['upgradedAt'] / 1000
                                duration = upgrade['duration'] * 3600
                                booster = incubate['speed']
                                duration_with_boost = duration / booster
                                complete_incubate = upgrade_time + duration_with_boost
                                complete_incubate_wib = datetime.fromtimestamp(complete_incubate).astimezone(wib).strftime('%x %X %Z')

                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Egg{Style.RESET_ALL}"
                                    f"{Fore.GREEN+Style.BRIGHT} Was Successfully Incubated {Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT}to Level {next_level_birds['level']}{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT} ] [ Complete at{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {complete_incubate_wib} {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                            else:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Egg{Style.RESET_ALL}"
                                    f"{Fore.RED+Style.BRIGHT} Failed to Incubate {Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT}to Level {next_level_birds['level']}{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                )
                        else:
                            need_more = required_balance - user['balance']
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Egg{Style.RESET_ALL}"
                                f"{Fore.YELLOW+Style.BRIGHT} Not Eligible to Incubate {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}] [ Reason{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} -{need_more:.1f} Birds {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Egg{Style.RESET_ALL}"
                            f"{Fore.GREEN+Style.BRIGHT} Already at The Maximum Level {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )

                elif status == "processing":
                    upgrade_time = incubate['upgradedAt'] / 1000
                    duration = incubate['duration'] * 3600
                    booster = incubate['speed']
                    duration_with_boost = duration / booster
                    complete_incubate = upgrade_time + duration_with_boost
                    complete_incubate_wib = datetime.fromtimestamp(complete_incubate).astimezone(wib).strftime('%x %X %Z')

                    now = int(time.time())

                    if now >= complete_incubate:
                        confirm = await self.confirm_upgrade(query)
                        if confirm:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Egg{Style.RESET_ALL}"
                                f"{Fore.GREEN+Style.BRIGHT} Upgrade Confirmed Succesfully {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                            await asyncio.sleep(3)

                            incubate = await self.incubate_info(query)
                            if not incubate:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Egg{Style.RESET_ALL}"
                                    f"{Fore.RED+Style.BRIGHT} Data Is None {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                                return
                            
                            current_level = incubate['level']
                            next_level_birds = incubate['nextLevel']
                            required_balance = next_level_birds['birds']

                            if current_level < 35:
                                if balance >= required_balance:
                                    upgrade = await self.incubate_upgrade(query)
                                    if upgrade:
                                        upgrade_time = upgrade['upgradedAt'] / 1000
                                        duration = upgrade['duration'] * 3600
                                        booster = incubate['speed']
                                        duration_with_boost = duration / booster
                                        complete_incubate = upgrade_time + duration_with_boost
                                        complete_incubate_wib = datetime.fromtimestamp(complete_incubate).astimezone(wib).strftime('%x %X %Z')

                                        self.log(
                                            f"{Fore.MAGENTA+Style.BRIGHT}[ Egg{Style.RESET_ALL}"
                                            f"{Fore.GREEN+Style.BRIGHT} Was Successfully Incubated {Style.RESET_ALL}"
                                            f"{Fore.WHITE+Style.BRIGHT}to Level {next_level_birds['level']}{Style.RESET_ALL}"
                                            f"{Fore.MAGENTA+Style.BRIGHT} ] [ Complete at{Style.RESET_ALL}"
                                            f"{Fore.WHITE+Style.BRIGHT} {complete_incubate_wib} {Style.RESET_ALL}"
                                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                        )
                                    else:
                                        self.log(
                                            f"{Fore.MAGENTA+Style.BRIGHT}[ Egg{Style.RESET_ALL}"
                                            f"{Fore.RED+Style.BRIGHT} Failed to Incubate {Style.RESET_ALL}"
                                            f"{Fore.WHITE+Style.BRIGHT}to Level {next_level_birds['level']}{Style.RESET_ALL}"
                                            f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                        )
                                else:
                                    need_more = required_balance - user['balance']
                                    self.log(
                                        f"{Fore.MAGENTA+Style.BRIGHT}[ Egg{Style.RESET_ALL}"
                                        f"{Fore.YELLOW+Style.BRIGHT} Not Eligible to Incubate {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT}] [ Reason{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} -{need_more:.1f} Birds {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                    )
                            else:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Egg{Style.RESET_ALL}"
                                    f"{Fore.GREEN+Style.BRIGHT} Already at The Maximum Level {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Egg{Style.RESET_ALL}"
                                f"{Fore.RED+Style.BRIGHT} Failed to Confirm Upgrade {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                            )
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Egg{Style.RESET_ALL}"
                            f"{Fore.YELLOW+Style.BRIGHT} In Incubation {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}] [ Confirm at{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} {complete_incubate_wib} {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                
            else:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Egg{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} Incubate and Upgrade {Style.RESET_ALL}"
                    f"{Fore.YELLOW+Style.BRIGHT}Skipped{Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                )

    async def main(self):
        try:
            with open('query.txt', 'r') as file:
                queries = [line.strip() for line in file if line.strip()]

            upgrade_egg = self.question()

            while True:
                self.clear_terminal()
                await asyncio.sleep(1)
                self.welcome()
                self.log(
                    f"{Fore.GREEN + Style.BRIGHT}Account's Total: {Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT}{len(queries)}{Style.RESET_ALL}"
                )
                self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}"*75)

                for query in queries:
                    query = query.strip()
                    if query:
                        await self.process_query(query, upgrade_egg)
                        self.log(f"{Fore.CYAN+Style.BRIGHT}-{Style.RESET_ALL}"*75)
                        await asyncio.sleep(3)

                seconds = 1800
                while seconds > 0:
                    formatted_time = self.format_seconds(seconds)
                    print(
                        f"{Fore.CYAN+Style.BRIGHT}[ Wait for{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {formatted_time} {Style.RESET_ALL}"
                        f"{Fore.CYAN+Style.BRIGHT}... ]{Style.RESET_ALL}",
                        end="\r"
                    )
                    await asyncio.sleep(1)
                    seconds -= 1

        except Exception as e:
            self.log(f"{Fore.RED + Style.BRIGHT}An error occurred: {e}{Style.RESET_ALL}")
            return

if __name__ == "__main__":
    try:
        bot = Birds()
        asyncio.run(bot.main())
    except KeyboardInterrupt:
        print(
            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
            f"{Fore.RED + Style.BRIGHT}[ EXIT ] Birds SUI - BOT{Style.RESET_ALL}                                       "                              
        )