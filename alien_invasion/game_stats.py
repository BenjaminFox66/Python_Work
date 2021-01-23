class GameStats:
    '''跟踪游戏的统计信息'''
    def __init__(self, ai_settings):
        '''初始化统计信息'''
        self.ai_settings = ai_settings
        self.reset_stats()
        # 游戏刚启动时，处于活跃状态
        self.game_active = False

        self.score = 0
        self.score_one = 1

        # 在任何情况下都不应重置最高得分
        self.high_score = 0

    def reset_stats(self):
        '''初始化在游戏运行期间可能变化的统计信息'''
        self.score = 0
        self.score_one = 1

