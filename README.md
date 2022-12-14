# Pi
먼저 원주율이란 유클리드 평면에서 ‘원은 크기와 관계없이 항상 닮은 도형이다.’ 라는 전제를 가지고 나타내는 원의 지름에 대한 원의 둘레의 비이다. 원의 지름을 d, 원의 둘레를 C라하면 원주율은 다음과 같이 나타내 진다.
π=  C/d
그리고 우리는 지름이 1인 원의 원주율을 계산하면 3.1415923565…. 라는 순환하지 않는 무한소수가 나온다. 
본 보고서에서는 파이의 근사값을 계산하고자 기존의 길이에 초점을 둔 방식에서 벗어나 몬테카를로 법을 통해 넓이와 확률을 이용한 방법으로 원주율을 계산해 보고자 했다. 이론은 다음과 같다.
	한 변의 길이가 2r인 정사각형을 그리고 그 안쪽에 4변에 접하는 반지름이 r인 원을 그린다.
	원의 넓이는 πr^2이고 정사각형의 넓이는 4r^2이다. 따라서 원의 넓이를 정사각형의 넓이로 나누면 π/4가 된다.
	정사각형 내부에 무작위의 점을 찍고 점이 원 안에 찍혔는지 밖에 찍혔는지 확인한다.
	찍은 점의 수가 많아 질수록 전체 찍힌 점의 수와 원안에 찍힌 점의 수의 비는 정사각형의 넓이와 원의 넓이의 비와 같아지게 된다.
이러한 관계를 수식으로 나타내면 다음과 같다. 
(πr^2)/(4r^2 )=  π/4  ≈  γ/δ
이때 γ는 원에 찍힌 점의 개수, δ는 전체 찍은 점의 개수로 기하학적 확률이다. 이 식을 바탕으로 파이를 계산하는 수식은 다음 과 같다.
π≈  4γ/δ
이를 바탕으로 정확한 결과를 위해 몬테카를로법을 이용한 시뮬레이션을 만들어 파이의 근사 값을 계산한다.

![image](https://user-images.githubusercontent.com/87216860/185031454-305404da-54a5-4dc6-adc6-ef9288fe6a35.png)
위그림은 시뮬레이션 결과를 그래프로 표현한 것이다. 가장 왼쪽 위의 시행횟수10회인 그래프에서 보 듯이 원 안에 들어온 점들을 보기 편하도록 점들을 선으로 이어서 시각화 했다. 그리고 실험한 것들은 자릿수에 따라 모두 그림으로 나타냈으나 100000자리 값부터는 점의 개수가 너무 많아 실제 표현하는 것이 불가능 했다. 
![image](https://user-images.githubusercontent.com/87216860/185031568-dc1cc5ae-261f-46cd-816a-12fa6ca2a4fa.png)
위의 값들은 모두 소수점 6자리이상으로 넘어갈 경우 반올림해서 정리했다.
