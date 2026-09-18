## en
- **Number: budget LLM cost by token count per language, not character count.** If Number ever pipes readings through an LLM for summarization or tagging, estimate cost separately for Korean and English input, since the same tokenizer charges Korean more per character.
- **alice-tech: log actual token counts for the daily report.** Since alice-tech is generated and read in both languages, track token counts per report rather than word counts, to catch cost drift the two languages produce through the same tokenizer.

## ko
- **Number: LLM 비용을 언어별 토큰 수로 예산 잡는다, 글자 수가 아니라.** Number가 읽기값을 요약이나 태깅을 위해 LLM에 넣는다면, 한국어와 영어 입력의 비용을 따로 추정한다. 같은 토크나이저라도 한국어가 글자당 더 비싸기 때문이다.
- **alice-tech: 일일 리포트의 실제 토큰 수를 기록한다.** alice-tech는 두 언어로 생성되고 읽히므로, 단어 수가 아니라 보고서별 토큰 수를 추적해 같은 토크나이저를 통과한 두 언어가 만드는 비용 편차를 잡아낸다.
