import re
import requests
import base64
import json
import os

CONFIG_FILE = "config_synx.json"

# Color codes
g = "\033[1;32m"
y = "\033[1;33m"
r = "\033[1;31m"
w = "\033[0m"
c = "\033[1;36m"
m = "\033[1;35m"

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def logo():
    print(m + "="*56)
    print(m + "  ████████╗██╗███╗   ███╗███████╗██████╗ " + w)
    print(m + "  ╚══██╔══╝██║████╗ ████║██╔════╝██╔══██╗" + w)
    print(m + "     ██║   ██║██╔████╔██║█████╗  ██████╔╝" + w)
    print(m + "     ██║   ██║██║╚██╔╝██║██╔══╝  ██╔══██╗" + w)
    print(m + "     ██║   ██║██║ ╚═╝ ██║███████╗██║  ██║" + w)
    print(m + "     ╚═╝   ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝" + w)
    print(m + "="*56 + w)
    print(c + "   PROJECT - Voucher Time Checker" + w)
    print(c + "   Telegram Channel 👉 @starlink663 && @starlink987" + w)
    print(g + "   Developer: @Nain663" + w)
    print(m + "="*56 + w)

def load_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_config(session_url):
    config = {"session_url": session_url}
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)

def get_session_id(session_url):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'priority': 'u=0, i',
        'referer': session_url,
        'sec-ch-ua': '"Chromium";v="148", "Microsoft Edge";v="148", "Not/A)Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0',
        'cookie':'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219e0ddbd9f2152-0df941f2efc6b08-4c657b58-1327104-19e0ddbd9f3a60%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fgemini.google.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTllMGRkYmQ5ZjIxNTItMGRmOTQxZjJlZmM2YjA4LTRjNjU3YjU4LTEzMjcxMDQtMTllMGRkYmQ5ZjNhNjAifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219e0ddbd9f2152-0df941f2efc6b08-4c657b58-1327104-19e0ddbd9f3a60%22%7D'
    }
    
    try:
        response = requests.get(session_url, headers=headers, timeout=10)
        session_id = re.search(r"[?&]sessionId=([a-zA-Z0-9]+)", response.url).group(1)
        return session_id
    except:
        return None

