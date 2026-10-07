import turtle       # 파이썬 그래픽 처리를 위한 터틀 라이브러리 로드
import math         # 삼각함수(sin, cos) 및 라디안 변환을 위한 수학 라이브러리 로드
from datetime import datetime  # 컴퓨터의 실제 현재 날짜와 시간을 가져오기 위한 라이브러리 로드

# ─── [1] 우주 공간 및 그래픽 환경 세팅 ───
screen = turtle.Screen()        # 터틀이 그림을 그릴 기본 스크린 객체 생성
screen.setup(950, 950)          # 8대 행성을 모두 담을 수 있도록 가로 950, 세로 950 픽셀 크기로 창 크기 설정
screen.bgcolor("#030308")       # 우주의 깊고 어두운 느낌을 주기 위해 검은색에 가까운 암청색(#030308) 배경 적용
screen.tracer(0, 0)             # 그래픽 자동 그리기를 끄고(0), 프로그래머가 원할 때만 화면을 갱신하도록 설정 (렉 방지 및 부드러운 애니메이션 필수)

t = turtle.Turtle()             # 그림을 그려나갈 펜(터틀 소환) 객체 생성
t.speed(0)                      # 터틀의 자체 드로잉 속도를 최고 속도(0)로 설정
t.hideturtle()                  # 화면에 터틀 화살표 아이콘이 보이지 않도록 숨김 처리
t.getscreen()._minus_one = lambda *args: None  # 터틀 그래픽 엔진 내부의 불필요한 예외 처리를 무시하여 연산 속도를 극대화하는 최적화 코드

# ─── [2] 8대 행성 및 주요 위성 천문학 고증 데이터 세팅 ───
# 구조설명: name(이름), radius(태양으로부터의 거리-픽셀), size(행성 크기), color(색상), 
#          start_angle(기준일 각도), real_speed(지구 기준 상대적 공전 속도), moons(거느린 위성 목록)
planets_data = [
    {
        "name": "수성", "radius": 55, "size": 4, "color": "#A1A1A1", "start_angle": 120.0, "real_speed": 4.15,
        "moons": [] # 수성은 자연 위성이 존재하지 않음
    },
    {
        "name": "금성", "radius": 95, "size": 7, "color": "#E3A857", "start_angle": 240.0, "real_speed": 1.62,
        "moons": [] # 금성은 자연 위성이 존재하지 않음
    },
    {
        "name": "지구", "radius": 145, "size": 8, "color": "#2B82C9", "start_angle": 0.0, "real_speed": 1.00,
        "moons": [
            # distance: 모행성(지구)으로부터의 거리, size: 달의 크기, color: 달의 색상, speed: 달의 자체 공전 속도
            {"name": "달", "distance": 18, "size": 2, "color": "#FFFFFF", "speed": 6.5}
        ]
    },
    {
        "name": "화성", "radius": 200, "size": 6, "color": "#C1440E", "start_angle": 45.0, "real_speed": 0.53,
        "moons": [
            {"name": "포보스", "distance": 11, "size": 1.5, "color": "#A09990", "speed": 8.5},
            {"name": "데이모스", "distance": 15, "size": 1.2, "color": "#88827A", "speed": 6.0}
        ]
    },
    {
        "name": "목성", "radius": 265, "size": 15, "color": "#D8A06A", "start_angle": 180.0, "real_speed": 0.25,
        "moons": [
            {"name": "이오", "distance": 18, "size": 2.2, "color": "#FFD700", "speed": 5.5},
            {"name": "유로파", "distance": 22, "size": 2.0, "color": "#E5E5E5", "speed": 4.2},
            {"name": "가니메데", "distance": 27, "size": 2.5, "color": "#B0C4DE", "speed": 3.0},
            {"name": "칼리스토", "distance": 32, "size": 2.3, "color": "#708090", "speed": 2.1}
        ]
    },
    {
        "name": "토성", "radius": 340, "size": 12, "color": "#E2BF7D", "start_angle": 310.0, "real_speed": 0.18,
        "moons": [
            {"name": "미마스", "distance": 17, "size": 1.2, "color": "#C0C0C0", "speed": 6.0},
            {"name": "엔셀라두스", "distance": 21, "size": 1.5, "color": "#F0F8FF", "speed": 4.8},
            {"name": "테티스", "distance": 25, "size": 1.7, "color": "#DCDCDC", "speed": 3.8},
            {"name": "타이탄", "distance": 31, "size": 3.2, "color": "#FFDEAD", "speed": 2.5},
            {"name": "이아페투스", "distance": 36, "size": 1.8, "color": "#555555", "speed": 1.5}
        ]
    },
    {
        "name": "천왕성", "radius": 410, "size": 10, "color": "#70D6FF", "start_angle": 95.0, "real_speed": 0.11,
        "moons": [
            {"name": "미란다", "distance": 14, "size": 1.2, "color": "#E0E0E0", "speed": 5.0},
            {"name": "아리엘", "distance": 18, "size": 1.8, "color": "#D3D3D3", "speed": 3.8},
            {"name": "엄브리엘", "distance": 22, "size": 1.6, "color": "#A9A9A9", "speed": 2.9},
            {"name": "티타니아", "distance": 26, "size": 2.2, "color": "#F5F5F5", "speed": 2.2},
            {"name": "오베론", "distance": 30, "size": 2.0, "color": "#DCDCDC", "speed": 1.6}
        ]
    },
    {
        "name": "해왕성", "radius": 470, "size": 9, "color": "#0047AB", "start_angle": 15.0, "real_speed": 0.08,
        "moons": [
            {"name": "프로테우스", "distance": 15, "size": 1.5, "color": "#696969", "speed": 4.5},
            {"name": "트리톤", "distance": 20, "size": 2.5, "color": "#FDF5E6", "speed": -3.0}, # 음수값 적용으로 역방향 공전 구현
            {"name": "네레이드", "distance": 26, "size": 1.2, "color": "#808080", "speed": 1.8}
        ]
    }
]

