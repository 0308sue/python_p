class Cat :
    def __init__(self,name,color): #생성자(객체 초기화)
        #객체의 고유 변수들 기술
        self.name = name
        self.color = color

    def meow(self):
        print(f'내 이름은 {self.name}, 색깔은 {self.color}')

nabi = Cat('나비','검정색')
nero = Cat('네로','흰색')
mimi = Cat('미미','갈색')

nabi.meow()
nero.meow()
mimi.meow()