def login_voucher(session_id, voucher):
    data = {
        "accessCode": voucher,
        "sessionId": session_id,
        "apiVersion": 2
    }
    post_url = base64.b64decode(b'aHR0cHM6Ly9wb3J0YWwtYXMucnVpamllbmV0d29ya3MuY29tL2FwaS9hdXRoL3ZvdWNoZXIvP2xhbmc9ZW5fVVM=').decode()
    headers = {
        "authority": "portal-as.ruijienetworks.com",
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json",
        "origin": "https://portal-as.ruijienetworks.com",
        "referer": f"https://portal-as.ruijienetworks.com/download/static/maccauth/src/index.html?RES=./../expand/res/mrlev58jlgslg49ervu&IS_EG=0&sessionId={session_id}",
        "sec-ch-ua": '"Chromium";v="139", "Not;A=Brand";v="99"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": f'Mozilla/5.0 (Linux; Android 12; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/139.0.0.0',
    }
    try:
        with requests.post(post_url, json=data, headers=headers, timeout=10) as response:
            res_text = response.text
            token_match = re.search('token=(.*?)&', res_text)
            if token_match:
                return token_match.group(1), None
            else:
                return None, res_text
    except Exception as Error:
        return None, str(Error)

def get_balance(active_session_id):
    headers = {
        'authority': 'portal-as.ruijienetworks.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9,my;q=0.8',
        'content-type': 'application/json;',
        'referer': f'https://portal-as.ruijienetworks.com/download/static/maccauth/src/balance.html?RES=./../expand/res/4ukmferxbdgmt3m49po&sessionId={active_session_id}&lang=en_US&redirectUrl=https://www.ruijienetwoacom&authTypeype=15',
        'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'cookie': 'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219e460ef444507-091ef90c028745-1e462c6e-343089-19e460ef4452ab%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTllNDYwZWY0NDQ1MDctMDkxZWY5MGMwMjg3NDUtMWU0NjJjNmUtMzQzMDg5LTE5ZTQ2MGVmNDQ1MmFiIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219e460ef444507-091ef90c028745-1e462c6e-343089-19e460ef4452ab%22%7D',
    }
    
    try:
        response = requests.get(
            f'https://portal-as.ruijienetworks.com/api/auth/balance/getBalance/{active_session_id}',
            headers=headers,
            timeout=10
        )
        return response.json()
    except:
        return None

def format_time(minutes):
    """Format minutes to readable time"""
    if minutes is None or minutes == 0:
        return "N/A"
    minutes = int(minutes)
    if minutes <= 0:
        return "⛔ Expired"
    days = minutes // 1440
    hours = (minutes % 1440) // 60
    mins = minutes % 60
    parts = []
    if days > 0: parts.append(f"{days}d")
    if hours > 0: parts.append(f"{hours}h")
    if mins > 0: parts.append(f"{mins}m")
    return " ".join(parts) if parts else "0m"

def display_voucher_info(voucher, active_session_id, balance_data, index, total):
    """Display voucher info without processing time"""
    print("\n" + "="*56)
    print(f"  📊 VOUCHER [{index}/{total}]")
    print("="*56)
    print(f"  🎫 Voucher: {g}{voucher}{w}")
    
    if balance_data and 'result' in balance_data:
        result = balance_data['result']
        
        mac = result.get('mac', 'N/A')
        print(f"  💻 MAC: {y}{mac}{w}")
        
        plan_name = result.get('profileName', 'Unknown')
        print(f"  📋 Plan: {g}{plan_name}{w}")
        
        total_minutes = result.get('totalMinutes', 0)
        if total_minutes:
            print(f"  📦 Total Time: {g}{format_time(total_minutes)}{w}")
        
        remaining = result.get('remainingMinutes', 0)
        if remaining:
            print(f"  ⏱️  Remaining: {g}{format_time(remaining)}{w}")
        else:
            print(f"  ⏱️  Remaining: {r}Expired / 0{w}")
        
        status = result.get('status', 'Unknown')
        if status == 1 or status == 'active':
            print(f"  📊 Status: {g}✅ Active{w}")
        else:
            print(f"  📊 Status: {r}❌ Inactive / Expired{w}")
    else:
        print(f"  📊 Status: {r}❌ Failed to retrieve data{w}")
    
    print("="*56)

def check_voucher(session_url, voucher, session_id=None):
    """Check a single voucher"""
    if not session_id:
        session_id = get_session_id(session_url)
        if not session_id:
            return False, None, None
    
    active_session_id, error = login_voucher(session_id, voucher)
    if not active_session_id:
        return False, None, None
    
    balance_data = get_balance(active_session_id)
    if not balance_data:
        return False, active_session_id, None
    
    return True, active_session_id, balance_data

def select_voucher_type():
    """Menu 1: Select voucher type"""
    print("\n" + "="*56)
    print("  🔢 SELECT VOUCHER TYPE")
    print("="*56)
    print("  [1] Digit 6 (6-digit numbers)")
    print("  [2] Digit 7 (7-digit numbers)")
    print("  [3] Digit 8 (8-digit numbers)")
    print("  [4] ASCII-Lower (6 lowercase letters)")
    print("="*56)
    
    while True:
        choice = input(f"{g}Enter your choice (1-4): {w}").strip()
        if choice == '1':
            return 'digit6', r'^\d{6}$', '6 digits'
        elif choice == '2':
            return 'digit7', r'^\d{7}$', '7 digits'
        elif choice == '3':
            return 'digit8', r'^\d{8}$', '8 digits'
        elif choice == '4':
            return 'ascii-lower', r'^[a-z]{6}$', '6 lowercase letters'
        else:
            print(f"{r}Invalid! Please select 1-4.{w}")

def collect_vouchers(voucher_type, pattern, format_desc):
    """Collect vouchers from user input"""
    print(f"\n{c}📝 ENTER VOUCHERS - {voucher_type.upper()}{w}")
    print(f"{y}Format: {format_desc}{w}")
    print(f"{y}Type 'done' when finished, or 'q' to quit.{w}\n")
    
    vouchers = []
    count = 0
    
    while True:
        count += 1
        voucher = input(f"{g}Voucher #{count}: {w}").strip()
        
        if voucher.lower() in ['done', 'q']:
            break
        if not voucher:
            continue
        
        # Validate
        if not re.match(pattern, voucher):
            print(f"{r}❌ Invalid! Must be {format_desc}.{w}")
            continue
        
        vouchers.append(voucher)
        print(f"{g}✅ Added: {voucher} (Total: {len(vouchers)}){w}")
    
    return vouchers

def batch_check(session_url, vouchers):
    """Check all collected vouchers"""
    if not vouchers:
        print(f"{r}❌ No vouchers to check!{w}")
        return
    
    print(f"\n{m}╔{'═'*56}╗{w}")
    print(f"{m}║  🚀 CHECKING {len(vouchers)} VOUCHERS{w}")
    print(f"{m}╚{'═'*56}╝{w}")
    
    # Get session ID once
    print(f"\n{y}⏳ Getting session ID...{w}")
    session_id = get_session_id(session_url)
    if not session_id:
        print(f"{r}❌ Failed to get session ID!{w}")
        return
    
    print(f"{g}✅ Session ID obtained{w}")
    
    # Track results
    valid_list = []
    invalid_list = []
    
    # Check each voucher
    for idx, voucher in enumerate(vouchers, 1):
        success, active_session_id, balance_data = check_voucher(session_url, voucher, session_id)
        
        if success and balance_data:
            valid_list.append(voucher)
            display_voucher_info(voucher, active_session_id, balance_data, idx, len(vouchers))
        else:
            invalid_list.append(voucher)
            print("\n" + "="*56)
            print(f"  📊 VOUCHER [{idx}/{len(vouchers)}]")            
            print("="*56)
            print(f"  🎫 Voucher: {y}{voucher}{w}")
            print(f"  📊 Status: {r}❌ Invalid / Expired{w}")
            print("="*56)
    
    # Summary
    print(f"\n{m}╔{'═'*56}╗{w}")
    print(f"{m}║  📊 CHECK SUMMARY{w}")
    print(f"{m}║  ─────────────────────────────{w}")
    print(f"{m}║  ✅ Valid: {g}{len(valid_list)}{w}")
    print(f"{m}║  ❌ Invalid: {r}{len(invalid_list)}{w}")
    print(f"{m}║  📦 Total: {c}{len(vouchers)}{w}")
    
    if valid_list:
        print(f"{m}║  ─────────────────────────────{w}")
        print(f"{m}║  ✅ Valid Vouchers:{w}")
        for v in valid_list:
            print(f"{m}║     {g}{v}{w}")
    
    if invalid_list:
        print(f"{m}║  ─────────────────────────────{w}")
        print(f"{m}║  ❌ Invalid Vouchers:{w}")
        for v in invalid_list:
            print(f"{m}║     {r}{v}{w}")
    
    print(f"{m}╚{'═'*56}╝{w}")

def main():
    clear_screen()
    logo()
    
    # Load saved URL
    config = load_config()
    saved_url = config.get("session_url", "")
    
    # Get session URL
    print(f"\n{y}🌐 WiFi Session URL{w}")
    if saved_url:
        print(f"{c}💾 Saved: {saved_url[:60]}...{w}")
    
    session_url = input(f"{g}Enter URL (Enter to use saved): {w}").strip() or saved_url
    
    if not session_url:
        print(f"{r}❌ Session URL is required!{w}")
        return
    
    if session_url != saved_url:
        save_config(session_url)
        print(f"{g}✅ URL saved!{w}")
    
    # Select voucher type
    voucher_type, pattern, format_desc = select_voucher_type()
    print(f"{g}✅ Selected: {voucher_type.upper()}{w}")
    
    # Collect vouchers
    vouchers = collect_vouchers(voucher_type, pattern, format_desc)
    
    if not vouchers:
        print(f"{r}❌ No vouchers collected!{w}")
        return
    
    print(f"\n{c}📦 Total collected: {len(vouchers)} voucher(s){w}")
    
    # Confirm
    confirm = input(f"{y}Start checking? (y/n): {w}").strip().lower()
    if confirm != 'y':
        print(f"{r}Cancelled.{w}")
        return
    
    # Batch check
    batch_check(session_url, vouchers)
    
    print(f"\n{g}✅ Done!{w}")

if __name__ == "__main__":
    main()
