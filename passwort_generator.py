    
import hashlib
import requests
import argparse
import random
import string


def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    chars = ''
    if use_upper:
        chars += string.ascii_uppercase
    if use_lower:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += string.punctuation
    if not chars:
        raise ValueError("Mindestens ein Zeichentyp muss ausgewählt werden.")
    return ''.join(random.SystemRandom().choice(chars) for _ in range(length))


def main():
    parser = argparse.ArgumentParser(description="Sicheres Passwort generieren.")
    parser.add_argument('-l', '--length', type=int, default=12, help='Passwortlänge (Standard: 12)')
    parser.add_argument('--no-upper', action='store_true', help='Keine Großbuchstaben verwenden')
    parser.add_argument('--no-lower', action='store_true', help='Keine Kleinbuchstaben verwenden')
    parser.add_argument('--no-digits', action='store_true', help='Keine Ziffern verwenden')
    parser.add_argument('--no-special', action='store_true', help='Keine Sonderzeichen verwenden')
    parser.add_argument('-c', '--count', type=int, default=1, help='Anzahl der zu generierenden Passwörter (Standard: 1)')
    parser.add_argument('--check-pwned', action='store_true', help='Prüft jedes Passwort gegen die HIBP Pwned Passwords API')
    parser.add_argument('--pause', action='store_true', help='Wartet am Ende auf Eingabe, damit das Fenster offen bleibt')
    args, unknown = parser.parse_known_args()

    def check_pwned(password):
        sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        prefix = sha1[:5]
        suffix = sha1[5:]
        url = f'https://api.pwnedpasswords.com/range/{prefix}'
        headers = {'Add-Padding': 'true'}
        try:
            resp = requests.get(url, headers=headers, timeout=5)
            if resp.status_code != 200:
                return 'Fehler bei API'
            hashes = (line.split(':') for line in resp.text.splitlines())
            for suf, count in hashes:
                if suf == suffix:
                    return f'GELEAKT ({count}x)'
            return 'OK'
        except Exception as e:
            return f'Fehler: {e}'

    def run_batch(count, length, use_upper, use_lower, use_digits, use_special, check_pwned_flag):
        try:
            generated = 0
            attempts = 0
            while generated < count:
                password = generate_password(
                    length=length,
                    use_upper=use_upper,
                    use_lower=use_lower,
                    use_digits=use_digits,
                    use_special=use_special
                )
                attempts += 1
                if check_pwned_flag:
                    status = check_pwned(password)
                    if status.startswith('GELEAKT'):
                        continue  # kein unsicheres Passwort anzeigen
                    elif status.startswith('Fehler'):
                        print(f"{password}  [{status}]")
                        continue
                    print(password)
                    generated += 1
                else:
                    print(password)
                    generated += 1
            if attempts > count:
                print(f"Hinweis: {attempts-count} unsichere Passwörter wurden verworfen.")
        except ValueError as e:
            print(f"Fehler: {e}")

    # Interaktives Terminal-UI, wenn keine Argumente übergeben wurden
    if len(unknown) == 0 and all(
        getattr(args, arg) == parser.get_default(arg)
        for arg in ['length', 'no_upper', 'no_lower', 'no_digits', 'no_special', 'count', 'check_pwned', 'pause']
    ):
        def ask_bool(prompt, default=True):
            while True:
                val = input(f"{prompt} [{'J/n' if default else 'j/N'}]: ").strip().lower()
                if val == '' and default is not None:
                    return default
                if val in ['j', 'y', 'yes']:
                    return True
                if val in ['n', 'no']:
                    return False
                print("Bitte j oder n eingeben.")

        def ask_int(prompt, default, minval=1, maxval=100):
            while True:
                val = input(f"{prompt} [Standard: {default}]: ").strip()
                if val == '':
                    return default
                try:
                    num = int(val)
                    if minval <= num <= maxval:
                        return num
                    else:
                        print(f"Bitte Zahl zwischen {minval} und {maxval} eingeben.")
                except ValueError:
                    print("Bitte eine gültige Zahl eingeben.")

        print("="*32)
        print("=     STRONK PWD Generator     =")
        print("="*32)
        while True:
            length = ask_int("Passwortlänge", 16, 4, 128)
            count = ask_int("Anzahl der Passwörter", 1, 1, 50)
            use_upper = ask_bool("Großbuchstaben verwenden?", True)
            use_lower = ask_bool("Kleinbuchstaben verwenden?", True)
            use_digits = ask_bool("Ziffern verwenden?", True)
            use_special = ask_bool("Sonderzeichen verwenden?", True)
            check_pwned_flag = ask_bool("Passwörter gegen HIBP prüfen?", True)
            print()
            run_batch(count, length, use_upper, use_lower, use_digits, use_special, check_pwned_flag)
            print()
            user = input("Weitere Passwörter generieren? (j/n): ").strip().lower()
            if user != 'j':
                break
        input("Enter drücken zum Beenden...")
    else:
        run_batch(
            args.count,
            args.length,
            not args.no_upper,
            not args.no_lower,
            not args.no_digits,
            not args.no_special,
            args.check_pwned
        )
        if args.pause:
            input("Enter drücken zum Beenden...")


if __name__ == "__main__":
    main()
