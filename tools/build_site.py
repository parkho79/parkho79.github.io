"""
parkho79.github.io 의 홈과 앱 소개 페이지를 만든다.

- 만드는 것: index.html(한국어), en/index.html(영어), <앱>/index.html, <앱>/en/index.html
- 그림: 아이콘 assets/<앱>.png, 스크린샷 <앱>/img/<언어>-<번호>.jpg (스토어 등록정보에서 줄여 복사)
- 문구를 고치면 이 파일의 APPS 를 고치고 다시 실행한다: python tools/build_site.py
- 그림 원본이 없는 PC(예: Mac)에서는 --pages-only 로 페이지만 다시 만든다.
"""
import hashlib
import html
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# 스토어 그림 원본이 있는 폴더 (Windows 기준, 다른 PC 는 PH_DEV 환경 변수로)
PH_DEV = Path(os.environ.get("PH_DEV", "E:/PH_dev"))
# 문의 이메일 (판매자 선언으로 이미 공개된 주소만 쓴다)
EMAIL = "parkho79@gmail.com"
# 스크린샷을 줄일 크기 (스토어 원본 1080x1920 의 절반)
SHOT_SIZE = (540, 960)

# 앱별 문구·링크·그림 원본. 문구는 스토어 등록정보(listing.txt)에서 가져와 줄였다.
APPS = [
    {
        "slug": "phcalendar",
        "play": "com.parkho.calendar",
        # 원스토어 주소 (비어 있으면 버튼을 그리지 않는다)
        "onestore": "https://m.onestore.co.kr/v2/ko-kr/app/0000773058",
        "icon": "Android/releases/PhCalendar/2.0.5.1-vc225/store/onestore/icon-512.png",
        "shots": {
            "ko": ("Android/releases/PhCalendar/2.0.5.1-vc225/store/playstore/ko-KR/ko-kr-shot{}.png", [1, 2, 4, 6, 7]),
            "en": ("Android/releases/PhCalendar/2.0.5.1-vc225/store/playstore/en-US/en-us-shot{}.png", [1, 2, 4, 6, 7]),
        },
        "ko": {
            "name": "간편 음력 달력",
            "store_name": "간편 음력 달력 - 24절기·간지·손없는날",
            "short": "음력·공휴일·24절기를 한눈에 보는 달력, 음력 생일 반복 알림과 홈 화면 위젯",
            "intro": "양력 날짜 아래 음력 날짜와 공휴일, 24절기를 함께 보여 주는 깔끔한 음력 달력이자 만세력입니다. "
                     "가입이나 로그인 없이 바로 쓸 수 있고, 인터넷이 없어도 음력과 절기가 그대로 보입니다.",
            "features": [
                ("음력과 공휴일", ["날짜마다 음력 날짜 (윤달 포함, 한국 음력 기준)", "설날·추석 연휴, 대체공휴일, 법정 기념일", "날짜를 누르면 그날 음력과 메모를 한눈에"]),
                ("24절기·세시풍속·간지", ["24절기, 한식·초복·중복·말복", "대보름·단오·칠석 등 세시풍속", "일진·월건·세차 간지, 손 없는 날"]),
                ("메모와 알림", ["음력 매년·매월 반복으로 음력 생일과 제사를 해마다", "매주·매월·매년, 원하는 간격으로 반복", "메모마다 알람 여러 개, 색상 6가지"]),
                ("홈 화면 위젯", ["4x2·4x3·4x4·5x5 월간 달력 위젯", "위젯에서 달 넘기기", "투명도·글자 크기 조절"]),
                ("내 취향대로", ["기본·벽걸이·무병장수 달력 테마", "남색·초록·빨강·배경화면 색, 라이트·다크", "날짜·음력·메모 글자 크기 조절"]),
                ("백업과 복원", ["메모를 파일로 백업하고 새 폰에서 복원"]),
            ],
        },
        "en": {
            "name": "Simple Lunar Calendar",
            "store_name": "Simple Lunar Calendar & Widget",
            "short": "Korean lunar calendar with holidays, 24 solar terms, lunar reminders and widget",
            "intro": "A clean calendar that shows the Korean lunar date under every day, together with public holidays "
                     "and the 24 solar terms. No sign-up or login needed, and lunar dates and solar terms work offline.",
            "features": [
                ("Lunar dates and holidays", ["The lunar date on every day, including leap months", "Korean public and substitute holidays", "Tap a day to see its lunar date and memos"]),
                ("Solar terms and traditions", ["All 24 solar terms, Hansik and the three Bok days", "Traditional days such as Daeboreum, Dano and Chilseok", "Stems and branches, lucky moving days"]),
                ("Memos and reminders", ["Repeat every year or month by the lunar date", "Weekly, monthly, yearly or custom repeats", "Several reminders per memo, 6 colors"]),
                ("Home screen widget", ["4x2, 4x3, 4x4 and 5x5 month widgets", "Move between months on the widget", "Adjust transparency and text size"]),
                ("Make it yours", ["Basic, Wall and Long life calendar themes", "Navy, green, red or wallpaper colors, light and dark", "Adjustable date, lunar and memo text sizes"]),
                ("Backup and restore", ["Back up memos to a file and restore them on a new phone"]),
            ],
        },
    },
    {
        "slug": "phdday",
        "play": "com.parkho.dday",
        "onestore": "",
        "icon": "Android/parkho-android-dday/apps/phdday/src/main/ic_launcher-playstore.png",
        "shots": {
            "ko": ("Android/parkho-android-dday/apps/phdday/store-listing/ko-KR/ko-kr-shot{}.png", [1, 2, 3, 4, 6]),
            "en": ("Android/parkho-android-dday/apps/phdday/store-listing/en-US/en-us-shot{}.png", [1, 2, 3, 4, 6]),
        },
        "ko": {
            "name": "D-Day 디데이 위젯",
            "store_name": "D-Day 디데이 위젯 - 기념일 계산기",
            "short": "수능, 커플 1000일, 아기 개월수, 음력 생일까지. 위젯·상단바·알림으로 남은 날을 한눈에",
            "intro": "기다리는 날까지 남은 날과 함께한 날을 세어 주는 심플한 디데이·기념일 계산기입니다. "
                     "수능 디데이, 커플 100일·1000일, 아기 개월수, 음력 생일, 월급날까지 홈 화면 위젯과 상단바에서 바로 확인하세요.",
            "features": [
                ("8가지 날짜 계산", ["디데이, 1일부터 세는 기념일", "아기 개월수, 1년 2개월 3일 같은 연월일", "매년·매월·매주 반복, 음력 생일 반복"]),
                ("홈 화면 위젯 3종", ["2x1·4x1·리스트(4x2) 위젯", "미리보기를 보며 배경·제목·숫자 색 바꾸기", "투명도 조절, 사진 배경 위젯"]),
                ("상단바 고정과 알림", ["알림창에 디데이 고정, 잠금화면에서도 확인", "당일, 1·2·5·7·10일 전 알림"]),
                ("다가올 기념일", ["100일, 200일 … 1주년, 2주년을 한 번에", "월별 달력에서 디데이와 공휴일 함께 보기"]),
                ("앱 테마", ["차분한·파스텔·미드나잇·로맨틱 4가지 스타일", "핑크·라벤더·민트·로즈골드 등 색상", "사진 배경, 라이트·다크 모드"]),
                ("백업과 복원", ["디데이와 사진을 파일 하나로 저장", "새 폰에서 그대로 복원"]),
            ],
        },
        "en": {
            "name": "D-Day Countdown",
            "store_name": "D-Day Countdown: Days Until",
            "short": "Days until birthdays, trips & exams, days since you met. Widgets & reminders.",
            "intro": "A simple countdown app and day counter. Count down the days until birthdays, exams, trips and holidays, "
                     "and count up the days since you met, quit smoking or welcomed your baby. See every countdown on your home screen and in your notification bar.",
            "features": [
                ("7 ways to count", ["Days until (D-1, D-2 …)", "Days since, starting from Day 1", "Month count, years / months / days, repeats"]),
                ("3 home screen widgets", ["2x1, 4x1 and a 4x2 list widget", "Change colors with a live preview", "Transparency and photo backgrounds"]),
                ("Notification bar and reminders", ["Pin a countdown to the notification bar", "Reminders on the day or 1–10 days before"]),
                ("Milestones and calendar", ["100 days, 200 days, 1 year, 2 years at a glance", "Monthly calendar with public holidays"]),
                ("App themes", ["Calm, Pastel, Midnight and Romantic styles", "Pink, Lavender, Mint, Rose gold and more", "Photo backgrounds, light and dark mode"]),
                ("Backup and restore", ["Save your D-Days and photos to one file", "Restore everything on a new phone"]),
            ],
        },
    },
    {
        "slug": "mycalendar",
        "play": "com.parkho.mycalendar",
        "onestore": "",
        "icon": "Github/MyCalendar/store-listing/icon-512.png",
        "shots": {
            "ko": ("Github/MyCalendar/store-listing/ko-KR/ko-kr-shot{}.png", [1, 3, 4, 5, 7]),
            "en": ("Github/MyCalendar/store-listing/en-US/en-us-shot{}.png", [1, 3, 4, 5, 7]),
        },
        "ko": {
            "name": "My Calendar",
            "store_name": "음력 달력 위젯 - 공휴일 캘린더 My Calendar",
            "short": "음력·공휴일이 한눈에 보이는 깔끔한 달력 & 일정 캘린더, 큰 글씨 조절, 홈 화면 위젯",
            "intro": "내 일정과 공휴일, 음력 날짜를 한 화면에서 보여 주는 깔끔한 달력·일정 관리 앱이자 홈 화면 달력 위젯입니다. "
                     "날짜와 일정 글자를 크게 키울 수 있어 부모님도 보기 편하고, 휴대폰에 저장된 일정도 자동으로 함께 보여 줍니다.",
            "features": [
                ("공휴일", ["대한민국 등 여러 나라 공휴일", "여러 나라 공휴일을 함께 표시", "공휴일 데이터 자동 업데이트"]),
                ("큰 글씨도 내 눈에 맞게", ["날짜·일정·음력 글자 크기를 각각 조절", "미리보기로 바로 확인"]),
                ("음력 표시", ["날짜 옆(또는 아래)에 음력 날짜", "한국 음력, 중국 농력, 베트남 음력"]),
                ("4가지 보기", ["년·월·주·일 보기", "여러 날 일정은 이어지는 막대로"]),
                ("홈 화면 위젯", ["일정·음력·공휴일이 함께 보이는 월간 위젯", "위젯에서 이전·다음 달, 오늘로 이동"]),
                ("일정과 알림", ["종일·반복 일정 추가와 수정", "길게 눌러 끌어 옮기기, 알림, 검색"]),
            ],
        },
        "en": {
            "name": "My Calendar",
            "store_name": "My Calendar: Widget & Holidays",
            "short": "Calendar & planner with public holidays, adjustable large text and month widget",
            "intro": "A clean, easy-to-read calendar, planner and calendar widget that shows your schedule together with public holidays. "
                     "Dates and events can be shown in large text, and the events already on your phone appear automatically.",
            "features": [
                ("Public holidays", ["United States and many more countries", "Show holidays from several countries together", "Holiday data updated automatically"]),
                ("Large, easy-to-read text", ["Set date and event text sizes separately", "See every change in a live preview"]),
                ("Lunar dates", ["Lunar date beside or under each day", "Korean, Chinese and Vietnamese lunar calendars"]),
                ("Four views", ["Year, month, week and day views", "Multi-day events drawn as continuous bars"]),
                ("Home screen widget", ["Month widget with events and holidays", "Change months or jump to today on the widget"]),
                ("Events and reminders", ["All-day and repeating events", "Drag to move, reminders and search"]),
            ],
        },
    },
]

