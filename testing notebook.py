from datetime import datetime
import textwrap


# ────────────────────────────────────────────────
#        Simple but pretty movie review writer
# ────────────────────────────────────────────────

def colored(text, color):
    """Very simple ANSI color helper"""
    colors = {
        'red': '\033[91m', 'green': '\033[92m',
        'yellow': '\033[93m', 'blue': '\033[94m',
        'magenta': '\033[95m', 'cyan': '\033[96m',
        'white': '\033[97m', 'gray': '\033[90m',
        'reset': '\033[0m'
    }
    return f"{colors.get(color, '')}{text}{colors['reset']}"


def stars(rating_out_of_10: float) -> str:
    full = int(rating_out_of_10 // 2)
    half = int((rating_out_of_10 % 2) >= 0.5)
    empty = 5 - full - half
    return "★" * full + "½" * half + "☆" * empty


def letter_grade(score: float) -> str:
    if score >= 9.0:  return "A+"
    if score >= 8.5:  return "A"
    if score >= 8.0:  return "A−"
    if score >= 7.5:  return "B+"
    if score >= 7.0:  return "B"
    if score >= 6.5:  return "B−"
    if score >= 6.0:  return "C+"
    if score >= 5.0:  return "C"
    return "D" if score >= 4.0 else "F"


def write_movie_review():
    print(colored("\n=== Movie Review Generator ===\n", "cyan"))

    # Basic info
    title = input("Movie title: ").strip()
    year = input("Year: ").strip()
    director = input("Director: ").strip()
    your_name = input("Your name / alias: ").strip() or "Anonymous"
    rating_10 = input("Rating (0–10, can be decimal): ").strip()

    try:
        rating = float(rating_10)
        if not 0 <= rating <= 10:
            rating = 5.0
            print("→ Rating clamped to 5.0")
    except:
        rating = 5.0
        print("→ Invalid rating → using 5.0")

    # Optional fields
    watch_date = input("Watch date (YYYY-MM-DD) [today]: ").strip()
    if not watch_date:
        watch_date = datetime.now().strftime("%Y-%m-%d")

    genres = input("Genres (comma separated): ").strip()
    runtime = input("Runtime in minutes (optional): ").strip()

    print("\n" + colored("Write your review (press Enter twice to finish):", "yellow"))
    print("─" * 60)

    lines = []
    while True:
        line = input()
        if line == "":
            if lines and lines[-1] == "":
                break
        lines.append(line)

    review_text = "\n".join(lines).strip()

    # ─── Build nice output ───────────────────────────────────────

    print("\n" + "=" * 70)
    print(colored(" REVIEW ".center(70), "magenta"))
    print("=" * 70 + "\n")

    print(colored(f"{title.upper()}", "white") +
          colored(f"  ({year})", "gray"))

    if director:
        print(colored("dir. ", "gray") + director)

    if genres:
        print(colored("• ", "gray") + genres.replace(",", ", "))

    if runtime:
        print(colored("• ", "gray") + f"{runtime} min")

    print()
    print(colored(f"★ {rating}/10   {stars(rating)}   {letter_grade(rating)}", "yellow"))
    print()

    if review_text:
        # Wrap text nicely
        wrapped = textwrap.fill(review_text, width=70,
                                initial_indent="  ", subsequent_indent="  ")
        print(wrapped)
        print()
    else:
        print(colored("  (no review text written)", "gray"))

    print(colored("— " + your_name, "cyan"), end="  •  ")
    print(colored(watch_date, "gray"))
    print("═" * 70 + "\n")


if __name__ == "__main__":
    try:
        write_movie_review()

        again = input("\nWrite another review? [y/N]: ").lower().strip()
        if again in ('y', 'yes'):
            print("\n" * 2)
            write_movie_review()
    except KeyboardInterrupt:
        print("\n" + colored("Bye 👋", "gray"))
