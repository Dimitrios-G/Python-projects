import random

# Συνάρτηση για να ελέγξουμε αν το όνομα περιέχει αριθμούς
def contains_numbers(input_string):
    return any(char.isdigit() for char in input_string)

# Συνάρτηση για να πάρουμε τα στοιχεία των παικτών
def get_player_info(players, score, player_chars):
    while True:
        # Ζητάμε το όνομα του Παίκτη 1
        name1 = input("Εισάγετε το όνομα του Παίκτη 1: ").strip()
        if not name1 or contains_numbers(name1):
            print("Άκυρο όνομα.")
            continue
        players.append(name1)
        score[name1] = 0
        break

    while True:
        # Ζητάμε τον χαρακτήρα του Παίκτη 1 (S ή O)
        char1 = input(f"{players[0]}, επιλέξτε γράμμα (S/O): ").strip().upper()
        if char1 in ('S', 'O'):
            player_chars[players[0]] = char1
            break
        else:
            print("Άκυρη επιλογή.")

    # Ο χαρακτήρας του Παίκτη 2 θα είναι το αντίθετο από του Παίκτη 1
    char2 = 'O' if char1 == 'S' else 'S'
    while True:
        # Ζητάμε το όνομα του Παίκτη 2
        name2 = input(f"Εισάγετε το όνομα του Παίκτη 2 ({char2}): ").strip()
        if not name2 or contains_numbers(name2) or name2 == players[0]:
            print("Άκυρο όνομα.")
            continue
        players.append(name2)
        score[name2] = 0
        player_chars[players[1]] = char2
        break

# Συνάρτηση για να εκτυπώσουμε τον πίνακα
def print_board(board):
    rows = len(board)
    cols = len(board[0])

    print("  ", end=" ")
    # Εκτυπώνουμε τους αριθμούς των στηλών
    for c in range(cols):
        print(f" {c:<2}", end=" ")
    print()

    # Εκτυπώνουμε τις γραμμές του πίνακα
    print("   " + "____" * cols)

    for r in range(rows):
        print(f"{r:<2}|", end="")
        for c in range(cols):
            print(f" {board[r][c]} |", end="")  # Εκτυπώνουμε κάθε κελί
        print()
        # Εκτυπώνουμε μια οριζόντια γραμμή μετά από κάθε γραμμή
        print("    " + "____" * cols)

# Συνάρτηση για να ελέγξουμε αν υπάρχει λέξη "SOS"
def check_sos(board, last_row, last_col):
    rows = len(board)
    cols = len(board[0])
    # Ελέγχουμε αν υπάρχει λέξη "SOS" οριζόντια
    for c in range(max(0, last_col - 2), min(cols - 2, last_col)):
        if board[last_row][c] == 'S' and board[last_row][c+1] == 'O' and board[last_row][c+2] == 'S':
            return True
    # Ελέγχουμε αν υπάρχει λέξη "SOS" κάθετα
    for r in range(max(0, last_row - 2), min(rows - 2, last_row)):
        if board[r][last_col] == 'S' and board[r+1][last_col] == 'O' and board[r+2][last_col] == 'S':
            return True
    # Ελέγχουμε αν υπάρχει λέξη "SOS" διαγώνια κάτω δεξιά
    for offset in range(-2, 1):
        r, c = last_row + offset, last_col + offset
        if 0 <= r < rows - 2 and 0 <= c < cols - 2:
            if board[r][c] == 'S' and board[r+1][c+1] == 'O' and board[r+2][c+2] == 'S':
                return True
    # Ελέγχουμε αν υπάρχει λέξη "SOS" διαγώνια κάτω αριστερά
    for offset in range(-2, 1):
        r, c = last_row + offset, last_col - offset
        if 0 <= r < rows - 2 and 2 <= c < cols:
            if board[r][c] == 'S' and board[r+1][c-1] == 'O' and board[r+2][c-2] == 'S':
                return True
    return False

