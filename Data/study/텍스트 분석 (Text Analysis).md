# 텍스트 분석 (Text Analysis)

- NLP(National Language Processing) / TA(Text Analysis/텍스트 분석)
  - 머신러닝이 보편화되면서 이 둘을 구분하는 것이 큰 의미는 없어짐...
  - NLP
    - 머신이 인간의 언어를 이해하고 해석하는 데 더 중점을 두고 기술이 발전했음.
  - TA (텍스트 마이닝/Text Mining 이라고도 불림)
    - 비정형 텍스트에서 의미 있는 정보를 추출하는 것에 조금 더 중점을 두고 기술이 발전했음.





- 머신러닝, 언어 이해, 통계 등을 활용해 모델을 수립하고 정보를 추출해

  비즈니스 인텔리전스(Business Intelligence)나 예측 분석 등의 분석 작업을 주로 수행함.



- TA의 "기술 영역"

  - 텍스트 분류(Text Classification)

    - Text Categorization 이라고도 함.

    - 문서가 특정 분류 또는 카테고리에 속하는 것을 예측하는 기법을 통칭.

    - 예 : 특정 신문 기사 내용이 연애/정치/사회/문화 중 어떤 카테고리에 속하는지 자동으로 분류하거나,

      ​       스팸 메일 검출 같은 프로그램 등등

    - 지도학습을 적용.

  - 감성 분석(Sentiment Analysis)

    - 텍스트에서 나타나는 감정/판단/믿음/의견/기분 등의 주관적인 요소를 분석하는 기법을 총칭.
    - 예 : 소셜 미디어 감정 분석, 영화나 제품에 대한 긍정, 리뷰/여론조사 의견 분석 등등
    - Text Analytics에서 가장 활발하게 사용되고 있는 분야.
    - 지도학습 방법뿐만 아니라 비지도학습을 이용해 적용할 수 있음.

  - 텍스트 요약(Summarization)

    - 텍스트 내에서 중요한 주제나 중심 사상을 추출하는 기법.
    - 대표적으로 "토픽 모델링(Topic Modeling)"이 있음.

  - 텍스트 군집화(Clustering)와 유사도 측정

    - 비슷한 유형의 문서에 대해 군집화를 수행하는 기법.
    - 텍스트 분류를 비지도학습으로 수행하는 방법의 일환으로 사용될 수 있음.
    - 유사도 측정 : 문서들간의 유사도를 측정해, 비슷한 문서끼리 모을 수 있는 방법.







✅ 머신러닝의 학습 방법 3가지

