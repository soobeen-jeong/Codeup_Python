# 어떤 형식에 맞추어 시간이 입력될 때, 그대로 출력하는 연습을 해보자.
# 콜론(:) 기호를 기준으로 두 수가 각 변수에 저장된다.
#
# 입력 : 3:15
# 출력 : 3:15
#
# Tip::
#
# split()의 매개변수로 문자열을 분할하기 위한 기준을 정의할 수 있다.
# 문자열의 메소드(함수)인 format()을 이용하면 문자열 내부에 변수값을 대입할 수 있다.
h, m = input().split(':')
print('{}:{}'.format(h, m))