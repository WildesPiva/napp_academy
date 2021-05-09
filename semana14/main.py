from redes_sociais.classes.redes_sociais import (
    facebook,
    linkedin,
    github,
    instagram
)

redes = [
    'facebook',
    'linkedin',
    'github',
    'instagram'
]

if __name__ == "__main__":
    profile_type = input(f"Qual perfil deseja criar: {redes}")
    profile = eval(profile_type.lower())()
    print("Criando perfil... ", type(profile).__name__)
    print("Perfil possui as sessões", profile.getSections())
