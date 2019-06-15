import random
import subprocess

# Quotes to add:
# Buffy, Firefly, 

possible_chars = ["beavis.zen", "cheese", "cock", "daemon", \
                  "default", "duck", "elephant", "flaming-sheep", \
                  "hellokitty", "koala", "luke-koala", "milk", \
                  "pony-smaller", "ren", "stimpy", "sheep", \
                  "snowman", "tux", "vader-koala"]

def get_char():
    index = random.randint(0, len(possible_chars) - 1)
    return possible_chars[index]

def build_and_run_command():
    character = get_char()

    # We have a special double-case
    # (You can't have ren without stimpy.. etc...)
    if character == "ren" or character == "stimpy":
        fortune_command = ["fortune", "-s"] # Short
        ren_command = ["cowsay", "-f", "ren", "-W 29"]
        stimpy_command = ["cowsay", "-f", "stimpy", "-W 29"]
        
        rens_fortune = subprocess.Popen(fortune_command, stdout=subprocess.PIPE)
        stimpys_fortune = subprocess.Popen(fortune_command, stdout=subprocess.PIPE)

        rens_cowsay = subprocess.Popen(ren_command, stdin=rens_fortune.stdout)
        stimpy_cowsay = subprocess.Popen(stimpy_command, stdin=stimpys_fortune.stdout)

        rens_fortune.stdout.close()
        stimpys_fortune.stdout.close()

        rens_cowsay.communicate()
        stimpy_cowsay.communicate()

    # We have a single case
    else:
        fortune_command = ["fortune"]
        cowsay_command = ["cowsay", "-f", character, "-W 29"]
        
        fortune = subprocess.Popen(fortune_command, stdout=subprocess.PIPE)
        cowsay = subprocess.Popen(cowsay_command, stdin=fortune.stdout)

        fortune.stdout.close()

        cowsay.communicate()

build_and_run_command()
print("\n")
print("\n")
print("\n")
