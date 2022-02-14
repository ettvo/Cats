"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns True. If there are fewer than K such paragraphs, return
    the empty string.

    Arguments:
        paragraphs: a list of strings
        select: a function that returns True for paragraphs that can be selected
        k: an integer

    >>> ps = ['hi', 'how are you', 'fine']
    >>> s = lambda p: len(p) <= 4
    >>> choose(ps, s, 0)
    'hi'
    >>> choose(ps, s, 1)
    'fine'
    >>> choose(ps, s, 2)
    ''
    """
    # BEGIN PROBLEM 1 

    #valid_paragraph = []
    #for paragraph in paragraphs:
    #    if select(paragraph):
    #        valid_paragraph.append(paragraph)
    #return valid_paragraph[k]
    
    #if k == 1:
    #    print(paragraphs)
    valid = []

    if len(paragraphs) < k:
        return ""
    
    for x in paragraphs:
        if select(x):
            valid.append(x)
    
    #if select(paragraphs[k]):
    #    x = paragraphs[k]
        #paragraphs.pop(k)
    #    paragraphs.append(x)
    #    return x
    #else:
        #paragraphs.pop(k)

    if len(valid) <= k:
        return ""
    else:
        return valid[k]


    

    # strings are taken out if they are or don't pass
    # END PROBLEM 1

# paragraph = LIST of strings
def about(topic):
    """Return a select function that returns whether
    a paragraph contains one of the words in TOPIC.

    Arguments:
        topic: a list of words related to a subject

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    
    #def check_paragraph(paragraphs):
    #    for x in topic:
    #        for line in paragraphs:
    #            if x in line:
    #                return True
    #return False

    def check_paragraph(paragraphs):
        #letters_only = []
        #for character in paragraphs:
        #    if character.isalpha():
        #        letters_only.append(character)
        #words = str(letters_only).split(" ")

        # need to remove punctuation
        
        # isalpha() or is whitespace


        """points for using previous code?"""

        words_only = ""
        for letter in paragraphs:
            no_punct = ""
            if letter.isalnum() or letter.isspace():
                    no_punct = no_punct + letter
            words_only = words_only + no_punct     

        words_only = words_only.split(" ")
        for word in words_only:
            for x in topic:
                if x.lower() == word.lower(): # need to ignore case
                    return True
        return False
    return check_paragraph

    # END PROBLEM 2
    # pay attention to spacing
    # paragraphs.split


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    Arguments:
        typed: a string that may contain typos
        reference: a string without errors

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    >>> accuracy('', '')
    100.0
    """
    
    typed_words = ""

    for letter in typed:
        if letter.isascii() and letter != '\t':
            typed_words += letter

    #if typed == " a b \tc":
    #    print(typed_words)
    typed_words = typed_words.split(" ")
    reference_words = reference.split(" ")

    accurate_words = 0

    for word in typed_words:
        if not word:
            typed_words.remove(word)
    
    for word in reference_words:
        if not word:
            reference_words.remove(word)
            

    # when processing strings, escape characters are processed as one character

    if not typed and not reference:
        return float(100)
    elif not typed and reference:
        return float(0)
    elif typed and not reference:
        return float(0)
    else:
        #if len(typed_words) > len(reference_words):
        #    print("")
       # if len(typed_words) < len(reference_words):
            #
       # else:
        if len(typed_words) > len(reference_words):
            for i in range(len(reference_words)):
                if typed_words[i] == reference_words[i]:
                    accurate_words = accurate_words + 1
        else:
            for i in range(len(typed_words)):
                if typed_words[i] == reference_words[i]:
                    accurate_words = accurate_words + 1
        #if typed == "a  b  c  d":
        #    print(accurate_words)
        #    print(len(typed_words))
        return 100*accurate_words/len(typed_words)
    # account for escape characters
    
    
    # how many decimal places
    # if typed > reference (length) --> check accuracy based on typed? TRUE


    # BEGIN PROBLEM 3
    
    

    # pay attention to escape characters ('\n' '\t')
    # both empty = return 100.0
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string.

    Arguments:
        typed: an entered string
        elapsed: an amount of time in seconds

    >>> wpm('hello friend hello buddy hello', 15)
    24.0
    >>> wpm('0123456789',60)
    2.0
    """
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    if not typed:
        return float(0)
    else:
        return (len(typed)/5)/(elapsed/60)    
    # END PROBLEM 4


###########
# Phase 2 #
###########

