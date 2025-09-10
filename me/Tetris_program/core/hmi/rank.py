from core.font.json_manager import json_mg
from core.hmi.list import BaseManager
from core.variable import PageTable, PathConfig


class RankManager(BaseManager):
    def __init__(self):
        # 預設一個排行榜狀態
        super().__init__({PageTable.RANK.value: []})
        self.page_table = PageTable.RANK
        self.load_rank()

    def load_rank(self):
        """讀取 JSON 中的排行榜"""
        self.state[PageTable.RANK.value] = json_mg.get_json_list("dict", PageTable.RANK.value)

    def add_score(self, min: int, sec: int, score: int):
        """加入新分數並更新排行榜"""
        new_entry = [min, sec, score]
        self.state[PageTable.RANK.value].append(new_entry)

        # 排序（依分數高低）
        self.state[PageTable.RANK.value].sort(key = lambda x: x[2], reverse = True)

        # 只保留前 3 名
        self.state[PageTable.RANK.value] = self.state[PageTable.RANK.value][:3]

        # 存回 JSON
        self._update_json_value(PageTable.RANK.value, PageTable.RANK.value, self.state[PageTable.RANK.value])
        json_mg.write_json(PathConfig.json_save, json_mg.word_dict_data, only_keys=[PageTable.RANK.value])

    def get_rank(self):
        """取得排行榜資料"""
        return self.state[PageTable.RANK.value]

rank_mg = RankManager()
