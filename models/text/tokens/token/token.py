class Token:
    def __init__(self, session, spacy_token, openai_token):
        self.session = session
        self.spacy_token = spacy_token
        self.openai_token = openai_token

    def __repr__(self):
        indent = 5
        column_width = 30

        parts = [
            f"source: {self.source:<{22}}target: {self.target}",
            f"{'':<{indent}}{'pos_source: ' + self.pos_source:<{column_width}}pos_target: {self.pos_target}",
            f"{'':<{indent}}{'gender_source: ' + self.gender_source:<{column_width}}gender_target: {self.gender_target}",
            f"{'':<{indent}}{'number_source: ' + self.number_source:<{column_width}}number_target: {self.number_target}",
            f"{'':<{indent}}{'already_exists: ' + str(self.exists)}",
        ]

        return "\n".join(parts)

    def get_pos_source_and_target(self):
        pos_target_to_source = {
            "adjective": "adjectif",
            "adposition": "adposition",
            "adverb": "adverbe",
            "auxiliary": "auxiliaire",
            "conjunction": "conjonction",
            "coord conj": "conj de coord",
            "determiner": "déterminant",
            "interjection": "interjection",
            "noun": "nom",
            "numeral": "numéral",
            "particle": "particule",
            "preposition": "préposition",
            "pronoun": "pronom",
            "proper noun": "nom propre",
            "punctuation": "ponctuation",
            "subord conj": "conj de subord",
            "symbol": "symbole",
            "verb": "verbe",
            "other": "autre",
            "space": "espace",
        }

        pos_target = self.token["pos"]

        if not pos_target:
            return "none", "none"

        pos_source = pos_target_to_source[pos_target]
        return pos_source, pos_target

    def get_gender_source_and_target(self):
        gender_target_to_source = {
            "masculine": "masculin",
            "feminine": "féminin",
            "neuter": "neutre",
        }

        gender_target = self.token["gender"]

        if not gender_target:
            return "none", "none"

        gender_source = gender_target_to_source[gender_target]
        return gender_source, gender_target

    def get_number_source_and_target(self):
        number_target_to_source = {
            "singular": "singulier",
            "plural": "pluriel",
        }

        number_target = self.token["number"]

        if not number_target:
            return "none", "none"

        number_source = number_target_to_source[number_target]
        return number_source, number_target

    def check_if_exists(self):
        matching_notes = self.session.anki.find_notes(
            self.source,
        )

        if matching_notes:
            self.exists = True
        else:
            self.exists = False

        return self.exists