from interfaces.anki_interface import AnkiInterface
from interfaces.user_interface import UserInterface
from interfaces.open_ai_interface import OpenAiInterface
from models.text import Text


def main():
    anki_interface = AnkiInterface()
    user_interface = UserInterface()
    open_ai_interface = OpenAiInterface()

    exit = False

    while not exit:
        all_decks = anki_interface.get_all_decks()
        read_deck, write_deck = user_interface.select_decks(all_decks)
        anki_interface.set_read_and_write_decks(read_deck, write_deck)

        restart = False

        while not restart:
            input = user_interface.enter_input()

            if input.lower().strip() == "restart":
                restart = True
                break

            if input.lower().strip() == "exit":
                exit = True
                break

            text = Text(input)

            anki_interface.find_existing_notes(text)
            user_interface.mark_tokens_for_lookup(text)
            open_ai_interface.look_up_tokens(text)
            # anki_interface.add_new_notes(text)


if __name__ == "__main__":
    main()
