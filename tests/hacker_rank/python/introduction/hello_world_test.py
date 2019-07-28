from src.hacker_rank.python.introduction.hello_world import hello_world


# https://www.hackerrank.com/challenges/py-hello-world/problem
# noinspection SpellCheckingInspection
def test_hello_world(capsys):  # noqa
    hello_world()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"