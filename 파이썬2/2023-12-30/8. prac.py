class Watch():
    def What(self):
        time = input('시간을 입력하세요>>')
        time_list = time.split(':')
        self.hour = int(time_list[0])
        self.min = int(time_list[1])
        self.sec = int(time_list[2])
        # 계속 사용할 변수들 앞에 self를 쓰는듯??? 

    def see(self):
        print(f'계산된 시간은 {self.hour}시 {self.min}분 {self.sec}초 입니다.')

watch = Watch()
watch.What()
watch.see()