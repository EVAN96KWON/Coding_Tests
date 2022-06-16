## Programmers 12981
### 영어 끝말 잇기

``` python
 words[i - 1][-1] != words[i][0]
```
끝말잇기니까 앞의 단어의 마지막 문자와 현재 단어의 첫번째 문자 비교

``` python 
words[i] in words[:i]
```
지금까지 나온 단어들 중 현재 단어가 있는 지 확인

words 순회 중 위의 조건 만족하면, `return [걸린 사람, 걸린 차례]` 없으면 `[0, 0]`