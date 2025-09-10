import pprint
import time

import pygame
from core.debug import dbg


#
# 遊戲狀態總管理
#
class CentralManager:
    def __init__(self):
        self.running = True
        self.debug_mode = True

    # 全局退出遊戲
    def leave_game(self, event):
        if event.type == pygame.QUIT:
            self.running = False

central_mg = CentralManager()



#
# timer
#
class ClockTimer:
    def __init__(self):
        self.start_time = None
        self.paused_time = 0
        self.running = False

    def start(self):
        """開始計時"""
        if not self.running:
            self.start_time = time.time() - self.paused_time
            self.running = True

    def pause(self):
        """暫停計時"""
        if self.running:
            self.paused_time = time.time() - self.start_time
            self.running = False

    def reset(self):
        """重置計時"""
        self.start_time = 0
        self.paused_time = 0
        self.running = False

    def get_min_sec(self):
        """
        取得目前分/秒數字
        返回 tuple: (minutes, seconds)
        秒數 0~59 循環(小數第二位)
        """
        total_sec = self._get_elapsed()
        minutes = int(total_sec // 60)
        seconds = round(total_sec % 60, 2)
        return minutes, seconds

    def _get_elapsed(self):
        """回傳總經過秒數（浮點）"""
        if self.running:
            return time.time() - self.start_time
        else:
            return self.paused_time



#
# Stack
#
class Stack:
    def __init__(self, start_table, genealogy_table):
        self.current            = start_table
        self.store              = [start_table]
        self.genealogy_table    = genealogy_table # genealogy_table: {PageTable: {index: child_page}}

    def visit(self, current_table, next_table):
        # 先判斷是否同屬一個父頁面
        if current_table == self.current:
            children = self.genealogy_table.get(current_table, {}).values()

            if next_table in children:
                self.store.append(next_table)  # 存入 stack

        # 更新當前頁面
        self.current = next_table

    def back(self, current_table):
        if len(self.store) > 1:
            self.store.pop()
            self.current = self.store[-1]
            return self.current
        else:
            dbg.log('The stack has no previous page and is already root')
            return current_table

    def show_stack(self):
        pprint.pprint(self.store)
        dbg.log(f'目前 stack: {self.store}')