# Συνάρτηση για να ελέγξουμε αν ο πίνακας είναι γεμάτος
def is_full(board):
    # Ελέγχουμε αν ο πίνακας είναι γεμάτος
    for row in board:
        if ' ' in row:
            return False
    return True

# Συνάρτηση για να εμφανίσουμε το κύπελλο για τον νικητή και την καρδιά για τον χαμένο
def display_winner_loser(winner, loser):
    # Εμφάνιση του κυπέλλου για τον νικητή
    print(f"\nΟ ΝΙΚΗΤΗΣ ΕΙΝΑΙ: {winner}")
    print("""
      _______
     /       \\
    |  WINNER |
     \\_______/
    """)
    
    # Εμφάνιση της καρδιάς για τον χαμένο
    print(f"\nΟ ΧΑΜΕΝΟΣ ΕΙΝΑΙ: {loser}")
    print("""
     *****   *
    *     *  *
     ***** * *
           * *
          *  *
          *  *
          *  *
    """)

# Κύρια συνάρτηση για την εκτέλεση του παιχνιδιού
def play_game():
    rows = 10
    cols = 10
    board = [[' ' for _ in range(cols)] for _ in range(rows)]

    # Τοποθετούμε το γράμμα "S" στις 4 γωνίες του πίνακα
    board[0][0] = 'S'
    board[0][cols - 1] = 'S'
    board[rows - 1][0] = 'S'
    board[rows - 1][cols - 1] = 'S'

    # Τοποθετούμε τη λέξη "SOS" στο κέντρο του πίνακα
    board[4][4] = 'S'
    board[4][5] = 'O'
    board[4][6] = 'S'

    score = {}
    players = []
    player_chars = {}
    current_player_index = 0

    # Παίρνουμε τα στοιχεία των παικτών
    get_player_info(players, score, player_chars)

    # Εκτυπώνουμε τον πίνακα πριν την αρχή του παιχνιδιού
    print_board(board)

    while not is_full(board):
        current_player_name = players[current_player_index]
        current_player_char = player_chars[current_player_name]

        # Ο παίκτης εισάγει τις συντεταγμένες για την κίνησή του
        while True:
            try:
                coords_str = input(f"Σειρά του {current_player_name} ({current_player_char}). Εισάγετε γραμμή (0-{rows-1}) και στήλη (0-{cols-1}): ").split()
                if len(coords_str) != 2:
                    print("Άκυρη είσοδος. Παρακαλώ εισάγετε γραμμή και στήλη χωρισμένα με κενό.")
                    continue
                row, col = map(int, coords_str)
                if not (0 <= row < rows and 0 <= col < cols):
                    print(f"Άκυρη είσοδος! Γραμμή μεταξύ 0-{rows-1}, στήλη μεταξύ 0-{cols-1}.")
                    continue
                if board[row][col] != ' ':
                    print("Το κελί είναι κατειλημμένο.")
                    continue

                # Τοποθέτηση του χαρακτήρα στον πίνακα
                board[row][col] = current_player_char

                # Εκτύπωση του πίνακα μετά την τοποθέτηση του χαρακτήρα
                print(f"Πίνακας μετά την κίνηση του {current_player_name}:")
                print_board(board)

                # Έλεγχος για "SOS"
                if check_sos(board, row, col):
                    score[current_player_name] += 1
                    print(f"{current_player_name} κέρδισε 'SOS'! Τρέχον σκορ: {score[current_player_name]}")

                # Εκτύπωση της τρέχουσας κατάστασης
                print(f"Σκορ: {score}")
                break
            except ValueError:
                print("Άκυρη είσοδος. Παρακαλώ εισάγετε έγκυρους αριθμούς.")

        # Αντικατάσταση του παίκτη
        current_player_index = (current_player_index + 1) % 2

    # Κλείσιμο του παιχνιδιού και εμφάνιση του νικητή
    winner = max(score, key=score.get)
    loser = players[0] if players[1] == winner else players[1]
    display_winner_loser(winner, loser)

# Εκτέλεση του παιχνιδιού
play_game()
