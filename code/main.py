from test_graph import run_tests, tests
from colorama import init, Fore

# make sure that after each coloured print, it returns back to normal.
init(autoreset=True)

if __name__ == "__main__":
    results = run_tests(tests)

    for r in results:
        result = r["result"]
        i = r["idx"]
        out = r["out"]
        t = r["test"]
        if result:
            print(f"{Fore.GREEN}Test {i+1} PASSED. Returns: {out}, expected: {t.exp}")
        else:
            print(f"{Fore.RED}Test {i+1} FAILED. Returns: {out}, expected: {t.exp}")