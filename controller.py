from AI import AI
from endgame import Ui_self


player = True
p1 = None
p2 = None
p3 = None
p4 = None
p5 = None
p6 = None
p7 = None
p8 = None
p9 = None
row_return = None
column_return = None
diagonal_return = None
p_list = [p1, p2, p3, p4, p5, p6, p7, p8, p9]


class Method():

    def __init__(self, window, colour_player_1, colour_player_2, with_ai, first):
        super().__init__()
        self.window = window
        self.colour_player_1 = colour_player_1
        self.colour_player_2 = colour_player_2
        self.with_ai = with_ai
        self.first = first
        
        if first == True:
            self.update_player(not player)
            for i in p_list:
                if i != None:
                    self.AI_moves(p_list, player)
            self.btn_list(0)
        

    def update_p_list(self, new_p_list):
        global p_list
        p_list = new_p_list

    def update_player(self, new_player):
        global player
        player = new_player

    def btn_list(self, i):
        try:
            button_list = [self.window.pushButton, self.window.pushButton_2, self.window.pushButton_3, self.window.pushButton_4,
                           self.window.pushButton_5, self.window.pushButton_6, self.window.pushButton_7, self.window.pushButton_8, self.window.pushButton_9]
            self.display_change_common(btn=button_list[i], number=i, p_list=p_list, player=player)
            
        except Exception:
            pass
            

    def display_change_common(self, btn, number, p_list, player):
        
        
        if player == True != self.with_ai:

            btn.setStyleSheet(self.colour_player_1)
            btn.setDisabled(True)

            p_list[number] = player
            player = False

            self.update_p_list(p_list)
            self.update_player(player)

            self.row_winner()
            self.column_winner()
            self.diagonal_winner()
            self.tie()

            

        elif player == True == self.with_ai:
            
            
            btn.setStyleSheet(self.colour_player_1)
            btn.setDisabled(True)

            p_list[number] = player
            player = False
            
            self.update_p_list(p_list)
            self.update_player(player)

            self.row_winner()
            self.column_winner()
            self.diagonal_winner()
            self.tie()

            self.AI_moves(p_list, player)
            

        elif player == False == self.with_ai:

            btn.setStyleSheet(self.colour_player_2)
            btn.setDisabled(True)

            p_list[number] = player
            player = True

            self.update_p_list(p_list)
            self.update_player(player)

            self.row_winner()
            self.column_winner()
            self.diagonal_winner()
            self.tie()

            

        elif player == False != self.with_ai:
            btn.setStyleSheet("background-color: rgb(255,255,0);")
            btn.setDisabled(True)
            p_list[number] = player
            player = True
            self.update_p_list(p_list)
            self.update_player(player)

            self.row_winner()
            self.column_winner()
            self.diagonal_winner()
            self.tie()


    
    def AI_moves(self, p_list, player):
        move = AI.AI_plays(p_list, player)
        self.btn_list(move)
        



    def player_name(self):
        global player
        if player == True == self.with_ai:
            player = "COMPUTER"
            

        if player == True != self.with_ai:
            player = self.window.player_2_textbox.text()
            if player == "":
                player = "HUMAN 2"
            

        if player == False == self.with_ai:
            player = self.window.player_1_textbox.text()
            if player == "":
                player = "HUMAN 1"
            

        if player == False != self.with_ai:
            player = "COMPUTER"
            

    def tie(self):
        if False == self.window.pushButton.isEnabled() == self.window.pushButton_2.isEnabled() == self.window.pushButton_3.isEnabled() == self.window.pushButton_4.isEnabled() == self.window.pushButton_5.isEnabled() == self.window.pushButton_6.isEnabled() == self.window.pushButton_7.isEnabled() == self.window.pushButton_8.isEnabled() == self.window.pushButton_9.isEnabled() != (row_return == column_return == diagonal_return):
            self.ui = Ui_self("IT WAS A TIE")
            self.ui.show()

    def row_winner(self):
        global row_return
        if (p_list[0] == p_list[1] == p_list[2] == True) != self.window.pushButton.isEnabled() == self.window.pushButton_2.isEnabled() == self.window.pushButton_3.isEnabled() == False:
            self.player_name()
            self.ui = Ui_self(player + " WON")
            self.ui.show()
            row_return = True
        if p_list[0] == p_list[1] == p_list[2] == False == self.window.pushButton.isEnabled() == self.window.pushButton_2.isEnabled() == self.window.pushButton_3.isEnabled():
            self.player_name()
            self.ui = Ui_self(player + " WON")
            self.ui.show()
            row_return = True
        if (p_list[3] == p_list[4] == p_list[5] == True) != self.window.pushButton_4.isEnabled() == self.window.pushButton_5.isEnabled() == self.window.pushButton_6.isEnabled() == False:
            self.player_name()
            self.ui = Ui_self(player + " WON")
            self.ui.show()
            row_return = True
        if p_list[3] == p_list[4] == p_list[5] == False == self.window.pushButton_4.isEnabled() == self.window.pushButton_5.isEnabled() == self.window.pushButton_6.isEnabled():
            self.player_name()
            self.ui = Ui_self(player + " WON")
            self.ui.show()
            row_return = True
        if (p_list[6] == p_list[7] == p_list[8] == True) != self.window.pushButton_7.isEnabled() == self.window.pushButton_8.isEnabled() == self.window.pushButton_9.isEnabled() == False:
            self.player_name()
            self.ui = Ui_self(player + " WON")
            self.ui.show()
            row_return = True
        if p_list[6] == p_list[7] == p_list[8] == False == self.window.pushButton_7.isEnabled() == self.window.pushButton_8.isEnabled() == self.window.pushButton_9.isEnabled():
            self.player_name()
            self.ui = Ui_self(player + " WON")
            self.ui.show()
            row_return = True

    def column_winner(self):
        global column_return
        if (p_list[2] == p_list[5] == p_list[8] == True) != self.window.pushButton_3.isEnabled() == self.window.pushButton_6.isEnabled() == self.window.pushButton_9.isEnabled() == False:
            self.player_name()
            self.ui = Ui_self(player + " WON")
            self.ui.show()
            column_return = True
        if p_list[2] == p_list[5] == p_list[8] == False == self.window.pushButton_3.isEnabled() == self.window.pushButton_6.isEnabled() == self.window.pushButton_9.isEnabled():
            self.player_name()
            self.ui = Ui_self(player + " WON")
            self.ui.show()
            column_return = True
        if (p_list[1] == p_list[7] == p_list[4] == True) != self.window.pushButton_2.isEnabled() == self.window.pushButton_8.isEnabled() == self.window.pushButton_5.isEnabled() == False:
            self.player_name()
            self.ui = Ui_self(player + " WON")
            self.ui.show()
            column_return = True
        if p_list[1] == p_list[7] == p_list[4] == False == self.window.pushButton_2.isEnabled() == self.window.pushButton_8.isEnabled() == self.window.pushButton_5.isEnabled():
            self.player_name()
            self.ui = Ui_self(player + " WON")
            self.ui.show()
            column_return = True
        if (p_list[0] == p_list[3] == p_list[6] == True) != self.window.pushButton.isEnabled() == self.window.pushButton_4.isEnabled() == self.window.pushButton_7.isEnabled() == False:
            self.player_name()
            self.ui = Ui_self(player + " WON")
            self.ui.show()
            column_return = True
        if p_list[0] == p_list[3] == p_list[6] == False == self.window.pushButton.isEnabled() == self.window.pushButton_4.isEnabled() == self.window.pushButton_7.isEnabled():
            self.player_name()
            self.ui = Ui_self(player + " WON")
            self.ui.show()
            column_return = True


    def diagonal_winner(self):
        global diagonal_return
        if (p_list[2] == p_list[4] == p_list[6] == True) != self.window.pushButton_3.isEnabled() == self.window.pushButton_5.isEnabled() == self.window.pushButton_7.isEnabled() == False:
            self.player_name()
            self.ui = Ui_self(player + " WON")
            self.ui.show()
            diagonal_return = True
        if p_list[2] == p_list[4] == p_list[6] == False == self.window.pushButton_3.isEnabled() == self.window.pushButton_5.isEnabled() == self.window.pushButton_7.isEnabled():
            self.player_name()
            self.ui = Ui_self(player + " WON")
            self.ui.show()
            diagonal_return = True
        if (p_list[0] == p_list[4] == p_list[8] == True) != self.window.pushButton.isEnabled() == self.window.pushButton_5.isEnabled() == self.window.pushButton_9.isEnabled() == False:
            self.player_name()
            self.ui = Ui_self(player + " WON")
            self.ui.show()
            diagonal_return = True
        if p_list[0] == p_list[4] == p_list[8] == False == self.window.pushButton.isEnabled() == self.window.pushButton_5.isEnabled() == self.window.pushButton_9.isEnabled():
            self.player_name()
            self.ui = Ui_self(player + " WON")
            self.ui.show()
            diagonal_return = True



