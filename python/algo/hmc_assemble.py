# https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=403

# 2
# 1 3 1 2
# 10 2

# 4

# A, B 라인
# N개의 작업장있음

# A1에서 최초 시작

# 1 3 1 2
# Ai 작업시간, Bi작업시간, Ai->Bi이동시간, Bi->Ai 이동시간
# 10 2
# An 작업시간, Bn작업시간

# 4: 가장 빠른 조립시간

# 1 3 1 2
# 10 2

# a1(1)  b1(3)

# a2(10)    1 ->     b2(2)
#        <- 2
#
# 선택 -> 2가지
# 1 3 1 2      10 2 1 2
# 2 11
# 최선인줄 알고 선택했더니, 다음번에 아니한만 못할 수 있다
# Greedy는 안될듯..


if __name__ == '__main__':

