"""
Solar System Quiz & Space Knowledge App
Author: Physicist Durodola Daniel 
"""

import random
import textwrap
import sys

"""
----------------------------
 QUESTION BANK (sample set)
----------------------------
"""
# Each question is a dict with: question, options (list of 4), answer (the correct option text)

QUESTION_BANK = [
    {
        "question": "What is the color of the Sun (as perceived from space)?",
        "options": ["Yellow", "Red", "White", "Orange"],
        "answer": "White"
    },
    {
        "question": "How many planets are in the Solar System (officially)?",
        "options": ["7", "8", "9", "10"],
        "answer": "8"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Mars", "Jupiter", "Mercury"],
        "answer": "Mars"
    },
    {
        "question": "Which planet has the most prominent ring system?",
        "options": ["Saturn", "Uranus", "Jupiter", "Neptune"],
        "answer": "Saturn"
    },
    {
        "question": "Which planet is the largest by mass?",
        "options": ["Jupiter", "Saturn", "Earth", "Neptune"],
        "answer": "Jupiter"
    },
    {
        "question": "What type of object is Pluto classified as now?",
        "options": ["Planet", "Dwarf planet", "Comet", "Asteroid"],
        "answer": "Dwarf planet"
    },
    {
        "question": "Which planet is closest to the Sun?",
        "options": ["Mercury", "Venus", "Earth", "Mars"],
        "answer": "Mercury"
    },
    {
        "question": "Which object is primarily composed of ice and dust and has a glowing coma when near the Sun?",
        "options": ["Asteroid", "Comet", "Meteor", "Dwarf planet"],
        "answer": "Comet"
    },
    {
        "question": "What is the name of Earth's natural satellite?",
        "options": ["Luna", "Phobos", "Titan", "Moon"],
        "answer": "Moon"
    },
    {
        "question": "Which planet has the Great Red Spot?",
        "options": ["Saturn", "Jupiter", "Uranus", "Neptune"],
        "answer": "Jupiter"
    },
    {
        "question": "What is a light-year?",
        "options": ["Time unit", "Distance light travels in a year", "Brightness of a year", "Speed of light in a year"],
        "answer": "Distance light travels in a year"
    },
    {
        "question": "What is the Milky Way?",
        "options": ["A galaxy", "A star", "A planet", "A nebula"],
        "answer": "A galaxy"
    },
    {
        "question": "What causes day and night on Earth?",
        "options": ["Earth orbiting the Sun", "Tilt of Earth's axis", "Earth rotating on its axis", "Moon's gravity"],
        "answer": "Earth rotating on its axis"
    },
    {
        "question": "What is a supernova?",
        "options": ["Birth of a star", "Death explosion of a massive star", "A black hole", "A comet impact"],
        "answer": "Death explosion of a massive star"
    },
    {
        "question": "Which spacecraft famously carried humans to the Moon in 1969?",
        "options": ["Voyager 1", "Apollo 11", "Sputnik", "SpaceX's Falcon1"],
        "answer": "Apollo 11"
    },
    {
        "question": "Which planet spins on its side, giving it an extreme tilt?",
        "options": ["Mars", "Uranus", "Neptune", "Saturn"],
        "answer": "Uranus"
    },
    {
        "question": "Which planet is famous for its dense, greenhouse-effect atmosphere, making it the hottest planet?",
        "options": ["Earth", "Mars", "Venus", "Mercury"],
        "answer": "Venus"
    },
    {
        "question": "What is the name of the galaxy that contains our Solar System?",
        "options": ["Andromeda", "Milky Way", "Triangulum", "Sombrero"],
        "answer": "Milky Way"
    },
    {
        "question": "Which of these is mainly composed of rock and metal and orbits the Sun between Mars and Jupiter?",
        "options": ["Comets", "Asteroids", "Kuiper belt objects", "Moons"],
        "answer": "Asteroids"
    },
    {
        "question": "What is a black hole?",
        "options": ["A very bright star", "A region with strong gravity where light cannot escape", "A comet", "A type of planet"],
        "answer": "A region with strong gravity where light cannot escape"
    },
]

