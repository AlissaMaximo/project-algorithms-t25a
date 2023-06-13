from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(6, 4)

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("message", "invalidkey")


assert encrypt_message("kuroneko", 3) == "ruk_okeno"

assert encrypt_message("kuroneko", 6) == "oken_oruk"

assert encrypt_message("kuroneko", 9) == "okenoruk"
