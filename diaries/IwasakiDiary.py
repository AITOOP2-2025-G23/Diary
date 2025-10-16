from diaries.AbstractDiary import AbstractDiary

class IwasakiDiary(AbstractDiary):

    def get_date(self):
        return "2025-10-16"
    
    def get_summary(self):
        return "今日はオブジェクト指向プログラミング演習2のグループワーク演習だった。Branchを利用した作業を学んだ。"
    
    def get_author(self):
        return "Iwasaki"