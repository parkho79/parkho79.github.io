# parkho79.github.io

parkho79 앱들의 웹 페이지 (GitHub Pages: https://parkho79.github.io/)

## 홈·앱 소개 페이지 (2026-11-17~)

- 홈 `/`(한국어)·`/en/`(영어), 앱 소개 `/<앱>/`·`/<앱>/en/` (phcalendar, phdday, mycalendar)
- `python tools/build_site.py` 로 만든다. HTML 을 직접 고치지 말고 스크립트의 `APPS`·`TEXT` 를 고쳐 다시 만든다.
  - 그림(아이콘 `assets/<앱>.png`, 스크린샷 `<앱>/img/<언어>-<번호>.jpg`)은 스토어 등록정보 원본에서 줄여 복사한다.
    원본이 없는 PC 에서는 `--pages-only` 로 페이지만 만든다. 원본 위치는 `PH_DEV` 환경 변수(기본 `E:/PH_dev`).
  - 스토어 문구·스크린샷을 바꾸면 여기도 다시 만든다.
  - 그림 주소 뒤에 파일 내용으로 만든 버전(`?v=…`)이 붙는다. 그림이 바뀌면 주소가 달라져 브라우저가 예전 그림을 다시 쓰지 않는다.
  - 원스토어 주소는 `APPS` 의 `onestore` 에 넣으면 버튼이 생긴다 (비어 있으면 Google Play 버튼만).

## 개인정보처리방침

| 앱 | 개인정보처리방침 |
|---|---|
| 간편 음력 달력 (PhCalendar) | https://parkho79.github.io/phcalendar/privacy/ |
| D-Day 디데이 위젯 (PhDday) | https://parkho79.github.io/phdday/privacy/ |
| My Calendar | https://parkho79.github.io/mycalendar/privacy/ |

- 스토어(Play Console, 원스토어)에 등록한 주소이므로 폴더 이름을 바꾸지 않는다.
- 앱의 권한·SDK 가 바뀌면 해당 방침과 "최종 수정일"을 함께 고친다.
- 예전 주소 https://parkho79.github.io/MyCalendarIndex/ 는 이 저장소의 My Calendar 방침으로 넘겨 주는 페이지로 남긴다.
  (`MyCalendarIndex/` 폴더를 이 저장소에 만들지 않는다)

## 첫 페이지

- `index.html`: Play 개발자 프로필의 웹사이트(판매자 상태 선언 뒤 EU 사용자에게도 공개)라 앱 소개·Play 링크·방침·문의를 한국어·영어로 둔다.
  아이콘은 `assets/`(앱 런처 아이콘 192px). 주소·전화번호는 넣지 않는다(판매자 정보는 Play가 따로 보여 준다).

## 앱 공유 링크

| 앱 | 공유 링크 (메신저 미리보기용) |
|---|---|
| My Calendar | https://parkho79.github.io/mycalendar/share/ (한국어: `share/ko/`) |

- Play 스토어 페이지는 og 태그가 HTML 1MB 뒤에 있어 카카오톡 미리보기가 안 나온다. 앱 "추천하기"는 og 태그만 맨 앞에
  둔 이 페이지를 보내고, 열면 Play 스토어로 바로 넘긴다.
- 앱이 보내는 주소이므로 폴더 이름을 바꾸지 않는다. 이미지(`feature.png`)는 스토어 그래픽 이미지(1024×500)를 복사한 것.
- 카카오톡은 주소별로 미리보기를 캐시한다. 내용을 고친 뒤 반영이 안 되면 카카오 공유 디버거에서 캐시를 지운다.

## app-ads.txt

- `app-ads.txt`: AdMob 앱 인증용(게시자 ID `pub-1383814903593125`). Play 등록정보의 개발자 웹사이트가 `https://parkho79.github.io`여야
  AdMob이 이 파일을 찾는다. 광고 네트워크를 더하면 그 줄을 덧붙인다.