# ─── [3] 실시간 날짜 동기화 연산 과정 ───
now = datetime.now()                # 현재 프로그램을 실행한 시점의 년-월-일-시-분-초 데이터를 읽어옴
day_of_year = now.timetuple().tm_yday # 현재 날짜가 1월 1일(1)을 시작으로 오늘이 올해의 몇 번째 날(Day)인지 1~365 정수로 반환

initial_angles = []                 # 오늘 날짜에 딱 맞춘 각 행성의 초기 시작 각도를 보관할 빈 리스트 생성
for p in planets_data:
    # 공식: [1월 1일 기준 기준 각도] + ([올해 흘러온 일수] * [하루 공전 각도량])
    today_angle = p["start_angle"] + (day_of_year * p["real_speed"])
    # 360도를 넘어가면 다시 0도부터 순환하도록 360으로 나눈 나머지(%)만 저장
    initial_angles.append(today_angle % 360)

time_frame = 0                      # 가상 시뮬레이션 환경 내에서 시간이 흘러감을 기록할 타임 타이머 변수 초기화

# ─── [4] 실시간 메인 루프 드로잉 함수 정의 ───
def draw_complete_solar_system():
    global time_frame               # 함수 외부에서 선언된 전역 변수 time_frame을 함수 내부에서 수정할 수 있도록 연동
    t.clear()                       # 잔상이 남지 않도록 이전 프레임(화면)에 그려진 모든 그림을 깨끗이 지움
    
    # [최적화 꿀팁] 매번 t.penup()을 호출하는 것보다 로컬 변수에 주소를 바인딩해 두면 파이썬 연산 속도가 비약적으로 상승함
    t_penup = t.penup
    t_pendown = t.pendown
    t_goto = t.goto
    t_color = t.color
    t_dot = t.dot
    t_setheading = t.setheading
    t_pensize = t.pensize
    t_circle = t.circle
    
    # ─── [4-1] 태양계의 심장: 중심 태양(Sun) 그리기 ───
    t_penup()                       # 선을 긋지 않도록 펜을 들어 올림
    t_goto(0, 0)                    # 태양계의 정중앙 좌표인 (0, 0)으로 펜을 이동
    t_color("#FF4500")              # 태양의 색상(타오르는 붉은 오렌지색) 지정
    t_dot(32)                       # 중심 위치에 지름 32 픽셀 크기의 꽉 찬 점(태양)을 찍음
    
    # ─── [4-2] 8대 행성 및 전 위성 순회 드로잉 시작 ───
    for i, planet in enumerate(planets_data): # planets_data 내부를 인덱스 번호(i)와 행성 정보(planet)로 쪼개어 반복문 가동
        
        # 1단계: 정갈한 정원 형태의 행성 고정 궤도선 그리기
        t_penup()                   
        t_goto(0, -planet["radius"]) # 원의 맨 아래쪽 시작점으로 이동 (중심이 0,0이므로 Y축 하단으로 반지름만큼 하강)
        t_setheading(0)             # 터틀의 머리 방향을 동쪽(오른쪽)으로 셋팅
        t_color("#121820")          # 우주 배경과 자연스럽게 매칭되도록 어둡고 흐린 회그린 색상 지정
        t_pensize(0.5)              # 선이 너무 튀지 않도록 가장 가늘고 세련된 두께로 고정
        t_pendown()                 # 선을 그리기 위해 펜을 도화지에 내려놓음
        t_circle(planet["radius"])  # 지정된 반지름 크기만큼 360도 완벽한 동심원 트랙(궤도선)을 그림
        
        # 2단계: 과학 법칙이 반영된 행성의 실시간 위치 좌표 연산
        # 공식: [오늘 시작 시점의 실제 각도] + ([가상 흘러간 시간] * [행성 고유 속도])
        planet_angle = initial_angles[i] + (time_frame * planet["real_speed"])
        planet_rad = math.radians(planet_angle) # 파이썬 삼각함수는 '도(Degree)'가 아니라 '라디안(Radian)'을 쓰므로 단위 변환 필수!
        
        # 삼각함수를 통한 원 운동 극좌표 계산법 적용
        # X축 좌표 = 중심점(0) + 반지름 * 코사인(각도)
        # Y축 좌표 = 중심점(0) + 반지름 * 사인(각도)
        planet_x = planet["radius"] * math.cos(planet_rad)
        planet_y = planet["radius"] * math.sin(planet_rad)
        
        # 3단계: 계산 완료된 좌표에 행성 본체 그리기
        t_penup()                   
        t_goto(planet_x, planet_y)  # 방금 삼각함수로 유도해 낸 행성의 실시간 (X, Y) 좌표로 순간이동
        t_color(planet["color"])    # 해당 행성이 가진 고유의 컬러 적용
        t_dot(planet["size"])       # 데이터 셋에 입력된 크기 비율대로 꽉 찬 점(행성 본체)을 그림
        
        # ─── [4-3] 특별 기믹: 지구 한정 ISS(국제우주정거장) 서브 루틴 가동 ───
        if planet["name"] == "지구": # 루프를 돌다가 현재 그리고 있는 행성이 '지구'일 때만 조건문 진입
            # ISS는 실제 고증상 지구 표면에 거의 스치듯 밀착해 있고 속도가 초고속임
            iss_angle = time_frame * 25.0 # 달보다 훨씬 강력한 회전 속도 가중치 부여
            iss_rad = math.radians(iss_angle) # 라디안 단위 변환
            
            # 지구 본체의 현재 중심 좌표(planet_x, planet_y)를 기반으로 하여 거리 6만큼만 벌려서 원 운동 좌표 계산
            iss_x = planet_x + 6 * math.cos(iss_rad)
            iss_y = planet_y + 6 * math.sin(iss_rad)
            
            t_penup()
            t_goto(iss_x, iss_y)    # 계산된 우주정거장 좌표로 이동
            t_color("#00FFFF")      # 인공 우주 구조물 특유의 밝고 선명한 네온 사이언(하늘색) 적용
            t_dot(1.5)              # 아주 미세한 인공 점 크기로 렌더링
        
        # ─── [4-4] 각 행성에 딸린 자연 위성(Moons) 드로잉 루틴 가동 ───
        for m_idx, moon in enumerate(planet["moons"]): # 해당 행성이 보유한 위성 개수만큼 내부 루프 가동 (m_idx는 위성 일련번호)
            # 위성 고유의 공전 각도 계산 (위성 고유 속도 반영 및 여러 위성이 겹치지 않게 인덱스별로 30도씩 분산 시작 오프셋 부여)
            moon_angle = (time_frame * moon["speed"]) + (m_idx * 30)
            moon_rad = math.radians(moon_angle) # 라디안 단위 변환
            
            # ISS와 동일하게, 행성의 현재 중심 좌표(planet_x, planet_y)를 기준으로 삼아 위성의 궤도 공간 확보
            moon_x = planet_x + moon["distance"] * math.cos(moon_rad)
            moon_y = planet_y + moon["distance"] * math.sin(moon_rad)
            
            t_penup()
            t_goto(moon_x, moon_y)  # 위성 좌표로 이동
            t_color(moon["color"])  # 위성 고유 색상(예: 달은 흰색) 적용
            t_dot(moon["size"])     # 지정된 위성 크기대로 점 드로잉
            
    screen.update()                 # [중요] 버퍼 메모리에 몰래 그려둔 완벽한 태양계 한 프레임을 모니터 화면에 단 한 번에 출력 (깜빡임 완벽 제거)
    
    time_frame += 0.25              # 다음 프레임이 그려질 때 행성들이 멈춰있지 않고 조금씩 앞으로 전진하도록 가상 시간 축 축적 (공전 속도 마스터 키)
    screen.ontimer(draw_complete_solar_system, 5) # 0.005초(5ms)의 간격을 두고 이 함수 자기 자신을 다시 강제 호출 (무한 루프 애니메이션 구동 엔진)

# ─── [5] 시스템 시뮬레이터 최종 가동 가속 서브 루틴 ───
draw_complete_solar_system()        # 함수를 최초 1회 수동 실행하여 무한 루프의 첫 시동을 걸어줌
screen.mainloop()                   # 프로그램이 끝나고 창이 바로 닫히지 않도록 마우스 클릭이나 강제 종료 전까지 그래픽 창을 유지하는 대기 모드