# ----------------------------
# ASK-THE-UNIVERSE ANSWERS (predefined)
# Keys should be lowercased simple phrases; I will match user questions against these keys.
# ----------------------------

UNIVERSE_QA = {
    "what is the solar system": "The Solar System is a collection of the Sun and the objects gravitationally bound to it, including planets, moons, asteroids, and comets.",
    "how old is the solar system": "The Solar System is about 4.6 billion years old.",
    "how many planets are in the solar system": "There are 8 officially recognized planets in the Solar System: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune.",
    "what is the sun": "The Sun is a star at the center of our Solar System, made mostly of hydrogen and helium and powered by nuclear fusion.",
    "is the sun a star": "Yes. The Sun is a G-type main-sequence star (a 'yellow dwarf').",
    "why is pluto not a planet": "Pluto is classified as a dwarf planet because it does not clear its orbital neighborhood of other debris, a rule from the IAU definition.",
    "what is a comet": "A comet is a small body of ice and dust that develops a glowing coma and sometimes a tail when it approaches the Sun.",
    "what is an asteroid": "An asteroid is a rocky object that orbits the Sun, mostly found in the asteroid belt between Mars and Jupiter.",
    "what is a light year": "A light-year is the distance light travels in one year—about 9.46 trillion kilometers (5.88 trillion miles).",
    "how many moons does earth have": "Earth has one natural moon, often called the Moon.",
    "who was the first man on the moon": "Neil Armstrong was the first person to walk on the Moon, on July 20, 1969, during Apollo 11.",
    "what is a black hole": "A black hole is an object with gravity so strong that nothing, not even light, can escape from it beyond its event horizon.",
    "what is dark matter": "Dark matter is a form of matter that does not emit light and is detected by its gravitational effects; it makes up most of the mass in galaxies, but its nature is unknown.",
    "what is dark energy": "Dark energy is a mysterious form of energy that is causing the expansion of the universe to accelerate.",
    "what is the milky way": "The Milky Way is the galaxy that contains our Solar System; it is a barred spiral galaxy.",
    "is there life on mars": "No confirmed life has been found on Mars yet. Scientists are actively searching for evidence of past or present microbial life.",
    "what causes day and night": "Day and night are caused by Earth's rotation on its axis—one side faces the Sun (day) while the other faces away (night).",
    "what is a supernova": "A supernova is a powerful explosion that happens when a massive star runs out of fuel and collapses or when a white dwarf acquires enough mass to explode.",
    "what are saturn rings made of": "Saturn's rings are made mostly of ice particles mixed with rock and dust.",
    "what is europa": "Europa is one of Jupiter's moons; it likely has a subsurface ocean under an icy crust and is of interest for the search for life.",
    "what is the iss": "The ISS (International Space Station) is a habitable artificial satellite where astronauts live and conduct experiments in low Earth orbit.",
    "what is a galaxy": "A galaxy is a huge system of stars, gas, dust, and dark matter bound together by gravity.",
    "what is a neutron star": "A neutron star is the dense remnant left behind after a massive star explodes in a supernova; it is made mostly of neutrons.",
    "what color is mars": "Mars appears red because its surface is rich in iron oxide (rust).",
    "what is the great red spot": "The Great Red Spot is a giant storm on Jupiter that has existed for at least hundreds of years.",
    "what is the temperature of the sun": "The Sun's surface temperature is about 5,500°C (around 5,800 K); its core is much hotter (millions of degrees).",
    "how many galaxies exist": "There are an estimated hundreds of billions of galaxies in the observable universe.",
    "what is a wormhole": "A wormhole is a hypothetical tunnel-like structure in spacetime that could connect distant regions; it remains theoretical.",
    "what is the james webb telescope": "The James Webb Space Telescope is a large infrared space telescope launched to study the early universe, star and planet formation, and more.",
    "what is the hubble telescope": "The Hubble Space Telescope is an optical and ultraviolet space telescope that has provided deep views of the universe since 1990.",
    "what is orion": "Orion is a prominent constellation containing bright stars like Betelgeuse and Rigel; it is easily seen from both hemispheres in certain seasons.",
    "what is a light year in kilometers": "One light-year is about 9.46 trillion kilometers (9.46 x 10^12 km).",
    "what is venus": "Venus is the second planet from the Sun, with a thick, hot atmosphere and surface temperatures hot enough to melt lead.",
}