# 화면 문구 (언어별)
TEXT = {
    "ko": {
        "site_lead": "가입 없이 바로 쓰는 안드로이드 달력·디데이 앱",
        "more": "자세히 보기",
        "features": "주요 기능",
        "privacy": "개인정보처리방침",
        "contact": "문의",
        "home": "parkho79 Apps",
        "other_lang": "English",
        "shots_label": "스크린샷",
        "onestore": "원스토어",
    },
    "en": {
        "site_lead": "Android calendar and countdown apps. No sign-up needed.",
        "more": "Learn more",
        "features": "Features",
        "privacy": "Privacy Policy",
        "contact": "Contact",
        "home": "parkho79 Apps",
        "other_lang": "한국어",
        "shots_label": "Screenshots",
        "onestore": "ONE store",
    },
}

# 모든 페이지가 함께 쓰는 스타일 (assets/site.css 로 따로 두지 않고 페이지마다 넣어 한 파일로 열리게 한다)
CSS = """
:root{--bg:#ffffff;--fg:#1d2033;--muted:#5d6278;--line:#e2e4ee;--accent:#3f51b5;--on-accent:#ffffff;--chip:#f3f4f8}
@media (prefers-color-scheme:dark){:root{--bg:#14151c;--fg:#e8e9f1;--muted:#a3a7bb;--line:#2c2f3d;--accent:#8c9eff;--on-accent:#14151c;--chip:#1e2029;color-scheme:dark}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Noto Sans KR",sans-serif;font-size:16px;line-height:1.65}
.wrap{max-width:880px;margin:0 auto;padding:32px max(16px,env(safe-area-inset-right,0px)) 64px max(16px,env(safe-area-inset-left,0px))}
a{color:var(--accent)}
h1,h2,h3,h4{margin:0;text-wrap:balance;line-height:1.35}
p{margin:0}
.muted{color:var(--muted)}
.top{display:flex;justify-content:space-between;align-items:center;gap:16px;margin-bottom:32px;font-size:15px}
.top a{color:var(--muted);text-decoration:none}
.top a:hover{color:var(--fg)}
.top .home{font-weight:700;color:var(--fg)}
.icon{width:64px;height:64px;border-radius:16px;display:block}
.btns{display:flex;gap:8px;flex-wrap:wrap}
.btn{font-size:15px;padding:8px 16px;border-radius:8px;text-decoration:none;border:1px solid var(--line);color:var(--fg);background:var(--bg)}
.btn.pri{background:var(--accent);border-color:var(--accent);color:var(--on-accent)}
.btn:hover{border-color:var(--accent)}
.btn:focus-visible,a:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.foot{border-top:1px solid var(--line);padding-top:16px;margin-top:48px;font-size:15px;color:var(--muted);display:flex;gap:8px 20px;flex-wrap:wrap}
.foot a{color:var(--muted)}
/* 홈: 앱을 한 줄씩 */
.home-head{display:flex;flex-direction:column;gap:6px}
.home-head h1{font-size:28px}
.list{display:flex;flex-direction:column;margin-top:24px}
.row{display:grid;grid-template-columns:64px minmax(0,1fr);gap:16px;padding:24px 0;border-top:1px solid var(--line);align-items:start}
.row:last-child{border-bottom:1px solid var(--line)}
.row>div{display:flex;flex-direction:column;gap:8px;min-width:0}
.row h2{font-size:20px}
.row h2 a{color:inherit;text-decoration:none}
/* 앱 페이지 */
.app-head{display:grid;grid-template-columns:88px minmax(0,1fr);gap:20px;align-items:center}
.app-head .icon{width:88px;height:88px;border-radius:22px}
.app-head>div{display:flex;flex-direction:column;gap:8px;min-width:0}
.app-head h1{font-size:28px}
.intro{margin-top:24px;max-width:65ch}
.shots{display:flex;gap:12px;overflow-x:auto;margin-top:28px;padding-bottom:8px;scroll-snap-type:x mandatory}
.shots img{width:200px;height:auto;aspect-ratio:9/16;flex:none;border-radius:12px;scroll-snap-align:start}
.sec{margin-top:40px;display:flex;flex-direction:column;gap:16px}
.sec>h2{font-size:20px}
.feat{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:24px 32px}
.feat h3{font-size:16px;margin-bottom:4px}
.feat ul{margin:0;padding-left:18px;color:var(--muted)}
@media (max-width:480px){.shots img{width:160px}.app-head{grid-template-columns:64px minmax(0,1fr)}.app-head .icon{width:64px;height:64px;border-radius:16px}.app-head h1{font-size:24px}}
"""


