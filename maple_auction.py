import pyautogui as pag
import time
import random


conf = 0.8 # 이미지 인식률 따라서 조정 . 컴퓨터마다 실행해보고 조절하면됨
search_delay = 6 # 검색 딜레이 서버 상황에 따라 조정
search_delay2 = 1 # 한 종류의 검색이 끝난 뒤 다음 검색까지의 딜레이

class Item:
    def __init__(self, name, path, price) :
        self.name = name
        self.path = path
        self.price = price
        pass

class MapleAuction:

    def __init__(self) :
        self.item = []
        pass

    # 구매 아이템 항목 추가
    def add_item(self, name, path, price):
        self.item.append(Item(name, path, price))
        pass

    # 텍스트 박스 지우기
    def erase_text(self, box):
        for i in range(5) :
            pag.click(box)
            pag.press(['backspace', 'backspace', 'backspace', 'backspace', 'backspace'])
        pass

    def run(self):

        buy_btn = None

        sobi_item = pag.locateCenterOnScreen('.\\item_image\\sobi_item.PNG', confidence=conf)
        if sobi_item != None :
            pag.click(sobi_item)

        time.sleep(1)
        input_text = pag.locateCenterOnScreen('.\\item_image\\input_item.PNG', confidence=conf)
        search_btn = pag.locateCenterOnScreen('.\\item_image\\search.PNG', confidence=conf)

        if input_text == None or search_btn == None:
            print('input_item or search_btn Error')
            return

        price_text = input_text.x + 55, input_text.y + 30

        item_index = 0

        while True :
            # 아이템 이름 입력
            self.erase_text(input_text + self.random_pos())
            pag.typewrite(self.item[item_index].name)
            time.sleep(0.5)

            # 가격 입력
            self.erase_text(price_text + self.random_pos())
            pag.typewrite(self.item[item_index].price)
            time.sleep(0.5)

            # 검색버튼 클릭 후의 대기 - search_delay
            pag.click(search_btn + self.random_pos())
            time.sleep(0.5)
            pag.press('enter')
            time.sleep(search_delay)
            pag.press('enter')

            # 팔린 아이템 구매 시도때문에 10번만 실행.
            for i in range(10) :
                result = pag.locateCenterOnScreen(self.item[item_index].path, confidence=conf)
                if result == None :
                    break
                pag.click(result + self.random_pos())
                time.sleep(0.5)

                buy_btn = pag.locateCenterOnScreen('.\\item_image\\buy.PNG', confidence=conf)
                
                pag.click(buy_btn + self.random_pos())
                time.sleep(0.5)

                pag.press(['9', '9', '9', '9'])
                time.sleep(0.2)
                pag.press('enter')
                time.sleep(0.5)
                pag.press('enter')
                time.sleep(0.5)

            # 순회 다했으면 처음부터 시작
            item_index += 1
            if item_index == len(self.item) :
                item_index = 0

            # 아이템 하나 검색 후의 대기
            pag.click(100 + random.random() * 700, 50)
            time.sleep(search_delay2)
        pass        

    def random_pos(self):
        return random.random() > 0.5 and (random.random() * 10, random.random() * -2) or (random.random() * -10, random.random() * 2)

            

if __name__ == '__main__':
    ma = MapleAuction()
    # 아이템명 영문 입력
    ma.add_item('tntkdgks zbqm', '.\\item_image\\cube.PNG', '99999')
    ma.add_item('vkdnjdpfflrtj', '.\\item_image\\power.PNG', '2499')
    ma.add_item('ghkdrmaakdcl 100%', '.\\item_image\\hammer.PNG', '20000000')
    ma.run()
    
