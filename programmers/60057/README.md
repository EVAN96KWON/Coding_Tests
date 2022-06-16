## Programmers 60057
### 문자열 압축

#### def compress
``` python
sliced = [s[i:i+n] for i in range(0, len(s), n)]
```
문자열 s를 n개 단위로 잘라 list로

``` python
while i < len(sliced):
    cnt = 0
    for j in range(i, len(sliced)):
        if sliced[i] != sliced[j]:
            break
        cnt += 1
        i = j
    compressed += str(cnt) + sliced[i] if cnt != 1 else sliced[i]
    i += 1
```
list sliced 순회하면서 i랑 같은 slice가 있는 지 확인

j로 순회하면서 개수 cnt

compressed에 합침

### solution
``` python
compresses = [len(compress(s, i)) for i in range(1, len(s))]
```
문자열 길이 만큼 순회하면서 슬라이스해서 저장하고 최소 길이 반환