def main():
    """
    페이지를 모두 만들고, --pages-only 가 없으면 그림도 다시 복사한다
    """
    pages_only = "--pages-only" in sys.argv
    if not pages_only:
        copy_images()
    for lang in ("ko", "en"):
        write(home_path(lang), render_home(lang))
        for app in APPS:
            write(app_path(app["slug"], lang), render_app(app, lang))
    print("done")


def copy_images():
    """
    스토어 원본에서 아이콘(256px)과 스크린샷(540x960 JPEG)을 줄여 복사한다
    """
    from PIL import Image

    for app in APPS:
        icon = Image.open(PH_DEV / app["icon"]).convert("RGBA").resize((256, 256), Image.LANCZOS)
        icon.save(ROOT / "assets" / f"{app['slug']}.png", optimize=True)
        img_dir = ROOT / app["slug"] / "img"
        img_dir.mkdir(parents=True, exist_ok=True)
        for lang, (pattern, numbers) in app["shots"].items():
            for i, n in enumerate(numbers, 1):
                shot = Image.open(PH_DEV / pattern.format(n)).convert("RGB").resize(SHOT_SIZE, Image.LANCZOS)
                shot.save(img_dir / f"{lang}-{i}.jpg", quality=82, optimize=True, progressive=True)


def render_home(lang):
    """
    홈 페이지(앱 목록) HTML
    """
    t = TEXT[lang]
    # 홈에서 앱 폴더·그림까지의 상대 경로 (영어 홈은 en/ 아래라 한 단계 위)
    up = "" if lang == "ko" else "../"
    rows = []
    for app in APPS:
        a = app[lang]
        page = f"{up}{app['slug']}/" + ("" if lang == "ko" else "en/")
        rows.append(f"""
<div class="row"><img class="icon" src="{up}assets/{app['slug']}.png?v={ver(f"assets/{app['slug']}.png")}" alt="" width="64" height="64">
  <div><h2><a href="{page}">{esc(a['name'])}</a></h2>
    <p class="muted">{esc(a['short'])}</p>
    <div class="btns"><a class="btn pri" href="{page}">{t['more']}</a>{store_buttons(app, lang)}</div>
  </div></div>""")
    other = "en/" if lang == "ko" else "../"
    body = f"""
<header class="top"><span></span><a href="{other}" hreflang="{other_lang(lang)}">{t['other_lang']}</a></header>
<div class="home-head"><h1>parkho79 Apps</h1><p class="muted">{esc(t['site_lead'])}</p></div>
<div class="list">{''.join(rows)}
</div>
<footer class="foot"><span>{t['contact']} <a href="mailto:{EMAIL}">{EMAIL}</a></span><span>© parkho79</span></footer>"""
    return page_html(lang, "parkho79 Apps", t["site_lead"], body, canonical=("" if lang == "ko" else "en/"),
                     alternates={"ko": "", "en": "en/"})


