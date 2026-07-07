import numpy as np

print([1,2,3]*2) # 리스트 복사
v = np.array([1,2,3])
u = np.array([4,5,6])

print(v*2) # 스칼라 곱
print(v+u) # 원소별 합
print(v*u) # *은 원소별 곱

print(np.dot(v,u)) # np.dot은 내적
print(v@u) # @도 내적을 의미