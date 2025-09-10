import sys

import core.init
import pygame
from core.base import central_mg
from core.interrupt import main_interrupt
from core.keyboard.main import main_keyboard
from core.page.main import main_page
from core.screen.main import main_screen

while central_mg.running:
    main_page()

    main_screen()

    # 事件處理，包含鍵盤中斷以及內部設定中斷
    for event in pygame.event.get():
        central_mg.leave_game(event)  # 檢查全局退出
        main_keyboard(event)
        main_interrupt(event)

pygame.quit()
sys.exit()