def render_app(app, lang):
    """
    앱 소개 페이지 HTML
    """
    t = TEXT[lang]
    a = app[lang]
    slug = app["slug"]
    # 앱 페이지에서 사이트 뿌리까지 (ko: /<앱>/, en: /<앱>/en/)
    up = "../" if lang == "ko" else "../../"
    img = "img/" if lang == "ko" else "../img/"
    shots = "".join(
        f'<img src="{img}{lang}-{i}.jpg?v={ver(f"{slug}/img/{lang}-{i}.jpg")}" alt=""{t["shots_label"]} {i}" width="540" height="960" loading="lazy">'
        for i in range(1, len(app["shots"][lang][1]) + 1)
    )
    feats = "".join(
        f"<div><h3>{esc(title)}</h3><ul>{''.join(f'<li>{esc(x)}</li>' for x in items)}</ul></div>"
        for title, items in a["features"]
    )
    other = "en/" if lang == "ko" else "../"
    home = up + ("" if lang == "ko" else "en/")
    privacy = "privacy/" if lang == "ko" else "../privacy/"
    body = f"""
<header class="top"><a class="home" href="{home}">{t['home']}</a><a href="{other}" hreflang="{other_lang(lang)}">{t['other_lang']}</a></header>
<div class="app-head"><img class="icon" src="{up}assets/{slug}.png?v={ver(f"assets/{slug}.png")}" alt="" width="88" height="88">
  <div><h1>{esc(a['name'])}</h1><p class="muted">{esc(a['short'])}</p>
    <div class="btns">{store_buttons(app, lang, primary=True)}</div></div></div>
<p class="intro">{esc(a['intro'])}</p>
<div class="shots" aria-label="{t['shots_label']}">{shots}</div>
<section class="sec"><h2>{t['features']}</h2><div class="feat">{feats}</div></section>
<footer class="foot"><a href="{privacy}">{t['privacy']}</a><span>{t['contact']} <a href="mailto:{EMAIL}">{EMAIL}</a></span><span>© parkho79</span></footer>"""
    return page_html(lang, a["store_name"], a["short"], body, canonical=f"{slug}/" + ("" if lang == "ko" else "en/"),
                     alternates={"ko": f"{slug}/", "en": f"{slug}/en/"}, og_image=f"assets/{slug}.png")


