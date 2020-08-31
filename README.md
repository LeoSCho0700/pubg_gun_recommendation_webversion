# pubg_gun_recommendation_webversion
Check out the "pubg_gun_recommendation" file before opening
### Description
이 프로그램은 가상 무장 활동인 PUBG Mobile 플레이어들을 위해 각 상황, 플레이어의 성향별 최적화된 화기를 추천해준다. 무수히 많은 플레이어들이 게임을 즐기고 있지만 어떤 화기가 좋은지, 심지어 어떤 화기가 있는지조차 모르고 그저 무난한 M4나 SCAR를 사용하는게 다반사다. 그래서 모든 화기에 대해 상세히 알고 있지 않은 사람들을 위해 이 프로그램을 만든다. 물론 자신이 직접 전 총기를 사용해보고 자신에게 맞는 것을 찾는것이 이상적이지만, 매우 귀찮고 오래 걸리는 작업이기에 대안으로 이 프로그램을 돌리는 것도 좋을듯 하다.
***
### Environment

+ OS: macOS Catalina 10.15.5
+ Language: Python 3.8
+ IDE: PyCharm CE
+ Database: MySQL 8.0
+ Additional programs: XAMPP, ATOM, Bootstrap, Api 1.0
***
### Code flow
<div>
<img src="https://user-images.githubusercontent.com/70150687/91562229-cee95680-e977-11ea-883d-80c4db28752c.png">
</div>

***
### Function
이 프로그램은 전작인 파이썬 버전과 기능은 일치하므로 설명은 생략한다. 그러나 웹 버전의 기본적인 시스템은 버튼 기반으로, 선택하고 싶은 항목의 버튼을 클릭하는 방식을 채택했다. 그리고 파이썬에는 있을수 없는 이미지나 비주얼적인 부분을 더 보강했다.

html과 bootstrap 프로그램을 이용해서 기본적인 웹 형식을 따왔다. 그리고 프로그램을 돌리기 위해 Api 를 써서 웹의 각 페이지와 연동하는 방식을 썼다. 개발자 모드를 키지 않은 상태에서는 각 맵, 탄약, 상황 등의 이미지들을 클릭해서 시각적으로 총을 뽑아낼 수 있다. 마지막으로 강렬한 인상을 위해 디자인은 보색을 주로 채용했다. 바이러스는 아마 없다.

아직은 인터넷에서 고유 주소를 타고 들어가는 것은 불가능하지만, 구현을 고려하고 있다.


