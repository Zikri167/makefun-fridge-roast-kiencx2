import os

LINE = "My smart fridge's camera mistook my leftover pizza for a science experiment and asked if I wanted to publish the results."


def find_output_dir():
    for env in ("OUTPUT_DIR", "_OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        value = os.environ.get(env)
        if value:
            return value
    for path in ("/output", "./output", os.getcwd()):
        if os.path.isdir(path):
            return path
    return "/output"


def main():
    assert "\n" not in LINE and LINE.strip(), "line must be a single non-blank line"
    assert len(LINE) <= 160, f"line too long: {len(LINE)} chars"
    out_dir = find_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    with open(path, encoding="utf-8") as f:
        content = f.read()
    assert content == LINE + "\n", "entry.txt mismatch"


if __name__ == "__main__":
    main()