def autocorrect(typed_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from TYPED_WORD. Instead returns TYPED_WORD if that difference is greater
    than LIMIT.

    Arguments:
        typed_word: a string representing a word that may contain typos
        valid_words: a list of strings representing valid words
        diff_function: a function quantifying the difference between two words
        limit: a number

    >>> ten_diff = lambda w1, w2, limit: 10 # Always returns 10
    >>> autocorrect("hwllo", ["butter", "hello", "potato"], ten_diff, 20)
    'butter'
    >>> first_diff = lambda w1, w2, limit: (1 if w1[0] != w2[0] else 0) # Checks for matching first char
    >>> autocorrect("tosting", ["testing", "asking", "fasting"], first_diff, 10)
    'testing'
    """
    # BEGIN PROBLEM 5
    if typed_word in valid_words:
        return typed_word
    else:
        smallest_diff = diff_function(typed_word, valid_words[0], limit)
        index = 0

        for i in range(len(valid_words) - 1):
            diff = diff_function(typed_word, valid_words[i + 1], limit)
            if smallest_diff > diff:
                smallest_diff = diff
                index = i + 1
        
        if smallest_diff > limit:
            return typed_word
        else:
            return valid_words[index]

        #can do min/max by using a recursive call on the second term to keep
        #going down in the count
        #used iteration instead of recursion
            

    # END PROBLEM 5


def sphinx_switches(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths and returns the result.

    Arguments:
        start: a starting word
        goal: a string representing a desired goal word
        limit: a number representing an upper bound on the number of chars that must change

    >>> big_limit = 10
    >>> sphinx_switches("nice", "rice", big_limit)    # Substitute: n -> r
    1
    >>> sphinx_switches("range", "rungs", big_limit)  # Substitute: a -> u, e -> s
    2
    >>> sphinx_switches("pill", "pillage", big_limit) # Don't substitute anything, length difference of 3.
    3
    >>> sphinx_switches("roses", "arose", big_limit)  # Substitute: r -> a, o -> r, s -> o, e -> s, s -> e
    5
    >>> sphinx_switches("rose", "hello", big_limit)   # Substitute: r->h, o->e, s->l, e->l, length difference of 1.
    5
    """
    # BEGIN PROBLEM 6
    #assert False, 'Remove this line'
    
    # use recursion

    # check for length first; then do [: len(start)]
    
    if len(start) != len(goal):
        letters_wrong = abs(len(goal) - len(start))
        if len(start) > len(goal):
            start = start[:len(goal)]
        else:
            goal = goal[:len(start)]
    else:
        letters_wrong = 0

    def check_letter(typed, reference, letters):
        if not typed or letters > limit:
            return letters
        elif typed[0] != reference[0]:
            return check_letter(typed[1:], reference[1:], 1 + letters)
        else:
            return check_letter(typed[1:], reference[1:], letters)

    return check_letter(start, goal, letters_wrong)

    # END PROBLEM 6


def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL.
    This function takes in a string START, a string GOAL, and a number LIMIT.

    Arguments:
        start: a starting word
        goal: a goal word
        limit: a number representing an upper bound on the number of edits

    >>> big_limit = 10
    >>> pawssible_patches("cats", "scat", big_limit)       # cats -> scats -> scat
    2
    >>> pawssible_patches("purng", "purring", big_limit)   # purng -> purrng -> purring
    2
    >>> pawssible_patches("ckiteus", "kittens", big_limit) # ckiteus -> kiteus -> kitteus -> kittens
    3
    """
    #assert False, 'Remove this line'
    test_case = start == "place" and goal == "wreat"

    if start == goal:
        return 0

    elif not limit:
        return 1

    elif not start or not goal:
        return abs(len(start) - len(goal)) - 1
        # assumes different lengths / not same length and all incorrect until "" ""
        # trouble
        # "" vs. "len" --> 2 instead of 3

    else:
        i = 0
        while i < len(start) - 1 and i < len(goal) - 1 and start[i] == goal[i]:
            i += 1

        add = 1 + pawssible_patches(start[i:], goal[i + 1:], limit - 1)

        remove = 1 + pawssible_patches(start[i + 1:], goal[i:], limit - 1)
        
        #print("substitute: \nstart:", start, "\nstart[i + 1:]:", start[i + 1:], "\ngoal[i + 1:]:", goal[i + 1:])
        substitute = 1 + pawssible_patches(start[i + 1:], goal[i + 1:], limit - 1)
        

        if test_case:
            print("Add:", add)
            print("Remove:", remove)
            print("Substitute:", substitute)

        return min(add, remove, substitute)

        # [:i] = not inclusive i



def final_diff(start, goal, limit):
    """A diff function that takes in a string START, a string GOAL, and a number LIMIT.
    If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function.'


FINAL_DIFF_LIMIT = 6  # REPLACE THIS WITH YOUR LIMIT


###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server.
    Returns the progress so far.

    Arguments:
        typed: a list of the words typed so far
        prompt: a list of the words in the typing prompt
        user_id: a number representing the id of the current user
        send: a function used to send progress to the multiplayer server

    >>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
    >>> # The above function displays progress in the format ID: __, Progress: __
    >>> print_progress({'id': 1, 'progress': 0.6})
    ID: 1 Progress: 0.6
    >>> typed = ['how', 'are', 'you']
    >>> prompt = ['how', 'are', 'you', 'doing', 'today']
    >>> report_progress(typed, prompt, 2, print_progress)
    ID: 2 Progress: 0.6
    0.6
    >>> report_progress(['how', 'aree'], prompt, 3, print_progress)
    ID: 3 Progress: 0.2
    0.2
    """
    # BEGIN PROBLEM 8
    
    """# list of functions:
    accuracy(typed, reference) // returns % accurate
    wpm(typed, elapsed) //time in seconds
    autocorrect(typed_word, valid_words, diff_function, limit)
    """

    num_correct, only_correct = 0, True # multiple assignment for composition points

    # for or while
    """for i in range(len(typed)):
        if typed[i] == prompt[i]:
            num_correct += 1
        else:
            i = range(len(typed)) + 1"""

    #i = 
    # iterable starts at i = 0 < len(typed)

    while only_correct and num_correct != len(typed):
        if typed[num_correct] == prompt[num_correct]: # stops iterating at last typed[i]
            num_correct += 1
        else:
            only_correct = False
    # remember to call send function
    progress = {'id': user_id, 'progress': num_correct/len(prompt)}

    send(progress)

    return progress['progress']

    # return dictionary
    # ID: 1 Progress: 0.6
    # 0.6
    # result is Float
    # stops at first instance of bad letter
    

    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.

    >>> p = [[75, 81, 84, 90, 92], [19, 29, 35, 36, 38]]
    >>> game = time_per_word(p, ['collar', 'plush', 'blush', 'repute'])
    >>> all_words(game)
    ['collar', 'plush', 'blush', 'repute']
    >>> all_times(game)
    [[6, 3, 6, 2], [10, 6, 1, 2]]
    """
    # BEGIN PROBLEM 9
    # game(words, times)
    # returns game(list(words), list(times)) with time[i][j] = element ith player with jth time
    # --> time stamps = calculate time differences between each array element

    times = []

    for player in times_per_player: # gives array specific to player
        player_time = []
        for time in range(1, len(player)): # gives time specific to player, 
            player_time.append(player[time] - player[time - 1])
        times.append(player_time)
    
    return game(words, times)


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.

    >>> p0 = [5, 1, 3]
    >>> p1 = [4, 1, 6]
    >>> fastest_words(game(['Just', 'have', 'fun'], [p0, p1]))
    [['have', 'fun'], ['Just']]
    """
    # game(words, times)
    # returns nested list (w/ each player), each nested list element = the ones that they won that are faster than everyone else
    # if same time, use ealrier player
    # The game argument is a game data abstraction, like the one returned in Problem 9. You can access words in the game with selectors word_at, which takes in a game and the word_index (an integer). You can access the time it took any player to type any word using time.
    # pure comparison because the valuesn are already calculated
    player_indices = range(len(all_times(game)))  # contains an *index* for each player
    word_indices = range(len(all_words(game)))    # contains an *index* for each word
    
    best_words = [[] for player in player_indices]
    # all_words(game)
    # all_times(game)
    # all_words(game)[0]


    # create list w/ linked list w/ index of best player

    for word in word_indices: # int
        lowest_time_player = 0
        for player in player_indices: # int
            if all_times(game)[player][word] < all_times(game)[lowest_time_player][word]:
                lowest_time_player = player
        best_words[lowest_time_player].append(all_words(game)[word])

    return best_words

    # def word_at(game, word_index)
    # return game[0][word_index]

    # def time(game, player_num, word_index):
    # return game[1][player_num][word_index]


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])


enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)