# I added a few synonyms mapping to the same answers (helps matching)
SYNONYMS = {
    "how many planets": "how many planets are in the solar system",
    "is pluto a planet": "why is pluto not a planet",
    "is pluto a comet": "why is pluto not a planet",
    "what is the sun made of": "what is the sun",
    "how old is the universe": "how old is the solar system"
}

"""
----------------------------
 Utility functions
----------------------------
"""
def wrap(text, width=78):
    return "\n".join(textwrap.wrap(text, width=width))


def clear_screen():
    import os
    os.system('cls' if sys.platform.startswith('win') else 'clear')


def normalize_text(s: str) -> str:
    import re
    s = s.lower().strip()
    s = re.sub(r'[^a-z0-9\s]', '', s)  # keep letters, numbers, spaces
    s = " ".join(s.split())
    return s


"""
----------------------------
 Quiz mechanics
----------------------------
"""
def ask_question(q_dict, q_num=None):
    """
    Ask one question dictionary and return True if answer is correct.
    q_dict: {question, options, answer}
    """
    if q_num is not None:
        print(f"\nQuestion {q_num}:")
    else:
        print("\nQuestion:")

    print(wrap(q_dict["question"]))
    opts = q_dict["options"][:]
    paired = list(enumerate(opts))
    random.shuffle(paired)
    shuffled_options = [opt for idx, opt in paired]

    # Map letters A-D to options
    letters = ['A', 'B', 'C', 'D']
    option_map = {}
    for i, opt in enumerate(shuffled_options):
        letter = letters[i]
        option_map[letter] = opt
        print(f"  {letter}) {opt}")

# To find which letter is the correct one
    correct_letter = None
    for letter, opt in option_map.items():
        if opt.lower() == q_dict["answer"].lower():
            correct_letter = letter
            break

    # To get user input
    while True:
        ans = input("Your answer (A/B/C/D or type 'skip'): ").strip().upper()
        if ans == 'SKIP':
            print(f"Skipped. Correct answer: {q_dict['answer']}")
            return False, 'skipped'
        if ans in option_map:
            chosen = option_map[ans]
            if chosen.lower() == q_dict["answer"].lower():
                print("Correct!")
                return True, 'correct'
            else:
                print(f"Wrong. Correct answer: {q_dict['answer']}")
                return False, 'wrong'
        else:
            print("Please enter A, B, C, D or 'skip'.")


def run_quiz(level='beginner', num_questions=10):
    """
    Run quiz session.
    level: 'beginner'|'intermediate'|'advanced' - for now i used same bank, but i can filter later.
    num_questions: how many questions to ask (max limited by bank size)
    """
    clear_screen()
    print("Starting the quiz. Good luck!\n")
    available = QUESTION_BANK[:]
    max_q = min(len(available), num_questions)
    questions = random.sample(available, max_q)

    score = 0
    stats = {'correct': 0, 'wrong': 0, 'skipped': 0}
    for i, q in enumerate(questions, start=1):
        correct, status = ask_question(q, q_num=i)
        if status == 'correct':
            score += 1
            stats['correct'] += 1
        elif status == 'wrong':
            stats['wrong'] += 1
        elif status == 'skipped':
            stats['skipped'] += 1

    percent = (score / max_q) * 100
    print("\n=== Quiz Complete ===")
    print(f"Score: {score} / {max_q} ({percent:.1f}%)")
    print(f"Correct: {stats['correct']}, Wrong: {stats['wrong']}, Skipped: {stats['skipped']}")
    if percent >= 80:
        print("Great job! You clearly know your space facts.")
    elif percent >= 50:
        print("Nice effort! Keep studying and you'll improve. ")
    else:
        print("Keep practicing ,i believe you'll get better quickly.")


