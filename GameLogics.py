import MyRandom as rnd
import static

class Level(object):
    def __init__(self, score):
        self.matrix = list()
        self.select_blocks = []
        self.select_col = 0
        self.width = 10
        self.height = 16
        self.score = score


    def create_level(self):
        is_not_empty_blocks = 5
        self.matrix.clear()
        for i1 in range(is_not_empty_blocks):
            row1 = []
            for j1 in range(self.width):
                row1.append(rnd.random_block())
            self.matrix.append(row1)
        for i2 in range(self.height - is_not_empty_blocks):
            row2 = []
            for j2 in range(self.width):
                row2.append(0)
            self.matrix.append(row2)


    def _shift(self, lst, steps):
        if steps < 0:
            steps = abs(steps)
            for i in range(steps):
                lst.append(lst.pop(0))
        else:
            for i in range(steps):
                lst.insert(0, lst.pop())


    def add_row(self):
        col_matrix = []
        for j in range(len(self.matrix[0])):
            col = []
            for i in range(len(self.matrix)):
                col.append(self.matrix[i][j])
            if col[-1] == 0:
                self._shift(col, 1)
                col[0] = rnd.random_block()
                col_matrix.append(col)

        for b in range(len(self.matrix[0])):
            for a in range(len(self.matrix)):
                self.matrix[a][b] = col_matrix[b][a]


    def take_blocks(self):
        if len(self.select_blocks) == 0:
            for row in range(len(self.matrix) - 1, -1, -1):
                if self.matrix[row][self.select_col] == 0:
                    continue
                else:
                    if self.matrix[row][self.select_col] != -1:
                        self.select_blocks.append(self.matrix[row][self.select_col])
                        self.matrix[row][self.select_col] = 0
                        if self.matrix[row - 1][self.select_col] == self.select_blocks[0]:
                            continue
                        else:
                            break
                    else:
                        break


    def _give_blocks(self):
        if len(self.select_blocks) > 0:
            for row in range(len(self.matrix)):
                if self.matrix[row][self.select_col] == 0:
                    for a in range(len(self.select_blocks)):
                        self.matrix[row + a][self.select_col] = self.select_blocks[a]
                    break
            self.select_blocks.clear()


    def _check_dinamit(self):
        for row in range(len(self.matrix) - 1, -1, -1):
            if self.matrix[row][self.select_col] == 0:
                continue
            else:
                if self.matrix[row][self.select_col] == -2:
                    for r in range(len(self.matrix)):
                        if self.matrix[r][self.select_col] != 0:
                            self.matrix[r][self.select_col] = 0
                            self.score += 100
                    return True
                else:
                    return False


    def _delete_4_more_same_blocks(self, boolmatrix):
        indexes = []
        count = 0
        for i in range(len(boolmatrix)):
            for j in range(len(boolmatrix[i])):
                if boolmatrix[i][j] == True:
                    indexes.append((i, j))
                    count += 1
        if count > 3:
            self.score += count*100
            for a in indexes:
                self.matrix[a[0]][a[1]] = 0


    def _check_empty_block_in_middle(self, column):
        indexes = []
        for row_plus in range(len(self.matrix)):
            if self.matrix[row_plus][column] == 0:
                indexes.append(row_plus)
                break
        for row_minus in range(len(self.matrix) - 1, -1, -1):
            if self.matrix[row_minus][column] != 0:
                indexes.append(row_minus + 1)
                break
        if len(indexes) == 2:
            if indexes[0] == indexes[1]:
                return (False, indexes[0], indexes[1])
            else:
                return (True, indexes[0], indexes[1])
        return (False, 0, 0)


    def _shift_empty_blocks(self, column, i1, i2):
        for row in range(i1, i2 + 2):
            if i2 < len(self.matrix):
                a = self.matrix[row + 1][column]
                self.matrix[row + 1][column] = self.matrix[row][column]
                self.matrix[row][column] = a


    def _check_empty_block_in_middle_in_all_columns(self):
        for col in range(len(self.matrix[0])):
            flag = self._check_empty_block_in_middle(col)
            if flag[0]:
                self._shift_empty_blocks(col, flag[1], flag[2])
                while self._check_empty_block_in_middle(col)[0]:
                    self._shift_empty_blocks(col, flag[1], flag[2])


    def _search_row_index(self):
        for row in range(len(self.matrix) - 1, -1, -1):
            if self.matrix[row][self.select_col] == 0:
                continue
            else:
                return row
        return -1


    def update(self):
        self._give_blocks()
        bool = self._check_dinamit()
        if bool == False:
            boolmatrix = static.create_false_boolmatrix(self.height, self.width)
            i = self._search_row_index()
            if i >= 0:
                boolmatrix = static.try_search_neighbor(self.matrix, boolmatrix, i, self.select_col)
                self._delete_4_more_same_blocks(boolmatrix)
                self._check_empty_block_in_middle_in_all_columns()


    def move_select_column(self, side):
        map = {
            'left': self.select_col - 1,
            'right': self.select_col + 1
        }
        if side == 'left':
            if self.select_col > 0:
                self.select_col = map[side]
            else:
                self.select_col = len(self.matrix[0]) - 1
        if side == 'right':
            if self.select_col < len(self.matrix[0]) - 1:
                self.select_col = map[side]
            else:
                self.select_col = 0


    def check_game_over(self):
        for i in range(len(self.matrix[0])):
            if self.matrix[-1][i] != 0:
                return True
        return False


    def __getitem__(self, key):
        return self.matrix[key[0]][key[1]]


    def get_select_blocks(self):
        color = 0
        count = 0
        if len(self.select_blocks) != 0:
            color = self.select_blocks[0]
            count = len(self.select_blocks)
        return {
            'color': color,
            'count': count
        }


    def get_select_col(self):
        return self.select_col


    def get_score(self):
        return self.score