[지도학습 / 비지도학습 / 강화학습](https://ebbnflow.tistory.com/165)

- 지도학습
  - **정답이 있는 데이터**를 활용해 데이터를 학습시키는 방법.
  - 종류 : 분류(Classification), 회귀(Regression)
- 비지도학습
  - **정답 라벨이 없는 데이터**를 비슷한 특징끼리 군집화 하여 새로운 데이터에 대한 결과를 예측하는 방법.
  - 대표적인 종류 : 클러스터링(Clustering)

~~- 지도/비지도 학습 모델(Semi-Supervised Learning)~~

- 강화학습
  - 행동 심리학에서 나온 이론
  - 분류할 수 있는 데이터가 존재하는 것도 아니고, 데이터가 있어도 정답이 따로 정해져 있지 않음.
  - 자신이 한 행동에 대한 보상(reward)를 받으며 학습하는 것.







### 1. 텍스트 분석 이해

- 텍스트 분석 : 비정형 데이터인 텍스트를 분석하는 것.

  - 비정형 텍스트 데이터를 피처 형태로 추출하는 것이 중요!

- 피처 벡터화(Feature Vectorization) / 피처 추출(Feature Extraction)

  - 텍스트를 word(또는 word의 일부분) 기반의 다수의 피처로 추출

    → 이 피처에 단어 빈도수와 같은 숫자 값을 부여

    → 텍스트가 단어의 조합인 벡터값으로 표현될 수 있음!

  - 변환 방법

    - BOW (Bag of Words)
    - Word2Vec



#### 텍스트 분석 수행 프로세스

1. 텍스트 사전 준비작업(텍스트 전처리)
   - 텍스트를 피처로 만들기 전에 사전에 클렌징, 대/소문자 변경, 특수문자 삭제 등의 클렌징 작업, 단어(Word) 등의 토큰화 작업, 의미 없는 단어(Stop word) 제거 작업, 어근 추출(Stemming/Lemmatization) 등의 텍스트 정규화 작업을 수행하는 것.
2. 피처 벡터화/추출
   - 사전 준비 작업으로 가공된 텍스트에서 피처를 추출하고, 여기에 벡터 값을 할당하는 것.
   - 대표적인 방법 : BOW, Word2Vec
     - BOW
       - Count 기반
       - TF-IDF 기반
3. ML 모델 수립 및 학습/예측/평가
   - 피처 벡터화된 데이터 세트에 ML 모델을 적용해 학습/예측 및 평가 수행.





#### 파이썬 기반의 NLP, 텍스트 분석 패키지

- NLTK(National Language Toolkit for Python)
  - 파이썬의 가장 대표적인 NLP 패키지
  - NLP의 거의 모든 영역을 커버
  - 수행 속도 측면에서 아쉬운 부분이 있어서, 실제 대량의 데이터 기반에서는 제대로 활용되지 못하고 있음.
- Gensim
  - "토픽 모델링" 분야에서 가장 두각을 나타내는 패키지.
  - SpaCy와 함께 가장 많이 사용되는 NLP 패키지.
- SpaCy
  - 뛰어난 수행 성능으로 최근 가장 주목 받는 NLP 패키지



- 사이킷런

  - 머신러닝 위주의 라이브러리여서 NLP 패키지에 특화된 라이브러리는 가지고 있지 않음.

    (예 : 어근 처리)

  - 하지만, 텍스트를 일정 수준으로 가공하고 머신러닝 알고리즘에 텍스트 데이터를 피처로 처리하기 위한 편리한 기능을 제공하고 있어서, 이걸로도 충분히 텍스트 분석 할 수 있음.

  - 하지만... 더 다양한 텍스트 분석이 적용돼야하는 경우, 보통 위의 세 가지 NLP 전용 패키지와 함께 결합해 앱을 작성함.





✅ 피처(Feature)

- 머신러닝 : 어떤 데이터를 분류하거나, 값을 예측(회귀)하는 것.
- 데이터의 값을 잘 예측하기 위한 데이터의 특징들 = Feature
- 동의어 : Label, Class, Target, Response, Dependent variable







### 2. 텍스트 사전 준비 작업(텍스트 전처리) - 텍스트 정규화

- 텍스트 정규화

  - 텍스트를 머신러닝 알고리즘이나 NLP 애플리케이션에 입력 데이터로 사용하기 위해

    클렌징, 정제, 토큰화, 어근화 등의 다양한 텍스트 데이터의 사전 작업을 수행하는 것.

    - 클렌징(Cleansing)
    
      - 텍스트에서 분석에 오히려 방해가 되는 불필요한 문자, 기호 등을 사전에 제거하는 작업.
      - 예 : HTML, XML 태그나 특정 기호 등을 제거
    
    - 토큰화(Tokenization)
    
      - 문장 토큰화 (Sentence Tokenization)
    
        - 문서에서 문장을 분리
    
        - 문장의 마침표(.), 개행문자(\n) 등 문장의 마지막을 뜻하는 기호에 따라 분리하는 것이 일반적.
    
          (정규 표현식에 따른 문장 토큰화도 가능)
    
      - 단어 토큰화 (Word Tokenization)
    
        - 문장에서 단어를 토큰으로 분리
    
        - 기본적으로 공백, 콤마(,), 마침표(.), 개행문자 등으로 단어를 분리.
    
          하지만 정규 표현식을 이용해 다양한 유형으로 토큰화 가능.
    
        - 마침표나 개행문자와 같이 "문장"을 분리하는 구분자를 이용해 단어 토큰화 가능
    
          → Bag of Word 같이 단어의 순서가 중요하지 않은 경우, 문장 토큰화를 사용하지 않고 단어 토큰화만 사용해도 충분!
    
          (보통 "문장 토큰화"는 각 문장이 가지는 시맨틱적 의미가 중요할 때 사용)
    
    - 필터링 / 스톱 워드 제거 / 철자 수정
    
      - 스톱 워드 제거
        - 스톱 워드 (Stop Word) : 분석에 큰 의미가 없는 단어. (예 : is, the, a, will 등)
        - 문법적 특성상 빈번하게 텍스트에 나타남 → 미리 제거하지 않으면, 빈도 높아서 중요하게 인식될 수 있음.
        - 언어별로 스톱 워드가 목록화돼 있음. (NLTK가 가장 다양한 언어의 스톱 워드 제공)
    
    - Stemming / Lemmatization
    
      - 문법적 또는 의미적으로 변화하는 단어의 원형을 찾는 것.
    
        (예 : working → work)
    
      - Stemming
    
        - 원형 단어로 변환 시, 일반적인 방법을 적용하거나 더 단순화된 방법을 적용
    
          → 원래 단어에서 일부 철자가 훼손된 어근 단어를 추출하는 경향이 있음.
    
      - Lemmatization
    
        - 품사와 같은 문법적인 요소와 더 의미적인 부분을 감안해, 정확한 철자로 된 어근 단어를 찾아줌.
        - 그래서 Stemming보다 변환 시간이 더 오래 걸림.







### 3. Bag of Words (BOW)

- 문서가 가지는 모든 단어를 문맥이나 순서를 무시하고 일괄적으로 단어에 대해 빈도 값을 부여해 피처 값을 추출하는 모델.

- 이름 뜻 : 문서 내 모든 단어를 한꺼번에 봉투 안에 넣은 뒤 흔들어서 섞는다는 의미.

- 장단점

  - 장점

    - 쉽고 빠른 구축
    - 단순히 단어의 발생 횟수에 기반하지만, 예상보다 문서의 특징을 잘 나타내서 활용도가 높음.

  - 단점

    - 문맥 의미(Semantic Context) 반영 부족

      - 단어의 순서를 고려하지 않아서, 문장 내에서 단어의 문맥적인 의미가 무시됨.
      - 보완하기 위해 n_gram 기법을 활용할 수 있지만, 제한적인 부분에 그쳐 문맥적인 해석을 처리하지 못함...

    - 희소 행렬 문제(희소성, 희소 행렬)

      - 많은 문서에서 단어를 추출하면, 매우 많은 단어가 칼럼으로 만들어지는데, 문서마다 서로 다른 단어로 구성되기 때문에, 단어가 문서마다 나타나지 않는 경우가 훨씬 많음.

        → 대규모 칼럼으로 구성도니 행렬에서 대부분의 값이 0으로 채워지는 희소 행렬이 나타나게 됨.

        → 일반적으로 희소 행렬은 ML 알고리즘의 수행 시간과 예측 성능을 떨어뜨림.

        → 희소 행렬을 위한 특별한 기법 사용 (COO, CSR)





#### BOW 피처 벡터화

- 머신러닝 알고리즘은 일반적으로 숫자형 피처를 데이터로 입력받아 동작함.

  → 텍스트는 머신러닝 알고리즘에 바로 입력할 수 없음!

  → "피처 벡터화"가 필요 (특정 의미를 가지는 숫자형 값인 벡터로 변환해주는 과정)

- 방식 2가지

  - 카운트 기반

    - 각 문서에서 해당 단어가 나타나는 횟수, 즉 Count를 단어의 피처값으로 부여.
    - 카운트 값이 높을수록 중요한 단어로 인식.
    - 문제점 : 언어의 특성상 문장에 자주 사용될 수밖에 없는 단어까지 높은 값을 부여...

  - TF-IDF(Term Frequency - Inverse Document Frequency) 기반

    - 위의 문제점을 보완하기 위해 사용됨.

    - 개별 문서에서 자주 나타나느 ㄴ단어에 높은 가중치를 주되,

      모든 문서에서 전반적으로 자주 나타나는 단어에 대해서는  페널티를 주는 방식.

    - 문서마다 텍스트가 길고 문서의 개수가 많은 경우에는, 이 방식을 사용하는 것이 예측 성능이 더 좋음.

- 사이킷런
  - Count → "CountVectorizer"
  - TF-IDF → "TfidfVectorizer"



#### BOW 벡터화를 위한 희소 행렬

- 희소 행렬 : 너무 많은 불필요한 0값이 메모리 공간에 할당돼,

  메모리 공간이 많이 필요하고, 행렬의 크기가 커서 연산 시에도 시간이 많이 소모됨.

  → 적은 메모리 공간 차지할 수 있도록 변환해야 됨.

  → COO 형식 / CSR 형식 (보통 계산 수행 능력이 더 뛰어난 CSR 형식 사용)

- 파이썬에서는 희소 행렬 변환을 위해 주로 "사이파이(Scipy)" 사용

- COO 형식 (Coordinate : 좌표)

  - 0이 아닌 데이터만 별도의 데이터 배열에 저장하고,

    그 데이터가 가리키는 행과 열의 위치를 별도의 배열로 저장하는 방식.

  - Scipy의 sparse 패키지 사용

- CSR 형식 (Compressed Sparse Row)

  - COO 형식이 행과 열의 위치를 나타내기 위해 반복적인 위치 데이터를 사용해야 하는 문제점을 해결한 방식.

  - 행 위치 배열이 0부터 순차적으로 증가하는 값으로 이뤄졌다는 특성을 고려

    → 행 위치 배열의 고유한 값의 시작 위치만 표기하는 방법으로 이러한 반복 제거 가능.







### 4. 텍스트 분류 실습 - 20 뉴스그룹 분류

- 텍스트 정규화

- 피처 벡터화 변환 & 머신러닝 모델 학습/예측/평가

  - CountVectorization
    - train에 사용한 피처 사용할 수 있도록, test에다가 fit() 다시 하지 말고 cnt_vect.transform() 이용해서 변환하기!
  - Logistic
    - 희소 행렬 분류를 효과적으로 잘 처리할 수 있는 알고리즘 : 로지스틱 회귀, 선형 서포트 벡터 머신, 나이브 베이즈 등

- 사이킷런 파이프라인(Pipeline) 사용 & GridSearchCV와의 결합

  - Pipeline

    - 이 클래스를 이용하면, 피처 벡트화와 ML 알고리즘 학습/예측을 위한 코드 작성을 한 번에 진행할 수 있음.
    - 또, 대용량 데이터의 피처 벡터화 결과를 별도 데이터로 저장하지 않고 스트림 기반에서 바로 머신러닝 알고리즘의 데이터로 입력할 수 있음 → 수행 시간 절약 가능.

  - GridSearchCV

    - 이 클래스의 생성 파라미터로 Pipeline을 입력해주면,

      Pipeline 기반에서도 하이퍼 파라미터 튜닝을 GridSearchCV 방식으로 진행할 수 있음.

    - 피처 벡터화를 위한 파라미터와 ML 알고리즘의 하이퍼 파라미터를 모두 한 번에 GridSearchCV를 이용해 최적화할 수 있음.







### 5. 감성 분석 (Sentiment Analysis)

- 문서의 주관적인 감성/의견/감정/기분 등을 파악하기 위한 방법
- 소셜 미디어, 여론조사, 온라인 리뷰, 피드백 등 다양한 분야에서 활용.
- 문서 내 텍스트가 나타내는 여러 가지 주관적인 단어와 문맥을 기반으로 감성(Sentiment) 수치를 계산.
  - 감성 지수 - 긍정 감성 지수 / 부정 감성 지수
    - 이 둘을 합산해 긍정 감성 / 부정 감성을 결정



- 학습 방법 2가지

  - 지도 학습

    - 학습 데이터와 타깃 레이블 값을 기반으로 감성 분석 학습을 수행한 뒤

      이를 기반으로 다른 데이터의 감성 분석을 예측하는 방법

      (일반 텍스트 기반 분류와 거의 동일)

  - 비지도 학습

    - "Lexicon"이라는 일종의 감성 어휘 사전을 이용.
      - 감성 분석을 위한 용어와 문맥에 대한 다양한 정보를 가지고 있음.
      - 이를 이용해 문서의 긍정 / 부정 감성 여부를 반단.







### 6. 토픽 모델링 (Topic Modeling)

- 문서 집합에 숨어 있는 주제를 찾아내는 것.

  - 사람 - "문장"으로 요약 / 머신러닝 기반 - "단어"로 요약

- 기법 2가지

  - LSA (Latent Semantic Analysis)

  - LDA (Latent Dirichlet Allocation)

    - 우선, 학습 데이터로 피처 벡터화 하고, 그 데이터 세트를 기반으로 LDA 토픽 모델링 수행.

    - 그러면 개별 토픽별로 각 word 피처가 얼마나 많이 그 토픽에 할당됐는지 수치가 나옴.

      (높을수록 해당 word 피처는 그 토픽의 중심 word가 됨.)

    - 연관도 높은 순서대로 출력해서, 각 토픽별로 어떤 단어가 핵심인지 살펴볼 수 있음.







### 7. 문서 군집화 (Document Clustering)

- 비슷한 텍스트 구성의 문서를 군집화 하는 것.

- 동일한 군집에 속하는 문서를 같은 카테고리 소속으로 분류.

- 텍스트 분류 기반 문서 분류와 유사하지만,

  텍스트 분류 기반 분류는 사전에 결정 카테고리 값을 가진 학습 데이터 세트가 필요하고 (지도 학습)

  문서 군집화는 학습 데이터 세트 필요 없음. (비지도 학습)







### 8. 문서 유사도

- 일반적으로 "코사인 유사도(Cosine Similarity)" 사용.
  - 벡터 간의 유사도를 비교하는 방법. (방향이 얼마나 유사한지)
  - 두 벡터 사이의 각도를 구함. (각도 작을수록 가까움 → 수치 작을수록 비슷)
  - 사용 이유
    - 문서를 피처 벡터화 변환하면, 보통 희소 행렬이 됨.
    - 희소 행렬 기반에서, 유클리드 거리 기반 지표 등 벡터 간의 크기에 기반한 유사도 지표는 정확도가 떨어질 확률이 큼.
    - 또, 문서의 길이에 따라 빈도수가 달라지기 때문에, 빈도수 자체보다는 "비율"로 보는 것.







### 9. 한글 텍스트 처리



#### 한글 NLP 처리의 어려움

- 보통 한글 언어 처리는 영어 등의 라틴어 처리보다 어려움.
  - 주된 이유 : "띄어쓰기"와 "다양한 조사" 때문.
    - 띄어쓰기 : 아버지 가방에 들어가신다. vs. 아버지가 방에 들어가신다. (실수하면 기계가 알아보기 힘들어짐.)
    - 다양한 조사 : 워낙 경우의 수가 많아서, 어근 추출(Stemming/Lemmatization) 등의 전처리가 매우 까다로움.



#### KoNLPy (콘엘파이)

- 대표적인 한글 형태소 패키지.
  - 형태소 : 단어로서 의미를 가지는 최소 단위
  - 형태소 분석(Morphological analysis) : 말뭉치를 형태소 어근 단위로 쪼개고 각 형태소에 품사 태깅(POS tagging)을 부착하는 작업.
- 이거 이전에는 파이썬 기반의 형태소 분석 프로그램이 거의 없었음. (대부분 C/C++, Java 기반 패키지)









✅ 로지스틱 회귀 (Logistic Regression)

- 범주형 변수를 예측하는 모델
- 등장 배경
  - **다중 선형 회귀(Multiple LInear Regression)** : 수치형 변수들간의 관계를 선형으로 가정하고 회귀계수를 추정하는 모델.
  - 모델의 정확성을 **오차제곱합**으로 가늠할 수 있음.
  - 그런데 변수가 연속형 숫자가 아닌 **"범주형 변수"**라면?
  - 숫자 그 자체가 아무 의미를 지니지 않기 때문에, 다중선형회귀 모델 사용하면 이상해짐!!
  - 그래서 등장한게 **"로지스틱 회귀"**!!
- 식의 형태가 "로지스틱 함수"의 꼴과 같아서 "로지스틱 회귀"라는 이름을 사용.







---







### 📚 뉴스 분석

E, S, G 각각 데이터를 구했으나, 1년 단위로 구할 수 있는 데이터...

그래서 그 사이의 변화도 계속 반영하고자, 각 기업의 esg 관련 기사 내용을 분석하고 점수로 산정해 esg 점수에 반영할 예정.



#### 뉴스 크롤링 방법

- 네이버 뉴스 api 사용 예정
  - 크롤링을 사용할 수 있지만, 뉴스 본문까지 가져오는건 사이트 측에서 막아놓음...
  - 그래서 네이버 뉴스 api를 사용해서 불러온 데이터 중 "제목"을 이용해서 분석할 예정.



#### 뉴스 분석 방법

- 사용 모델 : KoBERT

  - [KoBERT Github](https://github.com/SKTBrain/KoBERT)
  - SKTBrain에서 공개한 기계번역 모델.
  - 구글의 기계번역 모델인 BERT를 한국어에도 잘 활용할 수 있도록 만들어진 모델.
  - BERT는 약 33억 개의 단어로 학습한 모델이라 정확성이 매우 높지만, 영어에 대해 높을 뿐 한국어에 대해서는 정확도가 떨어짐.
  - 그래서 그 BERT를 기반으로 하는 대화 엔진을 개발하기 위해 SKTBrain에서 만든게 KoBERT
  - 한국어 데이터에 대해서도 높은 정확도를 나타냄!
  - 사용 이유
    - GPT-3, 네이버 하이퍼 클로바 등의 서비스는 유료라서 기각.
    - 대중적으로 사용하는 KoNLPY(콘엘파이)는 사용하기에는 비교적 간단하지만, KoBERT처럼 미리 학습된 내용이 없기 때문에 정확성이 떨어질 것이라 판단해 KoBERT 사용.

- 분석 방법

  1. 뉴스 데이터 불러옴

  2. 각 뉴스마다 E, S, G, N(기타) 중 어느 분야 관련 기사인지 분류 (다중 분류)

  3. 각 뉴스마다 "텍스트 감성 분석"을 이용해 긍정/부정을 판가름해 점수로 점수로 반영할 예정.

     (각각의 기사가 "얼마나" 긍정/부정인지 정도까지 평가하기에는 제목만으로는 무리가 있어서, 긍정/부정 "이진 분류"만 할 것.)

  - 위 분류에 대한 학습 결과가 없기 때문에, 기사 몇 백개 정도는 우리가 직접 분류해준 뒤, 그걸 train data로 넣어서 추가 학습 시킨 모델을 사용해야 할 듯...



[KoBERT를 이용한 감성 분석 예시](https://tech-diary.tistory.com/31)

[KoBERT로 다중분류 모델 만들기](https://velog.io/@seolini43/KOBERT%EB%A1%9C-%EB%8B%A4%EC%A4%91-%EB%B6%84%EB%A5%98-%EB%AA%A8%EB%8D%B8-%EB%A7%8C%EB%93%A4%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%ACColab)