"""
----------------------------
 Ask-the-Universe mode
----------------------------
"""

def ask_universe():
    """
    Ask a question (free-text) and attempt to find an answer from UNIVERSE_QA dictionary.
    Matching strategy:
      1) normalize input and check for exact key
      2) check synonyms mapping
      3) try to find a key where most keywords appear (simple scoring)
    """

    print("\n--- Ask the Universe Mode ---")
    print("Type a question about the Solar System or space (type 'back' to return):")
    while True:
        q = input("\nYour question: ").strip()
        if not q:
            continue
        if q.lower() in ('back', 'exit', 'quit'):
            return
        key = normalize_text(q)

        # direct synonym
        if key in SYNONYMS:
            key2 = SYNONYMS[key]
            ans = UNIVERSE_QA.get(key2)
            if ans:
                print("\n" + wrap(ans))
                continue

        # direct match
        if key in UNIVERSE_QA:
            print("\n" + wrap(UNIVERSE_QA[key]))
            continue

        # kind of fuzzy keyword match: token intersection scoring
        tokens = set(key.split())
        best_key = None
        best_score = 0
        for k in UNIVERSE_QA.keys():
            k_tokens = set(k.split())
            score = len(tokens.intersection(k_tokens))
            if score > best_score:
                best_score = score
                best_key = k

        # threshold to accept best match
        if best_score >= 1 and best_key:
            ans = UNIVERSE_QA[best_key]
            print("\nI think you might mean: \"" + best_key + "\"")
            print(wrap(ans))
            continue

        # 4) check for keywords inside the user question
        found = False
        for k in UNIVERSE_QA.keys():
            if any(word in key for word in k.split()):
                print("\n" + wrap(UNIVERSE_QA[k]))
                found = True
                break
        if found:
            continue

        ## Not found
        print("\nSorry, I don't have a good answer for that question yet.")
        print("You can try a simpler question (e.g., 'What is the Sun?' or 'How many planets?').")


"""
----------------------------
 Main menu and loop
----------------------------
"""

def main_menu():
    clear_screen()
    print("="*60)
    print("   Solar System Quiz & Space Knowledge App")
    print("="*60)
    print("\nChoose an option:")
    print("  1) Take a Quiz (Beginner - 10 questions)")
    print("  2) Custom Quiz (choose number of questions)")
    print("  3) Ask the Universe (type any space question)")
    print("  4) About / Instructions")
    print("  5) Exit\n")

    choice = input("Enter choice (1-5): ").strip()
    return choice


def about_text():
    clear_screen()
    print("About this project\n")
    print("I built this simple CLI app to practice Python and basic astronomy/physics knowledge.")
    print("It features a multiple-choice quiz and an Ask-the-Universe mode with pre-defined answers.")
    print("\nHow to use:")
    print(" - For the quiz, select an option and answer using A/B/C/D (or type 'skip' to skip).")
    print(" - In Ask-the-Universe mode, type questions like 'What is the Sun?' or 'Is Pluto a planet?'.")
    input("\nPress Enter to return to the main menu...")


def run():
    # main program loop
    while True:
        choice = main_menu()
        if choice == '1':
            run_quiz(level='beginner', num_questions=10)
            input("\nPress Enter to return to the main menu...")
        elif choice == '2':
            while True:
                n = input("Enter number of questions (max {}): ".format(len(QUESTION_BANK))).strip()
                if not n.isdigit():
                    print("Please enter a number.")
                    continue
                n = int(n)
                if 1 <= n <= len(QUESTION_BANK):
                    run_quiz(num_questions=n)
                    input("\nPress Enter to return to the main menu...")
                    break
                else:
                    print("Choose a number between 1 and {}.".format(len(QUESTION_BANK)))
        elif choice == '3':
            ask_universe()
            input("\nPress Enter to return to the main menu...")
        elif choice == '4':
            about_text()
        elif choice == '5':
            print("Thank you for trying the Solar System Quiz. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    run()
