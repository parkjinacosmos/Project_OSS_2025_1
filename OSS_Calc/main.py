# main.py

import tkinter as tk
from calculator_module import Calculator # calculator_module.py에서 Calculator 클래스를 임포트

if __name__ == "__main__":
    # Tkinter 윈도우 생성
    root = tk.Tk()
    # Calculator 클래스의 인스턴스를 생성하여 계산기 앱 시작
    calc = Calculator(root)
    # Tkinter 이벤트 루프 시작 (앱을 실행 상태로 유지)
    root.mainloop()