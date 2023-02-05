import math


class AI():
    # Figure out Tie condition because it is mandatory for minimax algo


    def tie(p_list):
        for i in p_list:
            if i == None:
                return 0
        return -1


    def winner(p_list):
        if (p_list[0] == p_list[1] and p_list[1] == p_list[2] and p_list[0] != None):
            return 1
        elif (p_list[3] == p_list[4] and p_list[4] == p_list[5] and p_list[3] != None):
            return 1
        elif (p_list[6] == p_list[7] and p_list[7] == p_list[8] and p_list[6] != None):
            return 1
        elif (p_list[2] == p_list[5] and p_list[5] == p_list[8] and p_list[2] != None):
            return 1
        elif (p_list[1] == p_list[7] and p_list[7] == p_list[4] and p_list[1] != None):
            return 1
        elif (p_list[0] == p_list[3] and p_list[3] == p_list[6] and p_list[0] != None):
            return 1
        elif (p_list[2] == p_list[4] and p_list[4] == p_list[6] and p_list[2] != None):
            return 1
        elif (p_list[0] == p_list[4] and p_list[4] == p_list[8] and p_list[0] != None):
            return 1
        elif (p_list[1] != None and p_list[2] != None and p_list[3] != None and p_list[4] != None and p_list[5] != None and p_list[6] != None and p_list[7] != None and p_list[8] != None and p_list[0] != None):
            return -1
        else:
            return 0


    


    def minimax(board, player):
        Predict_board = board
        Predict_Game = AI.winner(Predict_board)
        
        if Predict_Game == 1:
            if player == False:
                return 1
            else:
                return -1
        elif Predict_Game == -1:
            return 0
        elif Predict_Game == 0:
            if player == True:
                bestScore = -math.inf
                for i in range(0, 9):
                    if Predict_board[i] == None:
                        Predict_board[i] = False
                        score = AI.minimax(Predict_board, False)
                        Predict_board[i] = None
                        bestScore = max(score, bestScore)
                
                return bestScore
            else:
                bestScore = math.inf
                for i in range(0, 9):
                    if Predict_board[i] == None:
                        Predict_board[i] = True
                        score = AI.minimax(Predict_board, True)
                        Predict_board[i] = None
                        bestScore = min(score, bestScore)
                
                return bestScore

    def determine_move(Predict_board, player):
        bestmove = None
        bestscore = -math.inf

        for i in range(0, 9):
            if Predict_board[i] == None:
                Predict_board[i] = False
                score = AI.minimax(Predict_board, not player)
                Predict_board[i] = None
                if score > bestscore:
                    bestscore = score
                    bestmove = i
        return bestmove

    

    

    def AI_plays(p_list, player):
        number = AI.determine_move(p_list, not player)
        
        return number
        
        
