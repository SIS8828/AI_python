# 데이터 분석에 유용한 기능들....
# - split (구분자): 구분자로 구분, 기본값은 공백

test_text = 'song-il-su-with-python'
print(test_text.split('-'))


# 구분자.join(리스트): split 함수와 반대로 구분자로 붙인다.

test_text = ['song', 'il', 'su', 'with', 'python']
print(test_text)
cal = '+'
result = cal.join(test_text)
print(result)

# split() 와 join() 응용
result = '-'.join('345.234.6789'.split('.'))
print(result) #  345.234.6789 -> 345-234-6789 바뀜

# enumerate(list)  : 인덱스와 값을 함께 반환

for i, name in enumerate(['a','b','c','d']):
    print(i,name)

'''
0 a
1 b
2 c
3 d
'''

seq = ['mon','tue','wed','thu','fri','sat','sun']
print(dict(enumerate(seq)))

key_seq = 'abcdefg'
value_seq = ['mon','tue','wed','thu','fri','sat','sun']
print(dict(zip(key_seq,value_seq)))
# {'a': 'mon', 'b': 'tue', 'c': 'wed', 'd': 'thu', 'e': 'fri', 'f': 'sat', 'g': 'sun'}

# List comprehesion - 리스트 변환하는 표현식으로 유용한 기능
day = ['mon','tue','wed','thu','fri','sat','sun']
print([x for x in day]) # ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

data = [35,56,-53,45,27,-28,8,-12]
print([x for x in data if x >= 0 ]) #[35, 56, 45, 27, 8]

print([x **2for x in data if x >= 0 ]) #[1225, 3136, 2025, 729, 64]


# Counter를 이용한 카운팅
#       - Countsms 아이템의 갯수를 자동으로 카운팅
from collections import Counter

message = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer et augue blandit, cursus ex ac, mollis urna. Duis fermentum consequat ultrices. Nam porttitor nibh a urna tempor, auctor efficitur lacus tincidunt. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Maecenas posuere ipsum vel metus aliquet consequat. Nullam vulputate, odio vel bibendum tempus, libero arcu ornare augue, non malesuada enim ante at arcu. Morbi dui ipsum, finibus quis consequat a, euismod in ante. Proin id finibus sapien, eu viverra neque. Duis in mauris turpis. Morbi pellentesque mauris et varius ullamcorper. Vestibulum consequat augue ac pellentesque suscipit. Ut pellentesque dolor non purus porttitor, ut ultrices nibh sodales. Ut varius eget orci eu tristique. Vivamus tincidunt arcu eget eros varius finibus et a ligula.
Etiam ac imperdiet neque. In varius laoreet augue, non faucibus nulla mattis non. Vivamus dignissim augue et nibh hendrerit, nec porttitor orci convallis. Sed enim sem, interdum non velit ac, auctor imperdiet odio. Vestibulum vestibulum semper sapien et venenatis. Nulla convallis purus lectus. Quisque vitae massa sem. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nunc cursus diam eget lacus condimentum laoreet.
Aenean eget aliquam elit, sit amet luctus erat. Morbi tincidunt posuere cursus. Duis porttitor nec neque vel elementum. Maecenas nunc turpis, feugiat vitae dictum rutrum, sodales non nisi. Mauris eleifend mi elit, vel posuere erat tincidunt eu. Phasellus ornare tempor diam non accumsan. Cras at dignissim eros. Fusce eu malesuada risus. Aliquam vestibulum, urna quis auctor blandit, tortor nibh vulputate erat, a convallis turpis ex at lectus. Suspendisse commodo nibh nec massa rutrum gravida. Vivamus porttitor justo eget risus iaculis, ac vehicula urna tristique. Vestibulum sem elit, tristique sit amet massa id, hendrerit aliquet odio. Vestibulum semper nisi ac dui egestas varius.
Integer pellentesque lectus urna, a euismod nisi porttitor vel. Duis a magna nec nunc bibendum finibus. Proin sodales libero et ex congue, vel dictum libero lacinia. Duis eu bibendum sapien. Sed id tortor at diam blandit viverra. Vivamus viverra, tellus sed dapibus efficitur, ex dui vehicula augue, imperdiet fermentum erat nunc vitae risus. Quisque fermentum rutrum ligula, nec gravida tellus semper non. Etiam interdum finibus dolor, quis interdum dolor posuere eget. Pellentesque nec aliquet orci.
Donec ullamcorper risus ac commodo feugiat. Morbi eleifend pharetra magna. Fusce at ex in massa posuere bibendum. Phasellus ac lacus neque. Suspendisse placerat at purus id pretium. Sed blandit quis velit vel faucibus. Donec ornare vel libero volutpat sagittis. Quisque malesuada metus et purus pretium, non rhoncus leo mollis.

"""
counter = Counter(message.split())

print(counter) # dict 형태로 값을 반환해 준다.

print(counter.most_common()) # Count(dict) -> list 로 반환

# list -> dict 형태로 반환
dict_msg = dict(counter.most_common())
print(dict_msg)
print(dict_msg['non']) # 7