def store_buttons(app, lang, primary=False):
    """
    Google Play(와 주소가 있으면 원스토어) 버튼 HTML. primary 면 Play 버튼을 강조한다
    """
    hl = "ko" if lang == "ko" else "en"
    cls = "btn pri" if primary else "btn"
    out = f'<a class="{cls}" href="https://play.google.com/store/apps/details?id={app["play"]}&amp;hl={hl}">Google Play</a>'
    if app["onestore"]:
        out += f'<a class="btn" href="{esc(app["onestore"])}">{TEXT[lang]["onestore"]}</a>'
    return out


def page_html(lang, title, desc, body, canonical, alternates, og_image="assets/phcalendar.png"):
    """
    공통 머리(메타·og 태그·스타일)를 붙인 완성 HTML
    """
    base = "https://parkho79.github.io/"
    alt = "".join(f'<link rel="alternate" hreflang="{k}" href="{base}{v}">' for k, v in alternates.items())
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{base}{canonical}">
{alt}
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="{base}{og_image}?v={ver(og_image)}">
<meta property="og:url" content="{base}{canonical}">
<!-- 이 파일은 tools/build_site.py 로 만든다. 직접 고치지 말고 스크립트를 고쳐 다시 만든다 -->
<style>{CSS}</style>
</head>
<body>
<div class="wrap">{body}
</div>
</body>
</html>
"""


def ver(rel_path):
    """
    그림 주소 뒤에 붙일 버전 (파일 내용 해시 앞 8자리). 그림이 바뀌면 주소가 달라져 브라우저가 예전 그림을 다시 쓰지 않는다
    """
    return hashlib.md5((ROOT / rel_path).read_bytes()).hexdigest()[:8]


def home_path(lang):
    """
    언어별 홈 파일 경로
    """
    return ROOT / ("index.html" if lang == "ko" else "en/index.html")


def app_path(slug, lang):
    """
    언어별 앱 페이지 파일 경로
    """
    return ROOT / slug / ("index.html" if lang == "ko" else "en/index.html")


def other_lang(lang):
    """
    전환 링크가 가리키는 언어 코드
    """
    return "en" if lang == "ko" else "ko"


def esc(s):
    """
    HTML 에 넣을 문자열 이스케이프
    """
    return html.escape(s, quote=True)


def write(path, text):
    """
    폴더를 만들고 UTF-8 로 쓴다
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
